# HPF handover checklist

**Checklist version 1.0, August 2026.**

An index of what a future steward needs and where each thing is. It points at
sources rather than copying them, because a copy goes stale and then two
documents disagree.

The principles this serves are in
[hpf-organisational-continuity.md](hpf-organisational-continuity.md). Read that
first if you are deciding whether a handover should happen. Read this if it is
happening.

## How to use it

Work down the sections. For each row, confirm the source exists, is current, and
can be reached by the person taking over. A row you cannot confirm becomes an
open action with a name against it.

Two rules hold throughout:

- **One authoritative copy of each record.** If you find a second editable copy,
  resolve which one is authoritative and remove the other.
- **No credentials in writing.** No password, token, recovery code or security
  answer belongs in this repository, in the private records or in any pack sent
  to a successor. Access moves person to person, through the system that holds
  it, at handover.

---

## 1. The standard

| What | Where |
| --- | --- |
| Category definitions, organising principle, classification test, scope, edge cases | [taxonomy.md](../taxonomy.md) |
| Controlled values and record structure | [schema.json](../schema.json), with worked records in [examples/README.md](../examples/README.md) |
| Implementation guidance | [INTEGRATION.md](../INTEGRATION.md) |
| Proposed C2PA mapping | [c2pa-mapping.md](../c2pa-mapping.md) |
| Licence and patent non-assertion | [LICENSE.md](../LICENSE.md) |
| Citation metadata | [CITATION.cff](../CITATION.cff) |
| Plain-language guidance and the producer declaration form | [humanprovenance.film](https://humanprovenance.film) |

`taxonomy.md` and `schema.json` are the authoritative pair. Where anything else
disagrees with them, including this checklist, they win.

## 2. Release history and how a release happens

| What | Where |
| --- | --- |
| Version history and the amendment process | [GOVERNANCE.md](../GOVERNANCE.md) |
| Published artefacts | The tags and releases on `hpf-taxonomy`. A published tag never moves. |
| What has to pass before a tag, and how the tag relates to the taxonomy version | [release-checklist.md](release-checklist.md) |
| Who approves a release | The release owner, named in the private decision authority record. See section 3 of the continuity statement. |
| Repository checks | `tools/check_standard.py`, run by `.github/workflows/standard-checks.yml` |
| Deliberate exceptions to the checks | `tools/check-allowlist.txt`, each with its reason |
| The record of each past release | Release archive, private. See section 5. |

## 3. How change is proposed and decided

| What | Where |
| --- | --- |
| How to propose a change, how proposals are handled, and the confidentiality rules that apply to them | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Issue and pull request templates | `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md` |
| Open work and its status | Issues and the `v0.9 consultation close` milestone on `hpf-taxonomy` |
| Private vulnerability reporting | [SECURITY.md](../SECURITY.md) |
| Consultation responses, their status and the decision against each | Consultation tracker, private. See section 5. |
| Why the taxonomy says what it says | The Decision and Rationale columns of the consultation tracker. That is the decision record, and there is no separate one. |

## 4. Systems

Every system HPF depends on, who administers it, and how each is recovered, are
recorded in the private access register. That register is not published, and
neither is the list of systems: an inventory of a project's infrastructure and
accounts is of use mainly to someone attacking it. A steward receives it at
handover.

Getting the site running from `hpf-site` alone is one of the four tasks in the
handover rehearsal, in section 5 of the continuity statement.

## 5. Private records

Held in the private Drive, which is access-controlled. One index in the Drive
lists them all and is the entry point for everything in this section. A steward
receives access to it at handover.

- Asset register
- Private access register
- Decision authority record
- Legal and licensing record
- Funding record
- Stakeholder map
- Operational calendar
- Consultation record, including the tracker whose Decision and Rationale columns are the decision record
- Release archive

They are private because they hold access arrangements, personal data collected
under stated terms, and unpublished consultation material. The privacy notice at
[humanprovenance.film](https://humanprovenance.film) says how personal data is
handled and who the data controller is.

## 6. Unresolved work

A steward should be able to see what is undecided without asking anyone.

| What | Where |
| --- | --- |
| Governance questions that are open on purpose | Section 4 of [hpf-organisational-continuity.md](hpf-organisational-continuity.md) |
| Open change proposals and bugs | Issues on `hpf-taxonomy` |
| Work deferred past the consultation | Issues labelled `deferred-v1.0` |
| Known contradictions between documents | The documentation conflict register, private continuity records |
| Consultation responses not yet decided | Consultation tracker, filtered on undecided status |

## 7. Completing a handover

The steps that finish a transfer, including the access checks and the assessment
of the successor against sections 1, 6 and 7 of the continuity statement, are in
the private continuity records. Two of them are public commitments and are
recorded here so that anyone can check they happened: the transfer is published,
and [GOVERNANCE.md](../GOVERNANCE.md) is updated to name the new steward.

---

CC BY 4.0. See [LICENSE.md](../LICENSE.md). contact@humanprovenance.film |
[humanprovenance.film](https://humanprovenance.film)
