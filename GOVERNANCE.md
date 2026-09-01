# HPF taxonomy governance

**Version 0.9.2**
Originator and copyright holder: The Mise En Scène Company (MSC)

---

## Current status

This taxonomy was originated by MSC, which holds the copyright and has licensed it under CC BY 4.0. That licence is irrevocable, so what has been published stays published.

MSC owns the copyright in the taxonomy, licenses it under CC BY 4.0, and is the data controller for the website. HPF is the initiative itself, and is run as independently of MSC's commercial operations as is practicable. Where this document says HPF, it means the initiative and the people running it. Where it says MSC, it means the owner.

MSC is an international film sales agency and has a commercial interest in the outcome. A widely adopted disclosure standard would give the market a consistent way to tell whether generative AI is present in a finished production, and MSC expects that to bring more pricing clarity to films that do not contain it. Whether human-authored work commands a premium is an open question, and HPF does not claim to have answered it. The interest is stated here so that a reader can weigh it against what the taxonomy says.

MSC is committed to finding a neutral home for the standard, preferably an existing standards body and, failing that, an independent coalition or membership organisation governed independently of any one company, including MSC. As of the August 2026 update, MSC is assessing the organisational structure this would require; no legal form or permanent home has been selected.

v0.9 is currently open for public consultation. The consultation closes 31 October 2026. Responses should be submitted to contact@humanprovenance.film or via the GitHub repository.

A short Pre-v1 Consultation Survey is open until 30 September 2026, ahead of the wider consultation. HPF is also beginning to identify a small pre-v1 working group to pressure-test the taxonomy, descriptors, and implementation against real production and institutional use cases. The working group is advisory. It is not the future governing body, and participation does not imply endorsement of HPF.

---

## Amendment process

This process applies once v1.0 is published. While v0.9 is open for consultation, the draft is revised directly in response to feedback, including changes to the organising principle, the categories, and the classification test, with each revision recorded in the version history.

From v1.0:

**Minor amendments** (typos, clarifications, additional examples that do not change how productions are classified) can be made by HPF without a consultation period. They are noted in the version history.

**Substantive amendments** (changes to category definitions, the organising principle, or the classification test) require a minimum 30-day consultation period. HPF will notify those who have registered interest before any substantive amendment takes effect.

To propose an amendment at any time: email contact@humanprovenance.film, or open an issue or pull request on the GitHub repository. HPF will acknowledge within 5 working days.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| 0.9.0 | May 2026 | Initial release. Draft for consultation. |
| 0.9.1 | June 2026 | Organising principle reframed from enhance-or-replace to present-and-originated (categories unchanged). Tier renamed to category throughout. Consultation date set to 31 October 2026. Governance reframed to register-interest. Consultation questions added. Reconstruction test added for AI tools that act on existing footage. |
| 0.9.2 | August 2026 | Renamed the machine-readable version field from `hpf_taxonomy_version` to `hpf_standard_version`; a record using the old name is a record made under the earlier draft. Added the provisional descriptors and the glossary for consultation, and refined them: `altered_performance` records that AI modified a performance by an identifiable person and may be used on an Assistive AI or a Generative AI production, `synthetic_performance` was narrowed to generated performance content that does not represent an identifiable person, and no descriptor applies to No AI Used. Descriptors are factual provenance terms, take no meaning from any collective agreement, and state nothing about consent, rights, contractual requirements or compliance. Clarified that scope turns on AI output reflected in the finished production, and that a classification is unresolved where information is missing or uncertain. Moved the definition of artificial intelligence into Key terms so one boundary decides what counts as AI. Recorded that where a tool both reconstructs supplied material and fabricates content that was never captured, the fabrication decides the category. Set out what a declaration identifies, including a short factual summary of what the AI did; tool names are supporting information and do not replace it. Corrected the description of C2PA, replaced the assertion label `hpf.film.ai_disclosure` with `film.humanprovenance.ai-disclosure`, and recorded that the HPF mapping is not part of C2PA and has not been reviewed or endorsed by it. Distinguished provider marking under Article 50(2) of the EU AI Act from deployer disclosure under Article 50(4), and replaced "market standard" with "proposed voluntary industry standard". Corrected the claim that a false declaration is automatically covered by existing contracts: an HPF declaration is not by itself a contractual warranty. Replaced the statement that HPF provides no mechanism for retroactive disclosure: an authorised party may declare for a production already released where it can establish the facts, while inferring or bulk-applying a classification stays prohibited. HPF encourages audience display without requiring it. Added an eighth consultation question, on leaving out an objective measure of extent. Corrected the co-production framing: the standard classifies the finished production, not the parties to it, so the scope bullet no longer aggregates co-producers and contractors and the sentence about co-production structures obscuring AI use is removed. Contributors disclose what AI they used and what output reached the finished production; the producer applies the standard and signs. The descriptor disclaimer no longer names any organisation or collective agreement, and now covers every descriptor rather than Synthetic performance alone. Categories, organising principle, definitions, machine values and scope boundaries unchanged. |

0.9.0 and 0.9.1 were both released under the single tag `v0.9.0` on 22 June 2026, because the repository was tagged once. `v0.9.1` was added later at the same commit so the tag series matches this table. Renumbered on 27 August 2026: the June revision was substantive and should have carried its own number at the time.

---

## Editorial corrections during consultation

A published release tag is an immutable snapshot. `v0.9.0` and `v0.9.2` record the documents exactly as they stood when each revision was released, and a tag is never moved, overwritten or recreated. While v0.9 is open for consultation, non-semantic editorial corrections and clarifications may be made to the current working draft without opening a new version, and they are recorded here. A change that alters normative meaning, classification rules, permitted values, schema behaviour or a substantive requirement is not an editorial correction and requires version consideration.

**1 September 2026, v0.9.2 working draft.** Clarified the basis-of-reliance wording and the implementation warning for the proposed C2PA mapping. These changes do not alter HPF classifications, decision rules, permitted values or schema behaviour.

---

## Handoff

MSC is committed to seeking a governance transfer to an appropriate body. An appropriate body would be an established film or creative-industry standards organisation or regulatory body with the capacity to maintain and develop the standard on an ongoing basis, or, failing that, an independent coalition or membership organisation governed independently of any one company. Upon transfer, the originating repository will be archived with a redirect, and the CC BY 4.0 licence will continue to apply to all versions published under MSC's stewardship.

In the event HPF can no longer be maintained before a governance transfer is achieved, the most recent published version will remain available under CC BY 4.0. Any organisation may fork and maintain the standard under that licence. HPF will make reasonable efforts to notify those who have registered interest and the GitHub repository community before any such discontinuation.

The conditions a successor would have to meet, and the questions about a future structure that are deliberately still open, are set out in [docs/hpf-organisational-continuity.md](docs/hpf-organisational-continuity.md). The records a successor would need are indexed in [docs/hpf-handover-checklist.md](docs/hpf-handover-checklist.md). Neither changes the amendment process or the version history above, which remain authoritative.

---

## Registered interest

Organisations and individuals can register interest at [humanprovenance.film](https://humanprovenance.film) to be notified when v1.0 of the standard is published.

---

## Patent non-assertion

MSC makes no claim of patent or proprietary right over the taxonomy methodology in this repository and will not assert any such claim against organisations that implement it.
