# HPF integration guide

**HPF Guidance for the HPF AI Disclosure Standard v0.9.3.** Informative.
Updated October 2026. Consultation closes 31 October 2026.

This note covers one thing: the machine-readable HPF record, and the rules that keep it honest. [taxonomy.md](taxonomy.md) and [schema.json](schema.json) are authoritative for the classifications, definitions, permitted values and required fields, and they govern where this note and they disagree. Nothing here is a commitment that the current fields, permitted values or carriage options will be unchanged at v1.0.

**Technical integration is optional.** An organisation can collect and use HPF declarations with no software change at all: ask for a declaration, keep it with the record it belongs to, and apply its own policy. [Add HPF to your workflow](https://humanprovenance.film/resources/add-hpf-to-your-workflow/) is the guide for that route, and it is the right starting point for a fund, festival, awards body, commissioner, broadcaster, distributor or platform. Read this note only if you are holding HPF information in a system.

---

## The record

A record made under 0.9.3 has three required fields:

```json
{
  "hpf_standard_version": "0.9.3",
  "hpf_released_version": "Theatrical cut",
  "hpf_classification": "assistive_ai"
}
```

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

`hpf_standard_version` is a string in the form `MAJOR.MINOR` or `MAJOR.MINOR.PATCH`, naming the version of the Standard that was applied. `hpf_released_version` identifies the released version the declaration covers, in the declaration's own words; HPF prescribes no identifier scheme. It was added in 0.9.3. A record made under 0.9.2 carries the standard version and the classification only, and stays valid under the version it names: validate a record against the version it states, and do not reject or backfill a 0.9.2 record for lacking the released version. Treat [schema.json](schema.json) as the source for every field, not this note. Records that must validate, and records that must fail, are in [examples/](examples/).

A production carries one classification, at the highest applicable category, for the released version the declaration covers. There is no threshold and no de minimis exception. [taxonomy.md](taxonomy.md) has the classification test.

The required fields may be tested in integration during consultation. Implementers should retain the HPF standard version used and should not treat the provisional descriptor array as stable for production implementation.

> **`hpf_descriptors` is proposed and provisional.** The descriptor array in [schema.json](schema.json) is under consultation and its values may change before v1.0. Do not build a production integration against it. More than one descriptor may apply to the same production; [taxonomy.md](taxonomy.md) sets out how they combine. Retain descriptors that arrive on a record rather than dropping them, and treat them as factual context: a descriptor never determines or changes the classification.

---

## The record is not the declaration

The declaration is the complete signed statement: the work, the released version it covers, the classification, the declaring party, the date, the assertion and signature, and, where in-scope AI use is present, a short factual summary of what the AI did and what output reached the finished work. The [HPF AI Disclosure Form](https://humanprovenance.film/disclosure-form/) records these, and any document carrying the same information works the same way.

The record carries the classification, the released version and the Standard version through a system. They carry none of the rest, and cannot be read as though they did. Retain the declaration, or a reliable reference to where it is held, alongside the record. It may be kept in any documentary or electronic form; HPF requires no particular medium: the declaration may be on paper or digital. The authoritative source is the signed producer declaration, and a stored record carries only part of it. Treat a discrepancy between them as a transcription or version problem for the declaring party, not something to resolve by changing either one.

---

## Rules

- **HPF is producer self-declaration.** The classification is what an authorised party declared. Never derive one from software use, file metadata, automated detection, catalogue heuristics, release date, or the absence of a declaration.
- **Missing is never `no_ai`.** A missing, blank, invalid, unknown or unresolved value must not default to `no_ai`. Only a declaring party can state that no in-scope AI output is present.
- **Keep the two states apart.** "No AI Used" and "no valid HPF declaration received" are different facts. A schema, column, export format or interface that cannot hold both is not fit for HPF data.
- **Omit rather than pad.** The fields are required, so a record with null or empty values is invalid. Where no declaration exists, write no record.
- **Absence need not block ingest.** HPF does not require an organisation to block ingest or delivery solely because a declaration is absent. Proceed without writing a record, and flag the absence for follow-up where that is useful. Whether to require a declaration is for the receiving organisation to decide.
- **The record describes a named released version.** It describes AI output in that version, not AI use at every stage of production. An organisation that asks about other stages may need additional information, and asks for it under its own policy.
- **Flag, do not coerce.** An out-of-enum classification, a malformed version string, a missing version field, or a 0.9.3 record without its released version is invalid. Flag it for follow-up with the declaring party. Do not discard it silently or substitute a default.
- **Never bulk-apply.** A classification is not backfilled across a catalogue. Where an organisation produced the work itself it can declare as the producer; otherwise undeclared material has no record.
- **Pass the fields together.** A classification without its Standard version and released version cannot be read back reliably. Store the version string exactly as received and treat it as an identifier, not a number to compare arithmetically.
- **Do not re-express the classification.** A record received as `assistive_ai` is stored, passed on and displayed as `assistive_ai`. Where a classification is shown to an audience it should relate to the version actually made available, using the labels in [taxonomy.md](taxonomy.md). HPF does not require audience display or prescribe its form.
- **Keep the namespace clean.** Record the fields the schema defines and nothing else. Prompts, model names, training-data claims, consent flags, rights status and approval outcomes are outside the Standard's scope, and putting them behind an HPF label misrepresents what HPF is.

Detection sits outside all of this. Content detection, forensic analysis and watermark or fingerprint matching are external processes with their own purposes and limits. None can create an HPF classification, correct one, or stand in for a declaration that was never made.

---

## What structural validation establishes

That the data has the expected structure and uses permitted values. Nothing else. It says nothing about the accuracy of the declaration, the AI actually used in the production, the authority of the person who made the declaration, copyright, consent, rights, or compliance with any contract, collective agreement, policy or law. HPF does not audit, certify, approve or determine eligibility, and an integration must not be presented as though it does. An organisation may apply its own rules to declared HPF information; those rules are the organisation's and are not part of HPF.

---

## Versions of the production

One declaration covers one released version of a work, and may travel with every delivery of that same version. A released version is a separately released editorial edition or substantive localisation of a work, identified by its picture, sound and, where relevant, embedded audience-facing text. A later released version has its own declaration, even where the classification and factual summary are unchanged. See [taxonomy.md](taxonomy.md).

For a system this means:

- Store the released version with the classification. A different codec, bitrate, container, delivery master or transcode of the same picture, sound and embedded text is the same released version and carries the same record.
- A director's cut, a restored edition that changes the picture or sound, or a dubbed version is a different released version. Do not apply an existing record to it; ask the declaring party for its declaration.
- A declaration for a later released version does not change the record for an earlier one. Keep both. HPF does not require the producer to notify recipients of an earlier version, and a system should not wait for such a notice.

How the rule applies to episodic works, selectable subtitles and captions, dubbing and other localisation, and the boundary between a technical delivery variation and a substantively different released version is open for consultation. These are questions about applying the rule, not about reconsidering it, and this note does not settle them.

---

## Optional carriage

Receiving and retaining a declaration needs no API, ledger, manifest or provenance infrastructure, and HPF mandates no database or delivery architecture. A signed declaration exists independently of the delivery file, so it is not lost through transcoding, format conversion or platform ingest. [schema.json](schema.json) exists so that an organisation already holding title records in a system can hold the classification in the same place and pass it in a metadata exchange. HPF prescribes no filename or packaging pattern for a structured record; any sidecar or manifest arrangement is for the sending and receiving parties to agree.

[c2pa-mapping.md](c2pa-mapping.md) proposes an entity-specific C2PA assertion carrying the same payload. It is a working proposal, has not been submitted to the C2PA Technical Working Group, has no signing authority behind it, and is not for production implementation. C2PA can carry an HPF classification. It does not decide, validate or correct one.

---

## Technical implementation questions

These are technical matters for implementers, separate from the consultation questions in [taxonomy.md](taxonomy.md#consultation). They are recorded so that silence is not read as permission, and this note does not settle them:

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
| [schema.json](schema.json) | The record, its required fields and permitted values. |
| [examples/](examples/) | Records that must validate, and records that must fail. |
| [Add HPF to your workflow](https://humanprovenance.film/resources/add-hpf-to-your-workflow/) | What an organisation does without any integration. |
| [c2pa-mapping.md](c2pa-mapping.md) | The proposed C2PA assertion. A working proposal, not final and not part of C2PA. |
| [GOVERNANCE.md](GOVERNANCE.md) | The version history of the Standard and this note, and the amendment process. |

---

## Version history

Changes to this note are recorded in the version history in [GOVERNANCE.md](GOVERNANCE.md#version-history), with each release tag linked there.

---

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
