# HPF taxonomy governance

**Version 0.9.4**
Originator and copyright holder: The Mise En Scène Company (MSC)

---

## Current status

This taxonomy was originated by MSC, which holds the copyright and has licensed it under CC BY 4.0. That licence is irrevocable, so what has been published stays published.

MSC owns the copyright in the taxonomy, licenses it under CC BY 4.0, and is the data controller for the website. HPF is the initiative itself, and is run as independently of MSC's commercial operations as is practicable. Where this document says HPF, it means the initiative and the people running it. Where it says MSC, it means the owner.

MSC is an international film sales agency and has a commercial interest in the subject matter of AI disclosure in screen content. This interest is stated so that readers can weigh it against the taxonomy and the consultation process.

MSC is committed to finding a neutral home for the standard, preferably an existing standards body and, failing that, an independent coalition or membership organisation governed independently of any one company, including MSC. As of the August 2026 update, MSC is assessing the organisational structure this would require; no legal form or permanent home has been selected.

The public consultation on v0.9 closed on 31 October 2026, and the descriptor survey closed with it. Feedback on the standard remains welcome from individual practitioners and from trade associations, unions and guilds, festivals, awards bodies, commissioners, funders, and other industry organisations. Companies in the screen industries that are considering adopting HPF are welcome to send technical and implementation feedback. Send feedback to contact@humanprovenance.film or via the GitHub repository.

Separately from the consultation, pre-v1 working groups are testing the classifications, descriptors, and declaration form against production and institutional cases. Current participation details are on the [HPF website](https://humanprovenance.film/taxonomy#working-groups). The working groups are advisory. They are not the future governing body, and participation does not imply endorsement of HPF.

**Current revision: 0.9.4, released 2 November 2026.** The three categories, the organising principle and the highest-category rule are unchanged from 0.9.3. Descriptors are adopted as optional vocabulary, and an HPF record may carry them under the rules in the taxonomy. A declaration made under 0.9.4 includes the signer's name. Records made under earlier versions stay valid under the version they name. The full entry is in the [version history](#version-history).

---

## Amendment process

This section describes how HPF intends to maintain the standard after v1.0. It is a future process, adopted in the 0.9.4 draft, and does not mean v1.0 has been published. Until v1.0, the draft is revised directly in response to feedback and testing, including changes to the organising principle, the categories, and the classification test, with each revision recorded in the version history. The process below does not apply to that period.

### Who maintains the standard

MSC owns the copyright. HPF operates the standard and holds decision authority over it, under the arrangements described in [docs/hpf-organisational-continuity.md](docs/hpf-organisational-continuity.md). This policy creates no committee, voting system, independent host, membership model, or funding arrangement. If the standard moves to a neutral home, as described under Handoff, that body will publish its own process and this section will be revised in a recorded change.

### Review cadence

HPF will normally review substantive amendment proposals once a year. An annual review does not require a new release, and HPF will not publish a release in a year in which no change is needed.

HPF plans an initial implementation review about six months after v1.0. Its purpose is to assess how the standard has been used, identify problems, and decide whether changes are needed. It does not commit HPF to publishing v1.1.

Editorial corrections and guidance can be issued between reviews. HPF does not promise a fixed schedule for either.

### Proposals and decisions

Anyone can propose a change by opening an issue or pull request in the GitHub repository. Confidential feedback can be sent to contact@humanprovenance.film. HPF will not publish confidential contributions, or production information they contain, without permission, and will use anonymised summaries where a decision needs one. HPF does not promise a response time or an implementation date for every submission.

HPF will keep a public record of amendment decisions and the reasons for them. Each decision falls into one of four groups:

- Accepted for a future release.
- Addressed through guidance or examples.
- Deferred until there is further evidence.
- Declined, with reasons.

For a substantive amendment the record will also explain how comments received during consultation informed the decision. HPF will not treat the absence of objections as consensus.

### Types of change

**Editorial corrections** fix spelling, formatting, broken links, and similar matters without changing meaning. HPF can make them without consultation and records them in the version history.

**Guidance and examples** explain existing requirements. HPF can publish them between reviews. They cannot add a requirement, and they are read together with the specification they explain. Guidance or an example that changes what someone applying HPF must do, or how a case is classified, is a substantive amendment and follows the process for one.

**Substantive amendments** change classification, descriptor meaning, scope, declaration requirements, controlled values, or validation. A change is substantive if it changes an answer or an obligation, even where it is made in an example, a FAQ, a form, or a tool and not in the taxonomy. A substantive change needs a new version.

**Urgent corrections** address a serious contradiction or defect. The announcement will explain the defect, the versions it affects, the consequences, and any action users need to take. HPF will record why it used an exceptional timetable instead of the normal one.

### Consultation and implementation notice

For a normal substantive amendment, HPF expects to publish a concrete proposal and invite comments for six to eight weeks. HPF will notify those who have registered interest.

Where a technical requirement changes, HPF normally expects to allow at least three months between publishing the final specification and expecting implementations to support it, and longer for substantial changes. These are normal expectations, not mandatory deadlines. HPF does not set an industry-wide implementation date, and no organisation is required to adopt the latest release. Documented exceptions apply to urgent corrections.

### Published releases and compatibility

HPF keeps tagged releases, versioned specifications, schemas, and release notes available. A tag is never moved, overwritten, or recreated, and historical requirements are not rewritten. If a published release needs an erratum, HPF will publish it as a separate, dated note linked to that release, so that the original text stays as it was released.

Version strings follow the form already used in `hpf_standard_version`, `MAJOR.MINOR` or `MAJOR.MINOR.PATCH`, and are treated as identifiers. This policy gives the numbers no additional meaning. The release notes for each version state what the change means in practice.

The notes for every new release explain:

- What changed and why.
- Which users and implementations are affected.
- Whether controlled values or validation changed.
- What remains compatible.
- Whether migration or other action is needed.

A new version of the standard does not, by itself, require a producer to remake an existing declaration. A record is read under the version it names. That does not protect an inaccurate declaration. A producer who finds that a declaration states facts wrongly can correct it, and HPF recommends doing so for the same released version, as set out in the taxonomy under Correcting a declaration. That remains recommended practice. This section adds no mandatory correction process. A declaration for a different released version is a separate declaration under the released-version rule, whatever the standard version. A documented defect in a release may also call for specific action, which the notice for that defect will state.

### Coordinated releases

Before announcing a substantive revision, HPF checks that the taxonomy, schema, developer specification, examples, forms, tools, and current guidance agree. The release checklist in [docs/release-checklist.md](docs/release-checklist.md) records that check.

HPF states separately which standard version each of its own tools is maintained against. It does not promise to support every historical version of any software indefinitely.

### Limits

Maintenance does not change what HPF is. HPF remains a free, open disclosure standard under CC BY 4.0. It is not a certification scheme, a verification service, a rights registry, or a compliance service, and it does not adopt legal or technological changes automatically or commission research as part of this process.

---

## Version history

This is the single public record of what each revision of the standard changed. The history of `INTEGRATION.md`, `c2pa-mapping.md` and the taxonomy page on the website is recorded here too.

A published release tag is an immutable snapshot. Each tag records the documents exactly as they stood when that revision was released, and it is never moved, overwritten or recreated; the link under each entry leads to it. Until v1.0, editorial corrections and clarifications may be made to the working draft between tags. They are listed, dated, under Editorial corrections to the working draft, below, and not inside a released entry. Listing a correction there does not open a new version or announce a release. A change that alters normative meaning, classification rules, permitted values, schema behaviour or a substantive requirement needs a new version.

Revisions released while the public consultation was open, 0.9.0 to 0.9.3, are drafts for consultation; 0.9.4 is a pre-v1 draft. Items marked **Consultation revision** change what someone applying HPF does. They are the current rules of the revision that introduces them and, like all pre-v1 provisions, remain subject to evidence received during consultation; they are not settled v1 policy. The questions under consultation are in [taxonomy.md](taxonomy.md#consultation) and are not restated here.

### Versions and releases

| Term | Meaning | Example |
|---|---|---|
| Standard version | The version of the HPF Standard (the taxonomy, schema and rules) applied to a declaration or HPF record. | `0.9.4` |
| Tagged release | A fixed snapshot of the repository for one standard version. It is never moved. | `v0.9.4` |
| Working draft | The repository between tags. It may carry dated editorial corrections and still names the latest standard version. | `main` |
| Document version | A supporting document's own number, separate from the standard version. | C2PA mapping document version 0.9 |
| Series | The pre-v1 drafts taken together. | v0.9 |

### Editorial corrections to the working draft

Corrections made since the latest tag that do not change meaning. Each preserves the classification, the scope and every obligation for the same facts. They carry no new standard version; documents still name 0.9.4.

- Editorial, 19 November 2026, without changing a rule: the taxonomy's links to the feedback and testing section no longer cite a section number; the note on records made under earlier versions moves from the category definitions to the end of the declaration section; the worked descriptor examples and the Assistive AI examples point to the open questions that cover harder applications; the glossary says the signed declaration is the source of the information rather than "the record", and lists consent and compensation after the kinds of transparency instead of among them; and individual practitioners are named among those whose feedback is welcome.
- Editorial, 19 November 2026, without changing validation: the integration guide is reordered so the current HPF record comes before records made under earlier versions, which are summarised in one table; the handling rules are grouped together; it distinguishes values stored in a record from the labels shown to people; it uses "HPF record", "signed declaration" and "supporting production record" where "record" alone was ambiguous; it notes that the schema does not reject properties it does not define; it lists the signer's name among the contents of the signed declaration, as the taxonomy requires from 0.9.4; and it says that a stored classification value is shown to people with its label, as its own tables already set out.
- Editorial, 19 November 2026, without changing a rule or an identifier: the C2PA mapping separates its own document version from the HPF Standard version; no longer describes the assertion structure as stable, consistent with its statements that the label, namespacing, property names and signer are unsettled; corrects its account of the C2PA label convention, which allows hyphens, against C2PA 2.4 section 6.2; notes that C2PA 2.5 was published in October 2026; no longer implies that every two-part version value is historical; says that the absence of an AI-related action assertion does not establish `no_ai`; describes Durable Content Credentials as one approach, attributed to the Content Authenticity Initiative, rather than as the recommended one; states the hash algorithms C2PA 2.4 allows; and lists its official references.

### 0.9.4 · November 2026 · Pre-v1 draft

Adopts the descriptors as optional vocabulary, refines their definitions and examples, specifies how a record carries them, records the close of the public consultation on 31 October 2026, and accompanies a revised HPF AI Disclosure Form. The three categories, the organising principle, and the highest-category rule are unchanged.

**Taxonomy and declarations**

- **Consultation revision.** The descriptors are adopted as optional vocabulary and are no longer provisional. Their names and machine-readable values are unchanged from 0.9.2, recording them remains optional, and adoption does not settle every application question: how the performance descriptors apply and which combinations are useful remain open under question 2, and how factual summaries describe human contribution to synthetic performance under question 3.
- **Consultation revision.** Descriptor definitions refined. Altered performance concerns a captured or recorded performance by an identifiable person; the factual summary can say what changed, such as appearance, voice, expression, movement, or timing; and it can apply to Assistive AI or Generative AI without deciding the classification. Digital replica records a generated representation of an identifiable person, and Altered performance can be recorded alongside it where the generated material is inserted into or replaces part of that person's captured performance. Synthetic performance may incorporate human acting, voice, or motion capture; it records that the finished performance does not represent a contributing performer as an identifiable person. Generated voice records generated vocal content, can be recorded alongside Digital replica or Synthetic performance where the voice belongs to one, and does not cover AI processing of a recorded voice. Generated visual content can be recorded alongside a performance descriptor where AI also generated visual material that descriptor does not cover; no descriptor requires another. Generated writing and Generated music distinguish output incorporated in the released version from development material and temporary output that was not.
- Combination principle stated: record each descriptor that adds a distinct, relevant fact. The classification, the descriptors, and the factual summary do different jobs and none replaces another. Worked examples added for generated scenery around filmed actors, generated dialogue spoken by an actor, and a generated score.
- A declaration may record descriptors and a reference to supporting production records, both optional. A referenced record stays with the production, need not accompany the declaration, does not become part of it, and is not reviewed or verified by HPF. Continuation pages identify the declaration they belong to and are covered by its signature.
- Practical guidance on establishing the facts: ask the relevant people and suppliers what AI function was used, what output it produced, whether that output reached the named released version, and whether the AI processed supplied material or originated content. Records kept during production and reliable information obtained afterwards may both establish the facts; no recording system, tool inventory, or contemporaneous log is required. A missing fact and uncertainty about a rule are different, and neither is resolved by declaring No AI Used. The declaring party must be able to establish the facts supporting the classification; HPF prescribes no particular enquiry process or recording system, and these steps are recommended methods, not a mandatory questionnaire, contractual recording obligation or audit. A completed questionnaire or log does not establish the facts if its answers are missing or contradictory, and an incomplete production record does not by itself prevent a declaration. Classification is unresolved when missing information prevents the facts being established. This is an explicit 0.9.4 decision.
- Clarified, without changing a rule: development-only brainstorming, critique and unused references are outside the finished-work record where no output is incorporated; human editing does not by itself remove an AI contribution; new pixels alone do not show that content was generated; a Generative AI classification does not mean the whole production was generated; there is no departmental weighting or overall AI score; an HPF classification does not determine genre, animation or live action, authorship, funding category, eligibility, consent, rights, or compliance; a category recorded in another system cannot by itself determine the HPF classification; and a recipient's request for additional information does not become an HPF requirement or change the classification.
- The public consultation closed on 31 October 2026. The consultation section is renamed Feedback and testing before v1.0. It lists what remains to be tested under the same five numbers, Q1 to Q5, followed by how to take part and how to send further feedback; the rules and scope boundaries it previously repeated stay in their own sections. Question 1 is narrowed: the declaration basis is decided and two parts remain, Practical checks (what producers can establish in difficult workflows) and Classification scope, and the other sections refer to them by those names. Working-group participation details are on the website; the Markdown links to them. Question 4 adds autonomous editing and other operations that change captured material without producing a separate generated asset, and question 5 asks how producers proceed when a supplier cannot answer.
- **Descriptor independence.** Descriptors are independently optional: selecting one never requires another. Classification restrictions, and rejection of empty, repeated, undefined or invalid values, are unchanged. Combinations are explained by recommendations and examples only; an omitted descriptor means not declared, not that it cannot apply. The wording that Generated voice accompanies Digital replica or Synthetic performance became "can be recorded alongside".
- **Editorial restructure.** "In-scope AI output" is used in the organising principle and defined as a key term; the role-based wording was removed from Assistive AI without settling autonomous editing; the Scope section uses separate lists; Classification test became Applying the classification test; Edge cases became Applying the standard to production cases with Current guidance and Remaining question for each case; the declaration section separates required, optional and recommended information.
- **Consultation revision.** `hpf_descriptors` is specified as part of the HPF record and may be implemented. It is optional; where present it is an array of one or more distinct values from the descriptor table, in no meaningful order; no descriptor applies to `no_ai`, `assistive_ai` allows `altered_performance` only and `generative_ai` allows any; an empty array, a repeated value, an undefined value, or a value the classification does not allow makes the record invalid; and an omitted field means no descriptor was declared, not that none applies. The taxonomy states these rules under Descriptors, and the schema describes each value.
- Compatibility: the descriptor values and the validation rules in the schema are the ones introduced in 0.9.2. No value is renamed and no rule is stricter, so every record valid under 0.9.2 or 0.9.3, with or without descriptors, stays valid under the version it names, and descriptors on such a record are read with that version's provisional definitions. The schema has never rejected descriptors on a record naming 0.9, 0.9.0 or 0.9.1 and still does not, but those versions define no descriptors, so values on such a record have no HPF meaning. Declarations that use descriptors name a version that defines them. The example set adds records made under 0.9.2 and 0.9.3 that carry descriptors, and invalid records for descriptors on No AI Used, a mixed Assistive AI array, a repeated value, and a value that is not an array.
- Editorial, 2 November 2026, without changing a rule: the rules for `hpf_descriptors` are set out as a table of field rules at the end of the Descriptors section, and the detail on records made under earlier versions is in the integration guide; the organising principle states its two questions as statements; and the glossary introduction and sentences in Scope and the reconstruction test are reworded. The taxonomy page on the website carries the same changes and writes consultation question 1 as continuous text.
- The repository checks now confirm that the descriptor table in the taxonomy and the schema define the same values and restrictions, and that every JSON record shown in a published document is valid.
- Editorial, 2 November 2026, without changing a rule: the reconstruction test is reworded to say that classification depends on whether AI repairs recorded content or adds content the source does not establish, that generating replacement pixels or samples during a repair does not by itself make a use Generative AI, and that fabrication is Generative AI even where the same operation also repairs. It points to questions 1 and 4 for what remains open.
- Requirement, 2 November 2026: the signed declaration includes the signer's name, with the signature and the declaration date. The signer's role or job title is optional, and it does not establish authority; the existing confirmation that the signer is authorised is unchanged. Recipients need to identify who signed, and a job title says little about authority. The change applies to declarations made under 0.9.4 and later versions and not to declarations made under earlier versions. It adds no field to the machine-readable record, and it adds no identity verification, proof of authority, signing service or legal assurance.
- Unchanged: the three categories, the two questions of the organising principle, the highest-category rule, the reconstruction test, the absence of a threshold, the released-version rule, the required record fields, and the descriptor values.

**Guidance**

- 2 November 2026: the HPF AI Disclosure Form is revised. The declaration, its signature and its date stay together on one page, on A4 and US Letter, with the factual use summary on it. An optional descriptor section between the classification and the summary lists the descriptor names; their definitions are in the producer guidance and, on the online form, behind a control that shows them. Tool names and a reference to supporting production records are grouped as optional supporting information, and one line records the number of continuation pages attached, where blank or 0 means none. The declaring party is named in the first section, and the signer's name, an optional role, the signature and the date sit together in the signing block. Producer guidance, with questions for crew and suppliers and the descriptor definitions, is separate from the declaration and marked as not part of it. The online form, its printed output, and the fillable PDF carry the same wording, and drafts saved under the previous two form revisions are restored rather than discarded, including their continuation page count. The signer confirms that the classification, any descriptors selected, the factual use summary, and any continuation pages recorded are accurate for the released version, and that any referenced supporting record is correctly identified. Notes below the signature state that a referenced record is not part of the declaration and need not accompany it, that HPF does not review supporting records, and that the declaration does not establish that any consent, licensing, compensation, rights, contractual, insurance, or regulatory requirement has been met. Each continuation sheet states that it forms part of the declaration and is covered by its signature. The fillable PDF stays A4, embeds its typeface, wraps long entries instead of scrolling them, and carries its producer guidance on separate pages; the form page explains under Printing the fillable PDF that on US Letter it prints scaled to fit.
- Filmmaker guidance explains what to ask crew and suppliers, offers a request they can adapt, and explains how to follow up on missing or conflicting answers, what records can help, and how optional descriptors and record references are used.
- The integration note replaces its warning against descriptor integration with implementation guidance: the controlled values and labels, valid records for No AI Used, Assistive AI with Altered performance, and Generative AI with several descriptors, the invalid cases and what validation does with them, and how to store, pass on and show descriptors. The C2PA mapping carries descriptors under the same rules and remains a working proposal with its own status, including its warning against production integration of the assertion.

**Governance**

- Final consistency pass, 2 November 2026, without changing a classification rule: the production cases make processing classifications conditional on the processing being in scope and refer to the reconstruction test; the classification test says that an unresolved use or missing fact prevents classification only where resolving it could change the classification of the released version, so a retained AI-generated score establishes Generative AI while a separate denoising operation remains open; the descriptor table adds the machine-readable value of each descriptor; the section on records says that records naming 0.9.2 or earlier do not require `hpf_released_version`, which the current schema permits and does not require on them; de-ageing refers to AI-generated replacement speech so that dialogue recorded by an actor is not treated as a Generative AI use; the producer workflow no longer repeats the declaration basis or the signature confirmation; and question 1 states that the declaration basis is set in the declaration section and that testing will examine how producers establish the facts.
- Editorial restructure, 2 November 2026, without changing a rule: the classification test opens with a condition and result table and then explains missing facts and unresolved uses separately; the producer workflow is organised as four steps (establish the facts, complete and sign the declaration, supply it with the relevant paperwork, retain and pass on the declaration) with the declaration basis and the signature confirmation each stated once, and the simplified form illustration is removed from the taxonomy page in favour of a link to the form; the production cases are three short subsections (later releases, restoration and performance changes, VFX and animation) in place of a table; and each question in the feedback and testing section has its own heading. Question 3 no longer carries the sentence that a new descriptor would not be considered before testing the existing descriptors and summary.
- Editorial tightening, 2 November 2026, without changing a rule: the introduction to the document focuses on status, ownership, licensing and self-declaration; the descriptor selection rule is stated once under Choosing descriptors; the scope exclusions for development-only use and for marketing, publicity and sales materials are combined into single entries, and festival submissions are no longer listed as a blanket exclusion because the submitted film remains in scope; the classification test no longer repeats the list of excluded thresholds; the producer workflow says the same declaration can accompany subsequent deliveries of a released version, which creates no delivery obligation; the technical implementation section separates current from historical record requirements, and states that the current schema permits but does not require `hpf_released_version` on records naming 0.9.2 or earlier; and the production cases refer to the reconstruction test and scope provisions, treat AI-generated dialogue performed by a human actor as covered by Generated writing, and no longer repeat qualifications.
- Technical clarification, 2 November 2026, without changing validation: a historical record is validated against the schema published with the version it names and is kept as received, with no renaming or migration, even where the current schema would not accept it. Records that used the earlier version field name validate against the schemas in the v0.9.0 and v0.9.1 tags and not against the current schema. The taxonomy, integration guide, schema description and C2PA mapping state this, and the integration guide says it describes which older records the current schema accepts and is not a general compatibility guarantee.
- Editorial alignment, 2 November 2026, without changing a classification rule or its scope: short summaries of Assistive AI in the classification table, the homepage, the guide and the declaration form now read "In-scope AI output is present, but AI processed human-created material rather than originating new content", and the short question reads "Did the AI process human-created material, or originate new content?". The full definition in section 3.2 keeps "processed or optimised", and reconstruction remains explained in section 3.4 and the restoration guidance. Summaries of the Generative AI no-threshold rule read "regardless of duration, prominence, or proportion".
- Adopts a maintenance and amendment process for after v1.0, described under Amendment process. It is a future process, not a statement that v1.0 has launched. It replaces the earlier post-v1 provisions (a 30-day consultation period for substantive amendments and a five-working-day acknowledgement for issues and pull requests) with annual review, a six to eight week comment period on concrete proposals, at least three months' notice for changed technical requirements, a public record of amendment decisions, and no fixed response time for every submission. Editorial and guidance changes, the recommended correction practice, the released-version rule and the pre-v1 process are unchanged.

**Tools**

- Policy Mapper rules 0.1.2, replacing 0.1.1. It cites the standard as 0.9.4 and describes descriptors as optional rather than provisional. No mapping rule changed.
- AI Use Checker parser 1.12.0, replacing 1.11.1, cites the standard as 0.9.4. Where a description has the AI make editing decisions itself on captured material and the result can reach the finished work, it returns the open-case result under question 4 instead of Assistive AI; using only the production's own footage no longer settles that case. Human-directed editing assistance, discarded edits and marketing material keep their earlier readings, and a generating job still decides the category. Its explanations name the classification-scope part of question 1 where an established machine-learning feature is the open case. It returns no descriptors.

Text as released: [tag v0.9.4](https://github.com/human-provenance-in-film/hpf-taxonomy/tree/v0.9.4), 2 November 2026.

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
