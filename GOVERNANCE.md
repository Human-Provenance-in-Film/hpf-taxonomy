# HPF taxonomy governance

**Version 0.9.3**
Originator and copyright holder: The Mise En Scène Company (MSC)

---

## Current status

This taxonomy was originated by MSC, which holds the copyright and has licensed it under CC BY 4.0. That licence is irrevocable, so what has been published stays published.

MSC owns the copyright in the taxonomy, licenses it under CC BY 4.0, and is the data controller for the website. HPF is the initiative itself, and is run as independently of MSC's commercial operations as is practicable. Where this document says HPF, it means the initiative and the people running it. Where it says MSC, it means the owner.

MSC is an international film sales agency and has a commercial interest in the subject matter of AI disclosure in screen content. This interest is stated so that readers can weigh it against the taxonomy and the consultation process.

MSC is committed to finding a neutral home for the standard, preferably an existing standards body and, failing that, an independent coalition or membership organisation governed independently of any one company, including MSC. As of the August 2026 update, MSC is assessing the organisational structure this would require; no legal form or permanent home has been selected.

v0.9 is currently open for public consultation. The consultation closes 31 October 2026. Responses should be submitted to contact@humanprovenance.film or via the GitHub repository.

The Pre-v1 Consultation Survey phase closed on 30 September 2026. Its questions on the definitions and the provisional descriptors remain open as the descriptor survey until 31 October 2026. HPF is also beginning to identify a small pre-v1 working group to pressure-test the taxonomy, descriptors, and implementation against real production and institutional use cases. The working group is advisory. It is not the future governing body, and participation does not imply endorsement of HPF.

---

## Amendment process

This process applies once v1.0 is published. While v0.9 is open for consultation, the draft is revised directly in response to feedback, including changes to the organising principle, the categories, and the classification test, with each revision recorded in the version history.

From v1.0:

**Minor amendments** (typos, clarifications, additional examples that do not change how productions are classified) can be made by HPF without a consultation period. They are noted in the version history.

**Substantive amendments** (changes to category definitions, the organising principle, or the classification test) require a minimum 30-day consultation period. HPF will notify those who have registered interest before any substantive amendment takes effect.

To propose an amendment at any time: email contact@humanprovenance.film, or open an issue or pull request on the GitHub repository. HPF will acknowledge within 5 working days.

---

## Version history

This is the single public record of what each revision of the standard changed. The history of `INTEGRATION.md`, `c2pa-mapping.md` and the taxonomy page on the website is recorded here too.

A published release tag is an immutable snapshot. Each tag records the documents exactly as they stood when that revision was released, and it is never moved, overwritten or recreated; the link under each entry leads to it. While v0.9 is open for consultation, editorial corrections and clarifications may be made to the working draft between tags, and they are listed, dated, under the revision that will carry them. A change that alters normative meaning, classification rules, permitted values, schema behaviour or a substantive requirement needs a new version.

Every v0.9 revision is a draft for consultation. Items marked **Consultation revision** change what someone applying HPF does. They are the current rules of the revision that introduces them and, like all pre-v1 provisions, remain subject to evidence received during consultation; they are not settled v1 policy. The questions under consultation are in [taxonomy.md](taxonomy.md#consultation) and are not restated here.

### 0.9.3 · October 2026 · Draft for consultation

Clarifies that one signed declaration covers one released version of a work, and that later released editorial editions or substantive localisations receive their own declaration, including where the disclosed facts are unchanged. Removes the former requirement to notify all earlier recipients of a later declaration. Clarifies that descriptors may be combined where each adds factual information. Updates supporting guidance and the Policy Mapper output without changing HPF's core categories.

**Taxonomy and declarations**

- **Consultation revision.** One declaration covers one released version of a work and may travel with every delivery of that version. A released version is a separately released editorial edition or substantive localisation. A later released version has its own signed declaration, which may repeat unchanged facts.
- **Consultation revision.** A declaration for a later released version does not change the record for an earlier one. HPF does not require retrospective notification to recipients of an earlier version. This replaces the 0.9.2 edge-case rule for re-edits and director's cuts.
- **Consultation revision.** More than one descriptor may apply to the same production, with no limit, ranking or rule against overlap. The worked example of Digital replica, Generated voice and Altered performance now says what each adds.
- The schema adds `hpf_released_version`, required on a 0.9.3 record. A record made under 0.9.2 does not carry it and stays valid under the version it names.
- Consultation questions consolidated. v0.9.3 establishes the current consultation-draft rules for released versions and descriptor combinations. Like all pre-v1 provisions, they remain subject to evidence received during consultation, but are not listed as unresolved questions. The same applies to the absence of a percentage threshold. Contracts, consent, compensation, rights and legal compliance are outside HPF and are not consultation questions, and the design of audience-facing labels and display formats is a separate implementation matter. Five areas remain open: reasonable enquiry and established machine learning, asked in two parts (whether reasonable enquiry is the appropriate basis for a No AI Used declaration, and which established machine-learning functions, if any, should require Assistive AI disclosure); performance-related descriptors; human contribution to synthetic performance; complex finished-work and version cases, including intermediate VFX control data, which is not settled; and implementation. Examples of real production use that does not fit the current categories are invited.
- Where the 0.9.2 consultation questions now sit: 1, on the categories, is replaced by the invitation to send examples that do not fit them; 2 is questions 1 and 5; 3, on marketing materials, is no longer asked, because HPF's scope is the finished production; 4 is question 5, without its audience-display part; 5, on display formats, is no longer a taxonomy question; 6 is question 5, without its part on contractual and collective-bargaining frameworks; 7, on established machine-learning features, is part of question 1; 8, on a measure of extent, is answered by the current rule that HPF uses no percentage threshold. The wording as asked is in the v0.9.2 tag.
- The glossary entries for warranted declaration, chain of title, clearance and E&O insurance are removed. They defined legal and commercial terms that HPF does not use as its own.
- Wording revised: "leaving no trace" becomes the finished-work record; development-only AI is outside that record rather than "not requiring classification"; "paper declaration" becomes signed producer declaration; the comparison of descriptors with film ratings is removed; the scope section's legal and insurance notes become one statement that those questions remain outside HPF; references to a chain-of-title route become existing deal, delivery and other production paperwork.
- 1 September 2026: the basis-of-reliance wording and the implementation warning in the proposed C2PA mapping were clarified.
- No AI Used is clarified as applying to the named released version: AI may have been used in development or elsewhere in the workflow without its output being incorporated into that version. The classification describes the finished version, not the whole production process, how the work was staffed or its rights position.
- Unchanged: the three categories, the two questions of the organising principle, the highest-category rule, the reconstruction test, the absence of a threshold and the descriptor values.

**Guidance**

- Filmmaker guidance says when a later released version needs its own declaration and when a technical delivery change does not.
- Filmmaker guidance adds When output reaches the finished version: process-only use is outside the declaration, human editing does not by itself take AI-originated material out of scope, and there is no percentage threshold for transformation. Four paired examples, from workflow use to finished-work record, illustrate the current approach without resolving every transformed or hybrid case.
- When gathering the facts, producers are prompted to ask departments and vendors whether temporary, reference-only or replaced AI material remained in the released version. No log, inventory or vendor certification is required.
- Guidance on No AI Used carries reasonable enquiry as an open consultation question only.
- Filmmaker guidance adds that output need not stay in its original file format or appear as a standalone asset to contribute to the released version, with a dialogue example: discarded, outside the declaration; retained and performed, carried into the finished work; substantially rewritten before performance, an open case. The guide distinguishes processing or reconstruction from fabrication and names the cases that remain under consultation. Example factual use summaries sit beside the declaration instructions; they are not templates.
- Guidance for organisations says that an HPF declaration describes AI output in a named released version, so an organisation asking about other stages of production may need additional information. The integration note again says that HPF does not require ingest to be blocked solely because a declaration is absent.
- Enquiry guidance asks about the material that may have reached the version being declared, not for a production-wide tool inventory. Suppliers provide facts about their own deliverables; the producer classifies and signs.
- Guidance for receiving organisations no longer tells sales agencies or buyers what to include or request. Each organisation decides whether to request a declaration, how to keep it and what policy to apply.
- The integration note is now a short note on the machine-readable record, marked as informative guidance; the workflow narrative it carried is in the guide for organisations. It says the core fields may be tested in integration during consultation and the descriptor array is not for production implementation.
- The version histories of the integration note, the C2PA mapping and the website's taxonomy page now point to this one. Their entries are summarised under each revision here, and their text as released is in the tags.
- The statement of MSC's interest in this document no longer refers to pricing. The README's description of what disclosure makes possible is narrower.
- 10 September 2026: the HPF AI Disclosure Form gained an optional continuation sheet, on-screen completion with a draft kept only in the visitor's browser, and a fillable PDF alongside. The declaration information set did not change.
- 30 September 2026: the form names the released version it covers, and its signature statement no longer refers to reasonable enquiry.
- 1 October 2026, editorial: the taxonomy, its web page, How It Works and the FAQ were shortened and repeated explanation consolidated, without changing a rule, a controlled value or an open question. The Assistive AI examples, the reconstruction test and the worked examples no longer present denoising, upscaling, tracking or automated subtitles and captions as settled, and point to questions 1 and 4 instead. The development-only and live-action edge cases are folded into Scope and the category definitions, with their examples in the filmmaker guidance. HPF is described as production disclosure for transparency to audiences rather than as commercial disclosure. Glossary entries are shortened, with C2PA detail moved to the C2PA mapping.
- 1 October 2026, corrections: a restored edition is classified on all in-scope AI output it contains, including output retained from the original version, with AI processing of supplied footage an Assistive use; content AI originates is Generative AI even where human-created material was the input; the declaration's factual summary is described as concise rather than as an account of every use; the combined-performance descriptor example now describes AI-generated speech inserted into captured footage; and the glossary entries for technical provenance and C2PA were made more precise.
- 1 October 2026, editorial: Relationship to regulation is shortened to a statement that an HPF declaration does not establish legal compliance or replace obligations under applicable law; the explanation of Article 50(2) and 50(4) of the EU AI Act is removed from the taxonomy. The training-data statement moves into Scope. Neither change alters a rule or a controlled value.
- 1 October 2026, wording: the organising principle is two questions; marketing or distribution materials are outside scope unless their AI output is also incorporated into the finished film or programme; AI processing of animators' work is Assistive AI subject to the open questions on established machine-learning functions; an absent declaration establishes neither that AI was used nor that it was not; the Altered performance definition is one sentence. On the web page, the section 5 decision block applies the highest applicable category and does not force a classification for unknown facts or open questions. No rule, category, descriptor meaning or consultation question changed.

**Tools**

- Policy Mapper rules 0.1.1, replacing 0.1.0. A tool rules update, not a category change: it cites the taxonomy as 0.9.3, uses the released-version wording, no longer states reasonable enquiry as a producer obligation, and says in its output that it maps stated policies to HPF concepts and does not determine legal compliance, consent, contractual permission or verification.
- AI Use Checker parser 1.11.1, citing standard 0.9.3. Where AI-generated or AI-segmented mattes, masks, selected regions or similar control data shape the delivered picture and nothing else decides the category, the Checker returns an unresolved result that names this as an open consultation question, instead of Assistive AI or Generative AI. It decides this from what the description says the output did. Segmentation used only for logging, a matte replaced by hand before delivery and AI colour grading applied to the picture keep their results, and the classification test is otherwise unchanged. Generated dialogue that was substantially rewritten before it was performed also returns the unresolved result where the description does not establish what survived; dialogue retained and performed stays Generative AI, and discarded suggestions have no effect. Line art cleaned up by AI reads as animation rather than dialogue, and AI-made marketing or distribution material that the description says is not in the film does not affect the classification.

Text as released: [tag v0.9.3](https://github.com/human-provenance-in-film/hpf-taxonomy/tree/v0.9.3), 2 October 2026.

### 0.9.2 · August 2026 · Draft for consultation

Added provisional descriptors and a glossary for consultation, renamed the version field, and set out what a declaration identifies.

**Taxonomy and declarations**

- Renamed the machine-readable version field from `hpf_taxonomy_version` to `hpf_standard_version`. A record using the old name was made under an earlier draft.
- **Consultation revision.** Added the provisional descriptors. `altered_performance` may be used on an Assistive AI or a Generative AI production; `synthetic_performance` covers generated performance that does not represent an identifiable person; no descriptor applies to No AI Used. Descriptors are factual provenance terms, take no meaning from any collective agreement, and state nothing about consent, rights, contractual requirements or compliance.
- Added the glossary for consultation.
- Scope turns on AI output reflected in the finished production, and a classification is unresolved where information is missing or uncertain.
- The definition of artificial intelligence moved into Key terms. Where a tool both reconstructs supplied material and fabricates content that was never captured, the fabrication decides the category.
- Set out what a declaration identifies, including a short factual summary of what the AI did. Tool names are supporting information and do not replace it.
- An authorised party may declare for a production already released where it can establish the facts. Inferring or bulk-applying a classification is not permitted.
- The standard classifies the finished production, not the parties to it. Contributors disclose what AI they used and what output reached the finished production; the producer applies the standard and signs.
- An HPF declaration is not by itself a contractual warranty. HPF encourages audience display without requiring it.
- Provider marking under Article 50(2) of the EU AI Act distinguished from deployer disclosure under Article 50(4). HPF described as a proposed voluntary industry standard.
- Added consultation question 8, on leaving out an objective measure of extent.
- Unchanged: categories, organising principle, definitions, machine values and scope boundaries.

**Guidance**

- The proposed C2PA mapping took the label `film.humanprovenance.ai-disclosure` and records that it is not part of C2PA and has not been reviewed or endorsed by it. The integration note recorded the proposed descriptor field.

Text as released: [tag v0.9.2](https://github.com/human-provenance-in-film/hpf-taxonomy/tree/v0.9.2), 28 August 2026.

### 0.9.1 · June 2026 · Draft for consultation

Reframed the organising principle from enhance-or-replace to present-and-originated, with the three categories unchanged.

**Taxonomy and declarations**

- Organising principle reframed from enhance-or-replace to present-and-originated. Categories unchanged.
- Reconstruction test added for AI tools that act on existing footage.
- Tier renamed to category throughout.
- Consultation questions added, and the consultation close set to 31 October 2026.

**Governance**

- Governance reframed to register-interest.

Text as released: [tag v0.9.1](https://github.com/human-provenance-in-film/hpf-taxonomy/tree/v0.9.1). 0.9.0 and 0.9.1 were both released under the single tag `v0.9.0` on 22 June 2026, because the repository was tagged once; `v0.9.1` was added later at the same commit. The June revision was numbered 0.9.1 on 27 August 2026 because it was substantive.

### 0.9.0 · May 2026 · Draft for consultation

Initial release.

Text as released: [tag v0.9.0](https://github.com/human-provenance-in-film/hpf-taxonomy/tree/v0.9.0).

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
