#!/usr/bin/env python3
"""Consistency checks for the hpf-taxonomy repository.

Python 3 standard library only, so this runs anywhere without a build step.
If the optional `jsonschema` package is installed, example records are also
validated against schema.json generically. Without it the built-in validator
still enforces every rule schema.json states.

These checks detect objective inconsistency: values that disagree between
files, records that do not match the schema, links that do not resolve,
formatting the house style forbids. They make no judgement about writing
quality or taxonomy policy. That judgement stays with human review.

Usage:
    python3 tools/check_standard.py                     # run every check
    python3 tools/check_standard.py --list              # list the checks and exit
    python3 tools/check_standard.py --checks links,schema   # run a subset

Exit status is 1 if there are findings, 0 otherwise.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWLIST_PATH = os.path.join(ROOT, "tools", "check-allowlist.txt")

# Documentation the checks read. Every one of these is published.
DOC_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "INTEGRATION.md",
    "SECURITY.md",
    "c2pa-mapping.md",
    "taxonomy.md",
    "docs/release-checklist.md",
    "docs/hpf-organisational-continuity.md",
    "docs/hpf-handover-checklist.md",
    "examples/README.md",
    # Contributor-facing templates. Public, rendered on every issue and pull
    # request, and indexed. They are covered because a withdrawn term
    # reintroduced here would be as public as one in the documentation.
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/change-proposal.yml",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
]

# The only classification machine values HPF defines. Sourced from schema.json
# at run time; this list is the expectation the schema is checked against.
CLASSIFICATIONS = ["no_ai", "assistive_ai", "generative_ai"]

# Machine values that were considered and rejected, or that belong to
# superseded drafts. None of them may appear as a value anywhere.
WITHDRAWN_VALUES = [
    "no_ai_used",
    "ai_assisted",
    "ai_generated",
    "partial_ai",
    "minimal_ai",
    "limited_ai",
    "incidental_ai",
    "substantial_ai",
    "human_only",
]

TAXONOMY_VERSION = "0.9"

findings = []
checks_run = []


def add(check, path, line, snippet):
    findings.append((check, path, line, snippet.strip()))


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def existing_docs():
    return [rel for rel in DOC_FILES if os.path.exists(os.path.join(ROOT, rel))]


def load_allowlist():
    """path:pattern per line. `path` may be a repo-relative path, a filename
    suffix, or `*`. `pattern` is a literal substring of the reported snippet."""
    entries = []
    if not os.path.exists(ALLOWLIST_PATH):
        return entries
    with open(ALLOWLIST_PATH, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.split("#", 1)[0].strip()
            if not line or ":" not in line:
                continue
            path, pattern = line.split(":", 1)
            entries.append((path.strip(), pattern.strip()))
    return entries


def allowlisted(entries, path, snippet):
    for allow_path, pattern in entries:
        if allow_path not in ("*", path) and not path.endswith(allow_path):
            continue
        if pattern in snippet:
            return True
    return False


def each_line(rel):
    text = read(rel)
    if text is None:
        return
    for number, line in enumerate(text.splitlines(), 1):
        yield number, line


# ---------------------------------------------------------------- schema


def load_schema():
    text = read("schema.json")
    if text is None:
        add("schema", "schema.json", 0, "file is missing")
        return None
    try:
        return json.loads(text)
    except ValueError as error:
        add("schema", "schema.json", 0, "does not parse: %s" % error)
        return None


def check_schema(schema):
    """The schema states the controlled values. Confirm it still states the
    ones the taxonomy defines, so a silent edit cannot widen the enum."""
    checks_run.append("schema")
    if schema is None:
        return
    props = schema.get("properties", {})

    enum = props.get("hpf_classification", {}).get("enum")
    if enum != CLASSIFICATIONS:
        add("schema", "schema.json", 0,
            "hpf_classification enum is %r, expected %r" % (enum, CLASSIFICATIONS))

    required = schema.get("required")
    if required != ["hpf_taxonomy_version", "hpf_classification"]:
        add("schema", "schema.json", 0,
            "required fields are %r, expected the two identifying fields" % (required,))

    descriptors = props.get("hpf_descriptors", {}).get("items", {}).get("enum")
    if not descriptors:
        add("schema", "schema.json", 0, "hpf_descriptors has no enum")
    elif sorted(descriptors) != sorted(set(descriptors)):
        add("schema", "schema.json", 0, "hpf_descriptors enum repeats a value")

    # Descriptors must be barred outside generative_ai. The schema does this
    # with if/then/else; confirm the else branch still forbids the field.
    branch = schema.get("else", {}).get("properties", {}).get("hpf_descriptors")
    if branch is not False:
        add("schema", "schema.json", 0,
            "schema no longer forbids hpf_descriptors outside generative_ai")


# -------------------------------------------------- built-in record check


def validate_record(record, schema):
    """Enforce exactly what schema.json states, without a third-party
    library. Returns a list of human-readable problems."""
    problems = []
    if not isinstance(record, dict):
        return ["record is not a JSON object"]

    props = schema.get("properties", {})

    for field in schema.get("required", []):
        if field not in record:
            problems.append("missing required field %s" % field)

    version = record.get("hpf_taxonomy_version")
    if version is not None:
        pattern = props.get("hpf_taxonomy_version", {}).get("pattern")
        if not isinstance(version, str):
            problems.append("hpf_taxonomy_version is not a string")
        elif pattern and not re.match(pattern, version):
            problems.append("hpf_taxonomy_version %r does not match %s" % (version, pattern))

    classification = record.get("hpf_classification")
    if classification is not None:
        enum = props.get("hpf_classification", {}).get("enum", [])
        if classification not in enum:
            problems.append("hpf_classification %r is not one of %r" % (classification, enum))

    if "hpf_descriptors" in record:
        descriptors = record["hpf_descriptors"]
        if classification != "generative_ai":
            problems.append("hpf_descriptors present on a %r record" % classification)
        elif not isinstance(descriptors, list):
            problems.append("hpf_descriptors is not an array")
        else:
            if not descriptors:
                problems.append("hpf_descriptors is empty; omit the field instead")
            if len(descriptors) != len(set(map(str, descriptors))):
                problems.append("hpf_descriptors repeats a value")
            allowed = props.get("hpf_descriptors", {}).get("items", {}).get("enum", [])
            for value in descriptors:
                if value not in allowed:
                    problems.append("descriptor %r is not in the schema enum" % value)

    return problems


def check_examples(schema):
    """Files named valid-*.json must validate. Files named invalid-*.json must
    fail, so a change that quietly loosens the schema is caught too."""
    checks_run.append("examples")
    if schema is None:
        return
    directory = os.path.join(ROOT, "examples")
    if not os.path.isdir(directory):
        add("examples", "examples/", 0, "directory is missing")
        return

    # Optional. The built-in validator enforces every rule schema.json states,
    # so a missing or old jsonschema degrades to one validator instead of two.
    # Probe for the class, not just the module: versions before 4.0 have no
    # Draft 2020-12 validator, and importing them tells you nothing.
    validator_class = None
    try:
        import jsonschema
        validator_class = getattr(jsonschema, "Draft202012Validator", None)
    except ImportError:
        pass
    if validator_class is None:
        print("note: jsonschema with Draft 2020-12 support not available, "
              "using the built-in validator only\n")

    names = sorted(name for name in os.listdir(directory) if name.endswith(".json"))
    if not names:
        add("examples", "examples/", 0, "no example records found")

    for name in names:
        rel = "examples/" + name
        text = read(rel)
        try:
            record = json.loads(text)
        except ValueError as error:
            add("examples", rel, 0, "does not parse: %s" % error)
            continue

        problems = validate_record(record, schema)

        if validator_class is not None:
            generic = [e.message for e in validator_class(schema).iter_errors(record)]
            # The two validators must agree on whether the record is valid.
            if bool(generic) != bool(problems):
                add("examples", rel, 0,
                    "built-in and jsonschema validators disagree: built-in %r, jsonschema %r"
                    % (problems, generic))
            problems = problems or generic

        if name.startswith("valid-") and problems:
            add("examples", rel, 0, "should validate but does not: %s" % "; ".join(problems))
        elif name.startswith("invalid-") and not problems:
            add("examples", rel, 0, "should fail validation but passes")
        elif not name.startswith(("valid-", "invalid-")):
            add("examples", rel, 0,
                "name must begin with valid- or invalid- so its expected result is testable")


# ------------------------------------------------------- taxonomy values


def check_taxonomy_values(schema):
    """No withdrawn or invented classification value may appear in any
    published file, and no descriptor may be used that the schema does not
    define."""
    checks_run.append("taxonomy-values")
    allow = load_allowlist()

    descriptors = []
    if schema:
        descriptors = schema.get("properties", {}).get(
            "hpf_descriptors", {}).get("items", {}).get("enum", [])

    withdrawn = re.compile(r"\b(%s)\b" % "|".join(WITHDRAWN_VALUES))
    # A descriptor-shaped token: lowercase snake_case starting with a known
    # descriptor prefix. Catches generated_sound, synthetic_voice and similar
    # near misses without flagging ordinary prose.
    descriptor_like = re.compile(r"\b((?:generated|synthetic|digital)_[a-z_]+)\b")

    for rel in existing_docs() + ["schema.json"]:
        for number, line in each_line(rel):
            match = withdrawn.search(line)
            if match and not allowlisted(allow, rel, line):
                add("taxonomy-values", rel, number,
                    "withdrawn classification value %r: %s" % (match.group(1), line))
            for token in descriptor_like.findall(line):
                if token in descriptors or allowlisted(allow, rel, line):
                    continue
                add("taxonomy-values", rel, number,
                    "descriptor-shaped value %r is not in the schema enum: %s" % (token, line))


def check_deprecated_language(schema):
    """`tier` was renamed to `category` in the June 2026 revision. Any
    surviving use is either a miss or a deliberate historical reference that
    belongs in the allowlist with a reason."""
    checks_run.append("deprecated-language")
    allow = load_allowlist()
    tier = re.compile(r"\btiers?\b", re.IGNORECASE)
    for rel in existing_docs():
        for number, line in each_line(rel):
            if tier.search(line) and not allowlisted(allow, rel, line):
                add("deprecated-language", rel, number, "superseded `tier` language: %s" % line)


def check_version_parity():
    """Every file that names the taxonomy version must name the same one."""
    checks_run.append("version-parity")
    citation = read("CITATION.cff") or ""
    match = re.search(r'^version:\s*"?([0-9.]+)"?\s*$', citation, re.MULTILINE)
    if not match:
        add("version-parity", "CITATION.cff", 0, "no version field found")
    elif match.group(1) != TAXONOMY_VERSION:
        add("version-parity", "CITATION.cff", 0,
            "version %s does not match taxonomy version %s" % (match.group(1), TAXONOMY_VERSION))

    taxonomy = read("taxonomy.md") or ""
    if "Version %s" % TAXONOMY_VERSION not in taxonomy:
        add("version-parity", "taxonomy.md", 0,
            "does not state Version %s" % TAXONOMY_VERSION)

    governance = read("GOVERNANCE.md") or ""
    if "Version %s" % TAXONOMY_VERSION not in governance:
        add("version-parity", "GOVERNANCE.md", 0,
            "does not state Version %s" % TAXONOMY_VERSION)


# ------------------------------------------------------------ statement


def check_statement():
    """The Statement of Shared Intent is withdrawn. It must not appear in the
    repository as copy, as a route or as a file."""
    checks_run.append("statement")
    allow = load_allowlist()
    patterns = [
        (re.compile(r"statement of shared intent", re.IGNORECASE), "Statement of Shared Intent copy"),
        (re.compile(r"/statement(?:\.html)?\b"), "legacy /statement route"),
        (re.compile(r"\bsignator(?:y|ies)\b", re.IGNORECASE), "signatory language"),
    ]
    for rel in existing_docs():
        for number, line in each_line(rel):
            for pattern, label in patterns:
                if pattern.search(line) and not allowlisted(allow, rel, line):
                    add("statement", rel, number, "%s: %s" % (label, line))

    for current, _dirs, names in os.walk(ROOT):
        if ".git" in current:
            continue
        for name in names:
            if "shared_intent" in name.lower() or "shared-intent" in name.lower():
                rel = os.path.relpath(os.path.join(current, name), ROOT)
                add("statement", rel, 0, "file name refers to the Statement of Shared Intent")


# ------------------------------------------------------------- house style


def check_em_dashes():
    checks_run.append("em-dashes")
    allow = load_allowlist()
    for rel in existing_docs() + ["schema.json"]:
        for number, line in each_line(rel):
            if "—" in line and not allowlisted(allow, rel, line):
                add("em-dashes", rel, number, line)


# ----------------------------------------------------------------- links


def check_links():
    """Resolve every relative Markdown link, and every absolute link that
    points back into this repository, against the files on disk. No network
    access: an external URL is not this repository's business."""
    checks_run.append("links")
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    self_blob = re.compile(
        r"^https://(?:raw\.)?github(?:usercontent)?\.com/[^/]+/hpf-taxonomy/"
        r"(?:blob/|raw/)?(?:main/)?(.+)$", re.IGNORECASE)

    for rel in existing_docs():
        base = os.path.dirname(rel)
        for number, line in each_line(rel):
            for target in link.findall(line):
                if target.startswith("#") or target.startswith("mailto:"):
                    continue

                match = self_blob.match(target)
                if match:
                    inner = match.group(1).split("#", 1)[0]
                    if inner and not os.path.exists(os.path.join(ROOT, inner)):
                        add("links", rel, number,
                            "link to this repository points at a missing file: %s" % target)
                    continue

                if target.startswith(("http://", "https://")):
                    continue

                path = target.split("#", 1)[0]
                if not path:
                    continue
                resolved = os.path.normpath(os.path.join(ROOT, base, path))
                if not os.path.exists(resolved):
                    add("links", rel, number, "broken relative link: %s" % target)


# ------------------------------------------------------------------ main


DESCRIPTIONS = [
    ("schema", "schema.json states the controlled values the taxonomy defines"),
    ("examples", "example records validate, or fail, as their filename says"),
    ("taxonomy-values", "no withdrawn classification or undefined descriptor value"),
    ("deprecated-language", "no superseded `tier` wording"),
    ("version-parity", "every file names the same taxonomy version"),
    ("statement", "no Statement of Shared Intent copy, route or file"),
    ("em-dashes", "no em dashes in published files"),
    ("links", "relative and self-referencing links resolve"),
]


def main():
    if "--list" in sys.argv:
        for name, description in DESCRIPTIONS:
            print("%-20s %s" % (name, description))
        return 0

    selected = None
    if "--checks" in sys.argv:
        index = sys.argv.index("--checks")
        if index + 1 >= len(sys.argv):
            print("--checks needs a comma-separated list of check names")
            return 2
        selected = [name.strip() for name in sys.argv[index + 1].split(",") if name.strip()]
        known = {name for name, _ in DESCRIPTIONS}
        unknown = [name for name in selected if name not in known]
        if unknown:
            print("unknown check(s): %s" % ", ".join(unknown))
            print("known checks: %s" % ", ".join(sorted(known)))
            return 2

    def wanted(name):
        return selected is None or name in selected

    schema = load_schema()
    if wanted("schema"):
        check_schema(schema)
    if wanted("examples"):
        check_examples(schema)
    if wanted("taxonomy-values"):
        check_taxonomy_values(schema)
    if wanted("deprecated-language"):
        check_deprecated_language(schema)
    if wanted("version-parity"):
        check_version_parity()
    if wanted("statement"):
        check_statement()
    if wanted("em-dashes"):
        check_em_dashes()
    if wanted("links"):
        check_links()

    print("HPF standard checks")
    print("%d checks run over %d published files\n" % (len(checks_run), len(existing_docs())))

    if not findings:
        print("PASS: no findings.")
        return 0

    for check, path, line, snippet in findings:
        where = "%s:%d" % (path, line) if line else path
        print("  [%s] %s\n      %s" % (check, where, snippet[:200]))
    print("\nFAIL: %d finding(s)." % len(findings))
    print("If a finding is a deliberate exception, record it in "
          "tools/check-allowlist.txt with a reason. Do not delete a check to silence it.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
