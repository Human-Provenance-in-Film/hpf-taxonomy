# What this changes

<!-- One or two sentences. What is different afterwards, and why. -->

Related issue:
Taxonomy version and revision:

## Taxonomy meaning

- [ ] The three classifications are unchanged: No AI Used, Assistive AI, Generative AI.
- [ ] The classification test still turns on AI output present in the finished production, and on whether AI processed supplied material or originated new content.
- [ ] The highest-category rule still applies, with no threshold and no de minimis exception.
- [ ] Descriptors apply only to Generative AI and are still marked provisional.
- [ ] No new classification, descriptor or controlled value without an explicit taxonomy decision recorded in an issue.

If this changes what a production would be classified as, say so here and link the decision:

## Schema and example consistency

- [ ] `schema.json`, `taxonomy.md` and `INTEGRATION.md` state the same controlled values.
- [ ] `examples/` covers any new or changed rule, in both directions.
- [ ] `python3 tools/check_standard.py` passes.

## Scope boundaries

- [ ] Nothing here requests, stores, discloses, validates or carries consent, authorisation, licensing, compensation, rights ownership or compliance information.
- [ ] No recipient-specific, guild-specific, union-specific, platform-specific, policy-specific or person-level field.
- [ ] Legal, contractual and collective-agreement terms are treated as external policy language unless the taxonomy already defines them.
- [ ] Nothing describes C2PA as deciding or validating the classification.

## Missing states

- [ ] Missing, unknown or undisclosed information is never presented as No AI Used.
- [ ] An absent record stays absent. No null fields, no default value.

## Statement removal

- [ ] No Statement of Shared Intent copy, route, file, metadata or signatory language.

## Public copy

- [ ] UK English. No em dashes.
- [ ] No claim of verification, certification, audit, approval, eligibility or compliance.
- [ ] No claim of adoption, endorsement, partnership, accreditation or independent governance that is not already true.
- [ ] Direct, specific sentences. No promotional inflation.

## Related surfaces

Wording is duplicated across the repository and the site. List every place that says the same thing, and confirm each is consistent:

- [ ] `README.md`
- [ ] `taxonomy.md`
- [ ] `INTEGRATION.md`
- [ ] `c2pa-mapping.md`
- [ ] `GOVERNANCE.md`
- [ ] `CONTRIBUTING.md`
- [ ] Site pages in `hpf-site`, including `site/taxonomy.md`, the FAQ, How it works and the disclosure form
- [ ] Not applicable

## Tests

- [ ] `python3 tools/check_standard.py`
- [ ] `python3 tools/check_site.py` in `hpf-site`, if site copy changed
- [ ] Nothing else applies

Findings, and any allowlist entry added with its reason:

## Version history

- [ ] The version history in `GOVERNANCE.md` records this change, or this change is editorial and does not need an entry.
- [ ] `CITATION.cff` still names the most recent released version, not an unreleased one.
