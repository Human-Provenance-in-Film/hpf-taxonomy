# Human Provenance in Film

**HPF AI Disclosure Taxonomy, v0.9 draft for consultation**

Consultation closes 31 October 2026.

---

## What this is

A three-category classification standard for AI disclosure in film and television, designed to travel in chain of title and deal documentation (the legal and rights documentation that accompanies a film through distribution and licensing).

Without a consistent disclosure standard, there is no reliable market data on whether buyers and audiences distinguish between AI-generated and human-authored content.

---

## Who this repository is for

The files in this repository are intended for:

- **Platform engineers and catalogue / CMS developers** at distributors, streamers, and broadcasters: [schema.json](schema.json) and [INTEGRATION.md](INTEGRATION.md)
- **Sales agency and distributor technical staff** managing chain of title and deal documentation: [INTEGRATION.md](INTEGRATION.md)
- **Delivery portal and ingest system developers**: [INTEGRATION.md](INTEGRATION.md) and [schema.json](schema.json)
- **C2PA SDK developers and CAI members**: [c2pa-mapping.md](c2pa-mapping.md) and [INTEGRATION.md](INTEGRATION.md)
- **Post-production tool developers** building toward adoption: [INTEGRATION.md](INTEGRATION.md)
- **Regulators and policy staff** assessing the framework: [taxonomy.md](taxonomy.md) and [GOVERNANCE.md](GOVERNANCE.md)

The full taxonomy specification and plain-language guidance for productions are at [humanprovenance.film](https://humanprovenance.film), and the producer declaration form is at [humanprovenance.film/disclosure-form](https://humanprovenance.film/disclosure-form/).

---

## The three categories

Built on a single organising principle: **is AI output present in the finished film, and did it process human work or originate new content?**

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

For category definitions, scope, classification test, and edge cases: [taxonomy.md](taxonomy.md).

---

## How classification travels: paper to code

HPF classification originates as a signed producer declaration in the chain of title. It is not derived from technical analysis of the content.

The declaration travels with the film through deal and delivery documentation. At the point of platform or distributor ingest, it is translated into the two-field schema and stored in the content catalogue. The paper declaration is the authoritative record at every stage; the schema is how that record is held and passed on in technical systems.

```
Producer signs paper declaration
        |
        | travels in chain of title
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

Pending broader adoption, delivery portal and ingest systems, and post-production tools with delivery workflows, may also translate the declaration into the schema at the point of delivery acceptance, upstream of the receiving platform. Where this happens, the paper declaration still governs. See [INTEGRATION.md](INTEGRATION.md) for implementation guidance.

---

## Repository contents

| File | Description |
|---|---|
| [taxonomy.md](taxonomy.md) | Category definitions, organising principle, classification test, scope, and edge cases. |
| [schema.json](schema.json) | JSON Schema for HPF metadata fields. For platform engineers and ingest system developers. |
| [INTEGRATION.md](INTEGRATION.md) | Implementation guide for platform, sales agency, ingest, delivery portal, post-production tool, and C2PA developers. |
| [c2pa-mapping.md](c2pa-mapping.md) | Proposed mapping of HPF categories to C2PA assertion types. Working proposal. |
| [GOVERNANCE.md](GOVERNANCE.md) | Amendment process, version history, and governance handoff commitment. |
| [LICENSE.md](LICENSE.md) | CC BY 4.0 and patent non-assertion. |

---

## Licence

CC BY 4.0. No patent rights are asserted over the taxonomy methodology. See [LICENSE.md](LICENSE.md).

---

## Contact

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
