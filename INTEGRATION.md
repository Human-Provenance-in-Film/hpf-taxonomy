# HPF integration guide

**HPF Guidance for the HPF AI Disclosure Standard v0.9.4.** Informative.
Updated November 2026. The public consultation closed on 31 October 2026.

This guide explains how to store, validate, and pass on HPF metadata. The classifications, definitions, permitted values, and required fields are defined in [taxonomy.md](taxonomy.md) and [schema.json](schema.json). Those documents take precedence if this guide conflicts with them. Fields, permitted values, and ways of carrying the metadata may change before v1.0.

**Technical integration is optional.** You can request a signed declaration, keep it with the relevant title or submission, and apply your organisation's policy without changing any software. [Add HPF to your workflow](https://humanprovenance.film/resources/add-hpf-to-your-workflow/) explains that process. This guide is for organisations storing HPF metadata in a system.

In this note, the *HPF record* is the set of machine-readable fields defined in [schema.json](schema.json). The *signed declaration* is the document the producer signs. A *supporting production record*, such as an asset log or a supplier reply, is a separate document that stays with the production.

---

## The current HPF record

A record made under 0.9.3 or 0.9.4 has three required fields:

```json
{
  "hpf_standard_version": "0.9.4",
  "hpf_released_version": "Theatrical cut",
  "hpf_classification": "assistive_ai"
}
```

`hpf_standard_version` identifies the version of the Standard applied, using a string in the form `MAJOR.MINOR` or `MAJOR.MINOR.PATCH`.

`hpf_released_version` identifies the released version covered, using the wording in the declaration. HPF prescribes no identifier scheme. This field was added in 0.9.3.

See [schema.json](schema.json) for the field definitions and [examples/](examples/) for valid and invalid records. [Records made under earlier versions](#records-made-under-earlier-versions) explains historical compatibility.

`hpf_classification` takes one of three values. Systems store and pass on the value. Where a classification is shown to people, show the label.

| Value stored in `hpf_classification` | Label shown to people |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

A production carries one classification, at the highest applicable category, for the released version the declaration covers. There is no threshold and no de minimis exception. [taxonomy.md](taxonomy.md) has the classification test.

You can implement these fields while HPF remains a pre-v1 draft. Store the standard version with every record so it can always be interpreted under the version used to make it.

---

## Descriptors

`hpf_descriptors` is optional. It carries the descriptors the declaring party recorded, and nothing else. The descriptor vocabulary was adopted in 0.9.4, and the field is specified in [schema.json](schema.json) and in the Descriptors section of [taxonomy.md](taxonomy.md#descriptors), which defines what each value means.

| Value stored in `hpf_descriptors` | Label shown to people | Allowed on |
|---|---|---|
| `altered_performance` | Altered performance | `assistive_ai`, `generative_ai` |
| `digital_replica` | Digital replica | `generative_ai` |
| `synthetic_performance` | Synthetic performance | `generative_ai` |
| `generated_voice` | Generated voice | `generative_ai` |
| `generated_visual_content` | Generated visual content | `generative_ai` |
| `generated_writing` | Generated writing | `generative_ai` |
| `generated_music` | Generated music | `generative_ai` |

The rules:

- Where the field is present, it is an array of one or more of the values above, each at most once. The order carries no meaning; compare two arrays as sets.
- No descriptor applies to `no_ai`. `assistive_ai` allows `altered_performance` only. `generative_ai` allows any combination.
- Where no descriptor is declared, omit the field. Do not write an empty array or `null`.
- An omitted field means no descriptor was declared. It does not mean none applies. Do not add descriptors on the declaring party's behalf from the classification, the factual summary, tool names, file metadata, or detection output, and do not require them: a declaration without descriptors is complete.
- A descriptor never determines or changes the classification.

### Valid records

No AI Used. No descriptor applies, so the field is absent:

```json
{
  "hpf_standard_version": "0.9.4",
  "hpf_released_version": "Theatrical cut",
  "hpf_classification": "no_ai"
}
```

Assistive AI with Altered performance, for example cosmetic AI de-ageing of a performance captured in full:

```json
{
  "hpf_standard_version": "0.9.4",
  "hpf_released_version": "Theatrical cut",
  "hpf_classification": "assistive_ai",
  "hpf_descriptors": ["altered_performance"]
}
```

Generative AI with several descriptors, for example AI-generated speech representing an identifiable actor, inserted into footage of their captured performance. Each value records a different fact:

```json
{
  "hpf_standard_version": "0.9.4",
  "hpf_released_version": "Theatrical cut",
  "hpf_classification": "generative_ai",
  "hpf_descriptors": ["digital_replica", "generated_voice", "altered_performance"]
}
```

### Invalid records, and what validation does

Each case below is a file in [examples/](examples/) that the repository checks must fail.

| Record | Why it is invalid | File |
|---|---|---|
| `no_ai` with `["generated_music"]` | No descriptor applies to No AI Used. | `invalid-descriptors-on-no-ai.json` |
| `assistive_ai` with `["generated_music"]` | Assistive AI allows Altered performance only. | `invalid-descriptors-on-assistive.json` |
| `assistive_ai` with `["altered_performance", "generated_voice"]` | One value is allowed and one is not; the record is invalid as a whole. | `invalid-assistive-ai-mixed-descriptors.json` |
| `generative_ai` with `["generated_voice", "generated_voice"]` | A value is repeated. | `invalid-duplicate-descriptors.json` |
| `generative_ai` with `[]` | An empty array is not how to record that no descriptor was declared. | `invalid-empty-descriptors.json` |
| `generative_ai` with `"generated_music"` | The field must be an array, even for one value. | `invalid-descriptors-not-an-array.json` |
| `generative_ai` with a value that is not one of the seven above, such as an invented or misspelt descriptor | The value is not defined, so it has no meaning in any version. | `invalid-descriptor-outside-enum.json` |

Schema validation rejects all the cases above. If you receive an invalid record, retain it as received and flag it for follow-up with the declaring party. Do not remove, add, or merge values to repair it, or change the classification to make a descriptor fit.

If your system collects descriptors through an intake form, it should:

- start with no descriptors selected;
- allow multiple selections from the values permitted for the chosen classification;
- retain any selection that becomes invalid after a classification change and ask the person to resolve it, rather than silently removing it.

The [HPF AI Disclosure Form](https://humanprovenance.film/disclosure-form/) follows this approach and uses the same machine-readable values for its checkboxes.

### Storing, passing on, and showing descriptors

- Store the values exactly as received, with the record's standard version, and pass them on unchanged with the classification. Keep a record's descriptors even if your own system does not use them.
- Read each value with the definition of the version the record names. Records made under earlier versions are covered in [Records made under earlier versions](#records-made-under-earlier-versions).
- Descriptors are independent. Selecting one never requires another, and a record that omits a descriptor does not declare that it cannot apply. Examples show combinations that give further detail; they do not require every applicable descriptor to be recorded. Implementations must not add pairing rules, and a form or tool should accept any valid selection permitted for the classification.
- Where descriptors are shown to people, use the labels above and show them alongside the classification, never in place of it. HPF does not require descriptors to be displayed.

---

## Handling rules

- **HPF is producer self-declaration.** The classification is what an authorised party declared. Never derive one from software use, file metadata, automated detection, catalogue heuristics, release date, or the absence of a declaration.
- **Missing is never `no_ai`.** A missing, blank, invalid, unknown or unresolved value must not default to `no_ai`. Only a declaring party can state that no in-scope AI output is present.
- **Keep the two states apart.** "No AI Used" and "no valid HPF declaration received" are different facts. A schema, column, export format or interface that cannot hold both is not fit for HPF data.
- **Omit rather than pad.** The fields are required, so an HPF record with null or empty values is invalid. Where no declaration exists, write no HPF record.
- **Absence need not block ingest.** HPF does not require an organisation to block ingest or delivery solely because a declaration is absent. Proceed without writing an HPF record, and flag the absence for follow-up where that is useful. Whether to require a declaration is for the receiving organisation to decide.
- **The HPF record describes a named released version.** It describes AI output in that version, not AI use at every stage of production. An organisation that asks about other stages may need additional information, and asks for it under its own policy.
- **Flag, do not coerce.** An out-of-enum classification, a malformed version string, a missing version field, or a 0.9.3 or later record without its released version is invalid. Flag it for follow-up with the declaring party. Do not discard it silently or substitute a default.
- **Never bulk-apply.** A classification is not backfilled across a catalogue. Where an organisation produced the work itself it can declare as the producer; otherwise undeclared material has no HPF record.
- **Pass the fields together.** A classification without its Standard version and released version cannot be read back reliably. Store the version string exactly as received and treat it as an identifier, not a number to compare arithmetically.
- **Do not re-express the classification.** A record received as `assistive_ai` is stored and passed on as `assistive_ai`, and shown to people as Assistive AI. It is never converted to another category. Where a classification is shown to an audience it should relate to the version actually made available, using the labels in the table above, which are those in [taxonomy.md](taxonomy.md). HPF does not require audience display or prescribe its form.
- **Keep the namespace clean.** Record the fields the schema defines and nothing else. Prompts, model names, training-data claims, consent flags, rights status and approval outcomes are outside the Standard's scope, and putting them behind an HPF label misrepresents what HPF is.

Detection sits outside all of this. Content detection, forensic analysis and watermark or fingerprint matching are external processes with their own purposes and limits. None can create an HPF classification, correct one, or stand in for a declaration that was never made.

### What structural validation establishes

Schema validation checks data structure and permitted values. It does not establish whether the declaration is accurate, what AI was actually used, or whether the declaring person was authorised. It does not establish copyright, consent, rights, or compliance with contracts, collective agreements, policies, or law.

HPF does not audit, certify, approve, or determine eligibility. Do not present an integration as providing those services. An organisation may apply its own policies to HPF information, but those policies remain separate from the standard.

The schema does not reject properties it does not define. Passing validation therefore does not establish that a record follows every rule in this guide.

---

## The HPF record and the signed declaration

The signed declaration is the complete statement: the work, the released version it covers, the classification, the declaring party, the name and signature of the authorised person who signs it (the name is required for declarations made under 0.9.4 and later), the date, the assertion, and, where in-scope AI use is present, a short factual summary of what the AI did and what output reached the finished work. It may also record descriptors and a reference to supporting production records. The [HPF AI Disclosure Form](https://humanprovenance.film/disclosure-form/) records these, and any document carrying the same information works the same way.

The HPF record contains the classification, released version, standard version, and any declared descriptors. It contains only part of the signed declaration.

Retain the signed declaration, or a reliable reference to where it is held, alongside the HPF record. The declaration may be kept on paper or digitally; HPF requires no particular medium.

The signed declaration remains authoritative. If it differs from the HPF record, refer the discrepancy to the declaring party as a possible transcription or version error. Do not resolve it by changing either document yourself.

---

## Versions of the production

One declaration covers one released version of a work, and may travel with every delivery of that same version. A released version is a separately released editorial edition or substantive localisation of a work, identified by its picture, sound and, where relevant, embedded audience-facing text. A later released version has its own declaration, even where the classification and factual summary are unchanged. See [taxonomy.md](taxonomy.md).

For a system this means:

- Store the released version with the classification. A different codec, bitrate, container, delivery master or transcode of the same picture, sound and embedded text is the same released version and carries the same HPF record.
- A director's cut, a restored edition that changes the picture or sound, or a dubbed version is a different released version. Do not apply an existing HPF record to it; ask the declaring party for its declaration.
- A declaration for a later released version does not change the HPF record for an earlier one. Keep both. HPF does not require the producer to notify recipients of an earlier version, and a system should not wait for such a notice.
- A correction is not a later released version. A producer who finds an error in a declaration issues a corrected declaration for the same released version. HPF recommends that it carry its own date and name the declaration it replaces, so that a system can tell which is current; the standard does not yet require this, and what a recipient does with a superseded declaration is an open technical question below.

How the rule applies to episodic works, selectable subtitles and captions, dubbing and other localisation, and the boundary between a technical delivery variation and a substantively different released version is still open. These are questions about applying the rule, not about reconsidering it, and this note does not settle them.

---

## Optional carriage

Receiving and retaining a declaration needs no API, ledger, manifest or provenance infrastructure, and HPF mandates no database or delivery architecture. A signed declaration exists independently of the delivery file, so it is not lost through transcoding, format conversion or platform ingest. [schema.json](schema.json) exists so that an organisation already holding title records in a system can hold the classification in the same place and pass it in a metadata exchange. HPF prescribes no filename or packaging pattern for a structured record; any sidecar or manifest arrangement is for the sending and receiving parties to agree.

[c2pa-mapping.md](c2pa-mapping.md) proposes an entity-specific C2PA assertion carrying the same payload. It is a working proposal, has not been submitted to the C2PA Technical Working Group, has no signing authority behind it, and is not for production implementation. C2PA can carry an HPF classification. It does not decide, validate or correct one.

---

## Records made under earlier versions

Validate a record against the schema published with the version it names, which is in that release tag. That is a different question from whether the current schema accepts it.

| Version named | Version field | `hpf_released_version` | `hpf_descriptors` | Current schema accepts it |
|---|---|---|---|---|
| 0.9.0, 0.9.1 | `hpf_taxonomy_version`, with a two-part value such as `0.9` | Not defined | Not defined | No |
| 0.9.2 | `hpf_standard_version` | Not defined. The current schema permits it and does not require it. | Provisional vocabulary | Yes |
| 0.9.3 | `hpf_standard_version` | Required | Provisional vocabulary | Yes |
| 0.9.4 | `hpf_standard_version` | Required | Adopted vocabulary | Yes |

- Records that used the earlier version field validate against the schemas in the v0.9.0 and v0.9.1 tags and not against the current schema, which requires `hpf_standard_version`. That does not make them invalid. Keep them as received: do not rename the field, backfill missing fields or require migration.
- Do not reject or backfill a 0.9.2 record for lacking the released version.
- Records made under 0.9.2 or 0.9.3 may carry descriptors. The values and the classification restrictions have not changed since 0.9.2, so the current schema validates those records, and their descriptors are read with the provisional definitions of the version they name.
- Records that name 0.9, 0.9.0 or 0.9.1 cannot carry meaningful descriptors. Those versions defined no descriptors and no `hpf_descriptors` field. The schema has never rejected the field on such a record and still does not, so a record of this kind can pass validation while carrying values that the version it names does not define. Do not read those values with a later version's definitions. Keep the record as received and ask the declaring party which version it applied. A declaration that records descriptors names 0.9.2 or a later version.

This describes which older records the current schema accepts. It is not a general guarantee of compatibility across versions.

---

## Versions, compatibility and notice

A record is read under the version it names, so a new version of the Standard does not by itself make an existing record invalid or require it to be remade. Validate a record against the version it states. From v1.0, HPF intends to publish, with each release, what changed, who is affected, whether controlled values or validation changed, what stays compatible, and whether migration is needed. For a changed technical requirement HPF normally expects to allow at least three months between the final specification and expected implementation support, and longer for substantial changes. These are normal expectations, not mandatory deadlines, and no implementation is required to adopt the latest release. Tagged releases, schemas and release notes stay available, and an erratum to a published release is a separate dated note. HPF states which standard version each of its own tools is maintained against, and does not promise indefinite support for every historical version of any software. The full policy is in the [amendment process section of GOVERNANCE.md](GOVERNANCE.md#amendment-process).

---

## Technical implementation questions

The following technical questions remain open. They are separate from the classification questions in [taxonomy.md](taxonomy.md#consultation). This guide does not authorise an implementation choice merely because it leaves the question unanswered.

1. Who has signing authority for the proposed C2PA assertion.
2. What a recipient does with a superseded declaration.
3. Whether a controlled value should distinguish undeclared material from a declared `no_ai`.
4. Whether HPF should specify a sidecar filename and packaging pattern.

How the released-version rule applies to episodic works, selectable subtitles and captions, dubbing and other localisation is part of consultation question 4.

To contribute: open an issue or pull request on the repository, or email contact@humanprovenance.film.

---

## Related resources

| Document | What it is for |
|---|---|
| [taxonomy.md](taxonomy.md) | The Standard. Category definitions, the classification test, scope and edge cases. |
| [schema.json](schema.json) | The HPF record, its required fields and permitted values. |
| [examples/](examples/) | Records that must validate, and records that must fail. |
| [Add HPF to your workflow](https://humanprovenance.film/resources/add-hpf-to-your-workflow/) | What an organisation does without any integration. |
| [c2pa-mapping.md](c2pa-mapping.md) | The proposed C2PA assertion. A working proposal, not final and not part of C2PA. |
| [GOVERNANCE.md](GOVERNANCE.md) | The version history of the Standard and this note, and the amendment process. |

## Version history

Changes to this note are recorded in the version history in [GOVERNANCE.md](GOVERNANCE.md#version-history), with each release tag linked there.

---

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
