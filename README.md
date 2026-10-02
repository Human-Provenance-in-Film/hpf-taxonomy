# Human Provenance in Film

**HPF AI Disclosure Taxonomy, v0.9.3 draft for consultation**

Consultation closes 31 October 2026.

---

## What this is

A three-category classification standard for AI disclosure in film and television, designed to travel with a production's existing deal, delivery and other production paperwork.

Without more consistent disclosure, it is difficult to study whether and how buyers and audiences respond to different forms of AI use in finished screen work.

---

## Who this repository is for

The files in this repository are intended for:

- **Platform engineers and catalogue / CMS developers** at distributors, streamers, and broadcasters: [schema.json](schema.json) and [INTEGRATION.md](INTEGRATION.md)
- **Sales agency and distributor technical staff** managing deal and delivery paperwork: [INTEGRATION.md](INTEGRATION.md)
- **Delivery portal and ingest system developers**: [INTEGRATION.md](INTEGRATION.md) and [schema.json](schema.json)
- **C2PA SDK developers and CAI members**: [c2pa-mapping.md](c2pa-mapping.md) and [INTEGRATION.md](INTEGRATION.md)
- **Post-production tool developers** building toward adoption: [INTEGRATION.md](INTEGRATION.md)
- **Regulators and policy staff** assessing the framework: [taxonomy.md](taxonomy.md) and [GOVERNANCE.md](GOVERNANCE.md)

The full taxonomy specification and plain-language guidance for productions are at [humanprovenance.film](https://humanprovenance.film), and the producer declaration form is at [humanprovenance.film/disclosure-form](https://humanprovenance.film/disclosure-form/).

---

## The three categories

Built on a single organising principle: **is AI output present in the named finished version? If so, did the AI process human-created material or originate new content?**

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

For category definitions, scope, classification test, and edge cases: [taxonomy.md](taxonomy.md).

---

## How classification travels: signed declaration to metadata

HPF classification originates as a signed producer declaration, made on paper or digitally, for one released version of the production. It is not derived from technical analysis of the content.

The declaration can travel with the film through existing deal, delivery and other production paperwork. An organisation that holds title records in a system may record it in the required schema fields: the standard version, the released version and the classification. The core fields may be tested in integration during consultation. Implementers should retain the HPF standard version used and should not treat the provisional descriptor array as stable for production implementation. The signed producer declaration is the authoritative source at every stage; the schema is how part of that record is held and passed on in technical systems.

```
Producer signs declaration for a released version
        |
        | travels with deal and delivery paperwork
        v
Distributor / buyer / streamer receives delivery
        |
        | platform or ingest system translates declaration into schema fields
        v
HPF classification stored in content catalogue / CMS
        |
        v
Classification available for display, reporting, and downstream pass-through
```

Where technically implemented, the classification may also be carried in or alongside the delivery file as a C2PA Content Credential, at any point in the chain. This is optional and complementary. See [c2pa-mapping.md](c2pa-mapping.md) for the proposed technical implementation.

Pending broader adoption, delivery portal and ingest systems, and post-production tools with delivery workflows, may also translate the declaration into the schema at the point of delivery acceptance, upstream of the receiving platform. Where this happens, the signed producer declaration still governs. See [INTEGRATION.md](INTEGRATION.md) for implementation guidance.

---

## Repository contents

| File | Description |
|---|---|
| [taxonomy.md](taxonomy.md) | Category definitions, organising principle, classification test, scope, and edge cases. |
| [schema.json](schema.json) | JSON Schema for HPF metadata fields. For platform engineers and ingest system developers. |
| [INTEGRATION.md](INTEGRATION.md) | Implementation guide for platform, sales agency, ingest, delivery portal, post-production tool, and C2PA developers. |
| [c2pa-mapping.md](c2pa-mapping.md) | Proposed mapping of HPF categories to C2PA assertion types. Working proposal. |
| [GOVERNANCE.md](GOVERNANCE.md) | Amendment process, version history, and governance handoff commitment. |
| [docs/hpf-organisational-continuity.md](docs/hpf-organisational-continuity.md) | Stewardship conditions that cannot change, the conditions for moving to a new steward, and what such a steward would have to preserve. |
| [docs/hpf-handover-checklist.md](docs/hpf-handover-checklist.md) | Index of the records a future steward needs, and where each one is. |
| [docs/release-checklist.md](docs/release-checklist.md) | What has to pass before a revision of the draft is tagged and published. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to respond to the consultation and how proposals are handled. |
| [SECURITY.md](SECURITY.md) | How to report a suspected vulnerability privately, and what is in scope. |
| [CITATION.cff](CITATION.cff) | Citation metadata for referencing the standard. |
| [LICENSE.md](LICENSE.md) | CC BY 4.0 and patent non-assertion. |
| [examples/](examples/) | Worked records that must validate, or fail, as their filenames say. For anyone implementing against the schema or proposing a change to it. |
| [tools/](tools/) | The consistency checks. `python3 tools/check_standard.py`, standard library only, run on every push and pull request. |

---

## Licence

CC BY 4.0. No patent rights are asserted over the taxonomy methodology. See [LICENSE.md](LICENSE.md).

---

## Contact

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
