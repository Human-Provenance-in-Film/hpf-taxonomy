# Human Provenance in Film

**HPF AI Disclosure Taxonomy, v0.9.4 pre-v1 draft**

The public consultation closed on 31 October 2026. Feedback on the standard remains welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## What HPF is for

HPF is a free, open standard for declaring AI output present in finished film and television productions. It gives audiences and receiving organisations a common account of how AI was used. The producer selects one of three categories for each released version and records it in a signed declaration, which travels with the production's existing deal, delivery and other production paperwork. Consistent disclosure also makes it possible to study how buyers and audiences respond to different kinds of AI use.

The organising principle: **is AI output present in the named finished version? If so, did the AI process human-created material or originate new content?**

| Value stored in `hpf_classification` | Label shown to people |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

HPF is a self-declaration standard. It does not certify productions, audit workflows, or determine consent, rights or regulatory compliance.

---

## Start here

| I want to | Go to |
|---|---|
| Understand the categories and classify a production | [taxonomy.md](taxonomy.md), and [Classify and declare your production](https://humanprovenance.film/resources/classify-and-declare-your-production/) on the website |
| Make a declaration | The [HPF AI Disclosure Form](https://humanprovenance.film/disclosure-form/) |
| Ask for and receive declarations, with no software change | [Add HPF to your workflow](https://humanprovenance.film/resources/add-hpf-to-your-workflow/) |
| Hold HPF information in a system | [INTEGRATION.md](INTEGRATION.md), [schema.json](schema.json) and [examples/](examples/) |
| Carry a classification in a C2PA Content Credential | [c2pa-mapping.md](c2pa-mapping.md), a working proposal |
| Suggest a change or report a problem | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Check versions, governance and history | [GOVERNANCE.md](GOVERNANCE.md) |

---

## How a declaration travels

The producer signs one declaration for each released version of a production, on paper or digitally. It can travel with the existing paperwork to sales agents, distributors, platforms, festivals and other recipients, which decide how to use it under their own policies. The classification is declared, not derived from technical analysis of the content.

Technical integration is optional. An organisation that already holds title information in a system may also store the classification as an HPF record, using the fields in [schema.json](schema.json), and may carry it in a C2PA Content Credential where that is technically implemented. The signed declaration remains the authoritative source at every stage.

---

## Repository contents

| File | Description |
|---|---|
| [taxonomy.md](taxonomy.md) | The standard: categories, organising principle, classification test, scope, production cases and the declaration. |
| [schema.json](schema.json) | JSON Schema for the HPF record. |
| [INTEGRATION.md](INTEGRATION.md) | Guidance for holding HPF records in a system. Informative. |
| [c2pa-mapping.md](c2pa-mapping.md) | Proposed mapping of the HPF record to a C2PA assertion. Working proposal. |
| [GOVERNANCE.md](GOVERNANCE.md) | Amendment process (including maintenance after v1.0), version history, and governance handoff commitment. |
| [docs/hpf-organisational-continuity.md](docs/hpf-organisational-continuity.md) | Stewardship conditions that cannot change, the conditions for moving to a new steward, and what such a steward would have to preserve. |
| [docs/hpf-handover-checklist.md](docs/hpf-handover-checklist.md) | Index of the records a future steward needs, and where each one is. |
| [docs/release-checklist.md](docs/release-checklist.md) | What has to pass before a revision of the draft is tagged and published. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to send feedback and how proposals are handled. |
| [SECURITY.md](SECURITY.md) | How to report a suspected vulnerability privately, and what is in scope. |
| [CITATION.cff](CITATION.cff) | Citation metadata for referencing the standard. |
| [LICENSE.md](LICENSE.md) | CC BY 4.0 and patent non-assertion. |
| [examples/](examples/) | Example HPF records that must validate, or fail, as their filenames say. |
| [tools/](tools/) | The consistency checks. `python3 tools/check_standard.py`, standard library only, run on every push and pull request. |

---

## Licence

CC BY 4.0. No patent rights are asserted over the taxonomy methodology. See [LICENSE.md](LICENSE.md).

---

## Contact

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
