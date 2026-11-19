# HPF AI Disclosure Taxonomy

**Version 0.9.4, pre-v1 draft**
Updated November 2026. The public consultation closed on 31 October 2026.

Human Provenance in Film (HPF) is a free, open standard for declaring AI output present in finished film and television productions. It gives audiences and receiving organisations a common record of how AI was used. The producer selects one of three categories and records it in one signed declaration. The declaration travels with the production in existing deal, delivery and other production paperwork, so every recipient reads the same record.

This document sets out the classification, the declaration and the machine-readable record. HPF is a self-declaration standard. It does not certify productions, audit workflows, or determine consent, rights or regulatory compliance.

---

## Organising principle

> Is AI output present in the named finished version? If so, did the AI process human-created material or originate new content?

The producer answers two questions of fact about the version the declaration names. The first is whether any in-scope AI output is present in that version as distributed; if none is, the classification is No AI Used. The second, where in-scope AI output is present, is whether the AI processed human-created material (Assistive AI) or originated new content that appears in the finished work (Generative AI). The producer signs the declaration and is responsible for its accuracy. HPF does not verify it.

In-scope AI output is AI output that is present or embodied in the released version, as set out under [Scope](#scope). The qualification matters because the standard has not yet settled whether some established machine-learning functions, such as denoising and tracking, are in scope; that is the classification-scope part of [consultation question 1](#consultation).

HPF classifies how AI was used, not the underlying model or product. The same AI system can support an Assistive use in one production and a Generative use in another.

### Key terms

**Artificial intelligence**, for the purposes of this taxonomy, means software systems that use machine learning, neural networks, or similar techniques trained on data to generate, synthesise, enhance, or analyse content, as distinct from deterministic software that applies fixed rules or algorithms without learned models. Where a tool offers both conventional and AI-powered modes, only the AI-powered mode's output is in scope.

**AI tool** means any software that uses artificial intelligence, as defined above, to produce, modify or optimise content. Standard digital tools that do not use it are not AI tools.

**In-scope AI output** means AI output that is present or embodied in the released version a declaration covers, as described under [Scope](#scope).

**Released version** means a separately released editorial edition or substantive localisation of a work, identified by its picture, sound and, where relevant, embedded audience-facing text.

**Finished production**, also called the finished film or the finished work, means the released version a declaration covers, as distributed or exhibited. This taxonomy covers film and television.

---

## Released versions and declarations

One signed declaration covers one released version of a work and may travel with every delivery of that version. A later released version, such as a later editorial edition or a substantive localisation, has its own signed declaration, even where the classification and factual summary are unchanged; the new declaration may repeat those facts. It does not change the record for the earlier version; the earlier declaration continues to cover its version. HPF does not require the producer to notify recipients of an earlier version, although contracts or distribution arrangements may.

How this rule applies to episodic works, to selectable subtitles and captions, and at the boundary between technical and substantive localisation is open under [consultation question 4](#consultation). [Classify and declare your production](https://humanprovenance.film/resources/classify-and-declare-your-production/#released-versions) gives informative examples of releases that normally do and do not need a new declaration.

---

## Applying the classification test

For the released version the declaration covers, the highest applicable category governs.

| Condition in the released version | Classification |
|---|---|
| Any in-scope AI-originated content is present | `generative_ai` |
| In-scope AI output is present, but AI processed human-created material rather than originating new content | `assistive_ai` |
| No in-scope AI output is present | `no_ai` |

A film with AI-assisted colour grading and an AI-generated score is `generative_ai`. A `no_ai` declaration records that no in-scope AI output was found in the released version, not that nothing is known.

Whether some established processing functions, such as denoising, upscaling and tracking, count as in-scope AI output is open under [Q1](#consultation).

### Missing facts that could affect the classification

If missing facts could change the classification, no declaration is made until those facts can be established. Missing information is never evidence of No AI Used. A missing fact that could not change the classification, such as a further detail of a production already established as `generative_ai`, does not prevent a declaration. Nor does a missing optional record, such as a supporting production record, because what matters is whether the facts themselves can be established.

### Known uses whose treatment is unresolved

Some uses fall within a question the standard has not yet resolved, such as whether an established machine-learning function requires disclosure ([Q1](#consultation)) or how autonomous editing of captured material is treated ([Q4](#consultation)). The producer does not force a classification for that use and does not select No AI Used by default. The use prevents classification only where resolving the question could change the classification of the released version. For a production with no other in-scope AI output it could. For a production already established as `generative_ai` it could not: a retained AI-generated score establishes `generative_ai` while the treatment of a separate denoising operation remains open.

A declaration never presents a use whose classification remains unresolved as settled. It must still contain the required information and an accurate factual summary. The declaring party must also be able to establish the facts supporting any selected descriptors.

---

## Categories

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

These values correspond to `hpf_classification` in [schema.json](schema.json). A record made under this version carries `hpf_standard_version`, which names the version of this taxonomy that was applied; `hpf_released_version`, which identifies the released version the declaration covers; and `hpf_classification`. It may also carry the optional `hpf_descriptors` array.

### `no_ai`: No AI Used

No in-scope AI output is present in the finished film.

No AI Used applies to the named released version. AI may have been used during development or elsewhere in the production workflow without its output being incorporated into that version (see [Scope](#scope)). The classification describes the finished version. It does not describe the whole production process, how the work was staffed, or its rights position.

**Examples:** editing, colour grading, compositing, sound design, music recording, and visual effects performed without AI tools.

### `assistive_ai`: Assistive AI

In-scope AI output is present in the finished film, but the AI processed or optimised human-created material rather than originating new content. The classification turns on what the AI did and what output it left in the finished work, not on whether a person held a particular creative or production role.

**Examples:** AI-assisted colour grading; AI-assisted sound clean-up; de-flickering and archival restoration that repair supplied footage; cosmetic de-ageing of a performance captured in full, where AI refines appearance without rebuilding or generating any part of the performance; in animation, AI used to clean up or optimise frames created by animators. Whether some established processing functions require Assistive AI disclosure is open under [Q1](#consultation); see also [The reconstruction test](#the-reconstruction-test).

**Not `assistive_ai`:** if AI originated new content that appears in the finished work, the classification is `generative_ai`, even where human-created material was used as an input, and regardless of how the tool is marketed.

### `generative_ai`: Generative AI

AI originated content that appears in the finished film, rather than processing human-created material. If any qualifying AI-originated content appears in the finished work, the production is `generative_ai` regardless of duration, prominence, or proportion. A film using human-shot footage alongside a single AI-generated environment, title sequence or insert is `generative_ai` overall.

**Examples:** AI-generated backgrounds, environments, crowd scenes, or set extensions; AI-written screenplay elements present in the finished film; synthesised or cloned actor performances; AI voice cloning; AI-generated music present in the finished film; de-ageing or posthumous synthesis that fabricates part of a performance rather than refining one fully captured on set; in animation, AI-generated characters, environments, or sequences present in the finished work.

A `generative_ai` classification records that AI-originated content is present. It does not mean the whole production was generated. A film with actors recorded on set, with AI-generated scenery added in post-production, is `generative_ai`; its factual summary says that the performances were filmed and which scenery was generated, so a reader can tell it apart from a film with generated performers.

**Not `generative_ai`:** cosmetic enhancement of a performance that was captured in full is `assistive_ai`. Established machine-learning tools that process human-created material, such as denoising, upscaling, or tracking, are not `generative_ai`; whether they require `assistive_ai` disclosure is not settled in v0.9.4 and is the classification-scope part of [consultation question 1](#consultation).

---

## The reconstruction test

When AI works on existing footage, images, or sound, classification depends on whether it repairs recorded content or adds content that the source does not establish.

**Reconstruction** repairs material captured or created by people. De-flickering footage and removing recording artefacts are Assistive AI uses where they restore information supported by the source. The software may generate replacement pixels or audio samples during the repair; that alone does not make the use Generative AI.

**Fabrication** adds content that was not captured or created in the source material. Examples include generating scenery behind a removed object, inventing missing detail, or generating words or movements that a performer did not give. These are Generative AI uses, including when the same operation also repairs existing material.

Some restoration processes combine repair and invented detail in ways that are difficult to separate. These cases remain under review in [Q4](#consultation). [Q1](#consultation) separately asks which established processing functions, such as denoising, upscaling, and tracking, require Assistive AI disclosure at all. Automated subtitles and captions are also being considered under Q4.

---

## Descriptors

**Optional.** The descriptors were introduced as provisional terms in the August 2026 revision. Their names, values, and definitions are adopted for 0.9.4. HPF may refine them before v1.0 where evidence from testing shows a need, and a refinement that changes a value or a meaning would be made in a new version. How they apply in some performance cases is being tested under [question 2](#consultation).

#### Choosing descriptors

Descriptors are individually optional and may be selected separately or together. Selecting one does not require selecting another, and not every applicable descriptor has to be declared. An omitted descriptor means it was not declared, not that it cannot apply. The factual summary remains required for in-scope AI use.

Descriptors add factual information about the kind of AI output present in the finished work. They never determine or change the classification and carry no threshold. `altered_performance` may be recorded on an Assistive AI or a Generative AI production. Every other descriptor applies only to Generative AI. None applies to No AI Used.

| Descriptor | Value | Applies to | What it records |
|---|---|---|---|
| Altered performance | `altered_performance` | Assistive or Generative AI | AI changed a captured or recorded performance by an identifiable person, and the changed performance is in the finished production. The factual summary can say what changed, such as appearance, voice, expression, movement, or timing. The descriptor does not decide the classification: AI that processed the captured performance is Assistive AI, and AI that originated part of the performance is Generative AI. |
| Digital replica | `digital_replica` | Generative AI | AI generated a representation of an identifiable person, such as their likeness, voice, or performance, that is present in the finished production. Where the generated material is inserted into or replaces part of a performance that person gave on camera or on a recording, Altered performance can be recorded alongside it. |
| Synthetic performance | `synthetic_performance` | Generative AI | AI generated performance content that does not represent an identifiable person. Human acting, voice, or motion capture may have contributed to it. The term records that the finished performance does not represent a contributing performer as an identifiable person; it does not mean that no human performance contributed. |
| Generated voice | `generated_voice` | Generative AI | AI generated spoken or vocal content present in the finished production. It records the modality, so it can be recorded alongside Digital replica or Synthetic performance where the generated voice belongs to a replica or a synthetic performance. AI processing of a recorded voice, such as noise reduction or clean-up, is not Generated voice. |
| Generated visual content | `generated_visual_content` | Generative AI | AI generated visual content present in the finished production, such as an environment, background, set extension, object, title, or sequence. |
| Generated writing | `generated_writing` | Generative AI | AI generated written content embodied in the finished production, such as dialogue performed by an actor, narration, or on-screen text. AI-written text used only in development and not reflected in the finished production is outside the declaration. |
| Generated music | `generated_music` | Generative AI | AI generated music present in the finished production. A generated temporary score replaced before delivery is outside the declaration. |

#### Combining descriptors

More than one descriptor may describe the same use, and each adds a distinct fact. A descriptor that only repeats what another already records is not needed. For example, Generated visual content can be recorded alongside a performance descriptor where AI also generated visual material that the performance descriptor does not cover, such as scenery around a performer. It is not expected for every replica or synthetic performance that appears on screen. Which combinations are most useful in harder performance cases is part of question 2.

#### Descriptors, classification, and summary

The three do different jobs and none replaces another. The classification states the highest category that applies to the released version. Descriptors name kinds of AI output present. The factual summary says what the AI did and what output reached the released version, including what was captured and what AI changed or generated.

#### Worked descriptor examples

Each row shows a classification and the descriptors that describe the use. These rows are current guidance. How the performance descriptors apply in harder cases, and which combinations are most useful, is open under [Q2](#consultation).

| What happened | Classification and descriptors |
|---|---|
| Cosmetic AI de-ageing of a performance captured in full. | Assistive AI, Altered performance |
| Actors filmed on set, with AI-generated scenery added in post-production. Their faces and performances were not changed. | Generative AI, Generated visual content |
| AI-generated speech representing an identifiable actor, inserted into footage of their captured performance. | Generative AI, Digital replica, Generated voice, Altered performance |
| A wholly generated performer who does not represent an identifiable person. | Generative AI, Synthetic performance |
| A wholly generated fictional narrator. | Generative AI, Synthetic performance, Generated voice |
| Dialogue generated by AI and spoken by a human actor in the usual way. | Generative AI, Generated writing |
| An AI-generated score retained in the final mix. | Generative AI, Generated music |

In the third example each descriptor could record a different fact: Digital replica, that the generated material represents an identifiable person; Generated voice, that spoken content was generated; Altered performance, that a performance the actor gave on camera was modified. Where AI-generated dialogue is performed by a human actor and retained in the released version, the classification is Generative AI. The optional Generated writing descriptor can record that use, rather than Generated voice or Digital replica, because the actor's own performance carries the generated words.

Descriptors are factual provenance terms. Where a descriptor resembles a term in a collective agreement or contract, it takes its meaning from this standard alone. Descriptors do not state whether consent was obtained or whether rights, contractual or collective-agreement requirements were met, and they do not replace contracts, releases, consent records or chain-of-title documentation.

#### In a record

The optional `hpf_descriptors` field in a machine-readable record lists the descriptors the declaring party selected. The field is defined in [schema.json](schema.json). The [integration guide](INTEGRATION.md#descriptors) gives valid and invalid example records and explains how records made under earlier versions are read.

| Field rule | Requirement |
|---|---|
| Permitted values | Each value is one of the seven machine-readable values in the Value column of the descriptor table above. `no_ai` allows none, `assistive_ai` allows `altered_performance` only, and `generative_ai` allows any. |
| Selection | Each descriptor can be selected separately or together with others, and no descriptor requires another. Where the field is present, it is an array of one or more values. List each selected descriptor once. Values can appear in any order. |
| No descriptors declared | Omit the field if no descriptors are declared. An empty array is not valid. A record without the field, or a record that omits a particular descriptor, says only that the descriptor was not declared, not that it cannot apply. No one may add descriptors to it on the declaring party's behalf, whether from the classification, the factual summary, tool names, or detection output. |
| Invalid records | A record is invalid if `hpf_descriptors` is empty, repeats a value, contains a value not in the table, or contains a value its classification does not allow. |
| Version | Interpret descriptors using the standard version named in the record. A declaration that records descriptors names a version that defines them, which for a new declaration is the current version. Versions before 0.9.2 define none. |

---

## Scope

This taxonomy covers AI output that is present or embodied in the named finished version as distributed or exhibited. Production stages alone do not determine scope: AI used at any stage, from development to post-production, is in scope when its output reaches or is embodied in the declared released version, and is outside the declaration when its output does not. Output is incorporated when it is present or embodied in the released version.

Development-stage output is in scope when incorporated into the released version, such as generated dialogue performed in the film or pitch visuals reused as a title sequence. Brainstorming, critique, and unused references do not prevent a No AI Used declaration where no AI output is incorporated. Influence alone is not incorporation.

Human editing does not automatically remove an AI contribution. Whether substantially transformed output remains in scope is open under [Q4](#consultation).

### Covered by the declaration
- AI output that is present or embodied in the released version a declaration covers, whichever production stage it came from
- In-scope output supplied by the production company, a co-producer, or a third-party contractor

### Outside the declaration
- AI used for development, administration, or production management where none of its output is incorporated into the released version, such as script analysis, financial modelling, or scheduling
- AI output used only in marketing, publicity, or sales materials, such as posters, trailers, social media assets, sales decks, and EPKs, is outside the declaration. Any such output also incorporated into the named released version must be assessed under the same scope and classification rules as other output.
- Basic automation in standard long-standing industry use: loudness normalisation, timecode tools, spell-check

The production company or lead producer records one classification for the finished production, using the highest applicable category. Who produced a given element does not change the classification.

Rights, consent, contracts, insurance and legal compliance remain outside HPF. Organisations address them through their own processes. HPF does not assess the licensing of AI training data.

An HPF classification does not determine a work's genre, whether it is animation or live action, its authorship, its funding category, or its eligibility for any scheme, festival, or award.

---

## Applying the standard to production cases

These cases show how the current rules apply to particular production and release situations. Apply these examples alongside [The reconstruction test](#the-reconstruction-test) and [Scope](#scope). Where a question remains open, the case says so and links to [Feedback and testing before v1.0](#consultation).

### Later releases

A restored or remastered edition that changes the released picture or sound, a director's cut, an extended edition, and any other re-edit released after the original is a later released version with its own declaration, under the [released-version rule](#released-versions-and-declarations). The classification of the new version depends on all in-scope AI output it contains, including output retained from the original. Not every technical delivery variation is treated as a different released version, and where that boundary falls is open under [Q4](#consultation).

The provisional position on episodic and series content is that classification applies per episode, with the highest category across any episode applying where a series is classified as a whole. [Q4](#consultation) leaves open the unit of declaration (title, season or episode), how the released-version rule applies to episodes, seasons and series, and how classifications aggregate across episodes. It also covers how subtitles, captions and dubbing bear on the released version.

### Restoration and performance changes

The reconstruction test applies to archival restoration. Repair of source-supported content is `assistive_ai` where the processing is in scope, and AI-invented content retained in the released version is `generative_ai`. Hybrid restoration, where repair and invented detail are hard to separate, is open under [Q4](#consultation), and whether established functions such as denoising and upscaling are in scope is open under [Q1](#consultation). Where a third-party archive performed processing before the footage was licensed and the producer cannot establish what was done, that is a factual-information problem handled under [Applying the classification test](#applying-the-classification-test).

De-ageing follows the same test. De-ageing that adjusts or restores captured appearance is reconstruction, and is `assistive_ai` where the processing is in scope. AI-generated content that the performer did not give, such as posthumous synthesis or AI-generated replacement speech, is `generative_ai`. Recording replacement dialogue with a human actor is not itself a Generative AI use. AI-generated dialogue performed by a human actor is covered by Generated writing in [Descriptors](#descriptors). Applications in which refining captured appearance and generating performance content are hard to separate are part of the hybrid and substantially transformed cases in [Q4](#consultation).

### VFX and animation

The classification test applies to VFX and animation as it does to live action. Many tools in these fields have used machine learning for years, for example for denoising, upscaling, motion estimation, tracking, deep compositing, and rotoscoping assistance. Where a tool processes footage or elements captured or created by human crew, it is not automatically `generative_ai`. It is `generative_ai` where it originates content that is retained in the finished work, such as characters, environments or sequences.

Which of these processing functions require `assistive_ai` disclosure, or sit with the routine automation outside scope, is open under [Q1](#consultation), as is what producers can establish about features built into established software (Q1 and [Q5](#consultation)). Workflows in which the line between processing and origination is hard to draw are part of [Q4](#consultation).

---

## The declaration

No technical integration is required. The declaration is a signed producer document, on paper or digital. The [HPF AI Disclosure Form](https://humanprovenance.film/disclosure-form/) has every field, and any document that carries the same information can be used instead.

### 1. Establish the facts

The declaring party must be able to establish the facts supporting the classification. The methods below describe ways to obtain that information; HPF does not prescribe a particular enquiry process or recording system.

- Ask the people and suppliers responsible for material that may have reached the released version what AI function was used, what output it produced, whether that output reached the version, and whether the AI processed human-created material or originated content. Suppliers provide facts about their own deliverables, and the authorised declaring party determines the classification and signs.
- Consult records kept during production, such as asset logs, VFX breakdowns, cue sheets and dated supplier replies.
- Follow up on gaps and conflicting answers, checking each against the version being declared.

These methods are recommended, not prescribed. Reliable information obtained after production can establish the facts; a completed questionnaire or production log is insufficient if material answers remain missing or contradictory.

A category or label recorded in another system, such as a production database, a vendor report, or another disclosure scheme, cannot by itself determine the HPF classification. Check the underlying facts against the released version being declared. What to do when facts are missing or a rule is unresolved is set out under [Applying the classification test](#applying-the-classification-test). What producers can establish in difficult workflows, such as software with AI features that may run automatically, is part of the practical testing under Q1 and Q5 in [Feedback and testing before v1.0](#consultation).

### 2. Complete and sign the declaration

#### Required information

The declaration identifies:

- the work and the released version it covers;
- the classification and the version of the HPF standard applied;
- the party making the declaration;
- the name and signature of a person authorised to declare on behalf of the declaring party, and the declaration date;
- a short factual summary, where in-scope AI use is present, of what the AI did and what output reached the finished work. Tool names can support the summary but do not replace it.

It is signed by someone authorised to declare on behalf of the production. The signer's role or job title may be supplied optionally; a job title does not establish authority. This requirement applies to declarations made under this version, not to declarations made under earlier versions. By signing, the authorised person confirms that the classification, any descriptors selected, the factual summary and any continuation pages are accurate for the released version, and that any supporting record the declaration references is correctly identified.

#### Optional information

A declaration may also record:

- descriptors (see [Descriptors](#descriptors)), which can be selected separately or together;
- the names of the AI tools used;
- a reference to supporting production records, such as an asset log, VFX breakdown, cue sheet, or supplier reply;
- continuation pages, where the factual summary needs more space.

A referenced supporting record stays with the production. It does not have to accompany the declaration, confidential records need not be shared, and HPF does not review or verify it. The record itself is not part of the signed declaration, although the signature covers its identification. A continuation page is different: it identifies the declaration it belongs to and is part of it, so the declaration's signature covers it.

The declaration records AI output present in the released version. It does not request, store or carry consent, licensing, compensation, rights or compliance information, and it does not establish that any contractual, legal or policy requirement has been met (see [Scope](#scope)).

### 3. Supply it with the relevant paperwork

The producer supplies the signed declaration with the deal and delivery paperwork it already uses. A sales agent can pass it to buyers with the delivery materials, or the producer can supply it directly to the platform, broadcaster, festival or other organisation that requests it.

### 4. Retain and pass on the declaration

The producer keeps the signed declaration with the production's records. The same declaration can accompany subsequent deliveries of that released version, and receiving organisations retain, pass through, interpret or display the same version-specific record without recalculating the classification. HPF sets no retention period, no notification obligation and no mandatory distribution route.

### Correcting a declaration

If a declaration contains an error, HPF recommends that the producer issue a corrected declaration for the same released version, carrying its own date and naming the declaration it replaces. This is recommended practice in 0.9.4, not a requirement. A declaration for a later released version does not correct the earlier one, because each released version has its own declaration.

### Declaring an already released production

An authorised party may make a declaration for a production already released, where it can establish the relevant facts. The declaration carries the date it was made, not the release date. No one may infer a classification from a release date, detection output or incomplete catalogue information, or apply one in bulk across a catalogue. Where no declaration has been made, there is no record. An absent declaration establishes neither that AI was used nor that it was not used.

### How recipients use the declaration

The disclosure rests on the producer's signed declaration, which sits alongside other producer representations in existing deal, delivery and other production paperwork. HPF does not verify the declaration or audit the production's tools or workflows. A declaration is not by itself a contractual warranty. Parties may incorporate the classification into their representations and warranties, and any remedy for misrepresentation is then a matter for their contract.

A receiving organisation decides whether to request a declaration and may ask for additional information under its own policies. Such a request does not become an HPF requirement and does not change the producer's classification. HPF encourages platforms and distributors to display the classification but does not require display or prescribe a label, format or placement.

Technical implementation, including how an HPF record is stored and carried, is in [INTEGRATION.md](INTEGRATION.md).

### Earlier versions

Historical records remain valid if they meet their applicable historical schema, even where the current schema does not accept them. Keep them as received; do not automatically rename fields or migrate them.

- Versions 0.9.1 and earlier used `hpf_taxonomy_version`; 0.9.2 introduced `hpf_standard_version`.
- `hpf_released_version` became required in 0.9.3.
- Descriptors were introduced as optional, provisional vocabulary in 0.9.2 and adopted in 0.9.4 with the same machine-readable values. Versions before 0.9.2 define no descriptors.

Interpret each record using the version it names. The [integration guide](INTEGRATION.md) explains historical validation, current-schema compatibility, and descriptor handling.

---

## Relationship to regulation

HPF is a voluntary disclosure standard for AI output in finished film and television. An HPF declaration does not establish legal compliance or replace obligations under applicable law.

---

## Glossary and definitions

This glossary defines terms used around AI disclosure in film. Terms defined earlier in this document are not restated.

### Different kinds of transparency

- **Regulatory transparency**: disclosure or marking required by law, such as Article 50 of the EU AI Act.
- **Technical provenance**: records of a digital asset's origin and history. Content Credentials can carry such records. Watermarking and fingerprinting can support identification or link content to records, but do not necessarily provide a provenance history themselves.
- **Production disclosure**: information about how a finished work was made, supplied by the party responsible for it. HPF provides this form of production disclosure. The producer's signed declaration is the source of this information, and existing deal, delivery and other production paperwork is the route by which it reaches the organisations and audiences that use it.

HPF complements technical provenance and regulatory disclosure and does not replace them.

**Consent and compensation** are not forms of transparency. They are rights mechanisms, such as collective-bargaining provisions, licences and permissions, that govern whether material, performances or data may be used and on what terms. HPF does not determine consent, compensation or underlying rights.

### How information is recorded

| Term | Meaning |
|---|---|
| Metadata | Information stored with a digital asset rather than forming part of the picture or sound. Ordinary metadata can be altered and is often lost when files are transcoded, exported or uploaded. |
| Provenance | A documented history of a digital asset: where it came from, what contributed to it, what happened to it, and who made the claims. It does not necessarily establish that the record is complete, that the content is true, or that rights were obtained. |
| C2PA and Content Credentials | C2PA provides a technical standard for signed provenance claims, commonly presented as Content Credentials. Signature validation checks the integrity of the signed claims and the signing credential. It does not establish that every claim is true. [c2pa-mapping.md](c2pa-mapping.md) explains how C2PA relates to HPF. |
| Ingredient | In C2PA terminology, an asset used in creating another asset. Provenance attached to one ingredient, such as a camera capture, does not by itself describe how the finished production was made. |
| Watermarking | Information embedded in the content itself, visible or detectable by software. What can be inferred from it depends on the watermarking system. |
| Fingerprinting | A representation calculated from the content and matched against records held elsewhere. YouTube Content ID is an example. |
| Machine-readable marking | A marking that allows AI-generated or manipulated content to be identified by automated means, as required of AI system providers by Article 50(2) of the EU AI Act. |

### How information is communicated

| Term | Meaning |
|---|---|
| Labelling | A statement presented to an audience about the nature or production of a work, such as a caption, icon or end card. Confidence in it depends on the process behind the claim. |
| Disclosure | Providing defined information to a defined recipient. An audience label is one form of disclosure; a declaration supplied to a distributor or financier is another. |
| Self-declaration and certification | A **self-declaration** is a claim made by the party responsible for the work. **Certification** involves an independent body assessing conformity with specified requirements. HPF uses self-declaration, not certification. |

Where recognised definitions for these terms exist or emerge in the creative sectors, HPF will seek to align with them rather than create a competing vocabulary. The glossary may be revised before v1.0. Reference to an external standard, technology, organisation or regulatory framework does not imply coordination with or endorsement by that body.

---

<a id="consultation"></a>

## Feedback and testing before v1.0

### Consultation outcome

The public consultation closed on 31 October 2026. Responses are informing the revisions before v1.0, including the adopted optional descriptors and updated declaration form. Contributors will be acknowledged according to their attribution preferences, and private responses will not be identified.

### What remains to be tested

Before v1.0, the working groups will use production cases to test the classifications, descriptors, and declaration form. Some cases will help improve the guidance; others will inform decisions about disclosure scope and released versions. The questions below identify what remains unresolved.

#### Q1: Practical checks and established machine learning

The agreed declaration basis is in [The declaration](#the-declaration).

##### Practical checks

What can producers establish in difficult workflows, particularly when software includes AI features that may run automatically, and what practical guidance would help?

##### Classification scope

Which established functions, such as denoising and tracking, should require Assistive AI disclosure?

#### Q2: Applying performance descriptors

Can practitioners consistently distinguish altered performances, digital replicas, and synthetic performances? When does adding Generated visual content explain something further, and when does it repeat information?

#### Q3: Human contributions to synthetic performances

Does the factual summary clearly explain how human acting, voice, or motion capture contributed to a synthetic performance?

#### Q4: Difficult production and release cases

How should the rules treat masks and mattes used in compositing, autonomous editing, substantially transformed output, and restoration that combines repair with invented detail? The same question covers episodes, subtitles, captions, dubbing, and the line between a technical delivery variation and a different released version.

#### Q5: Completing and receiving declarations

What facts can producers establish from their records and suppliers, what should they do when answers are missing or conflict, and does the completed declaration give recipients useful information?

### Working groups

Participation details for the pre-v1 working groups are on the [HPF website](https://humanprovenance.film/taxonomy#working-groups).

### Continuing feedback

Feedback on the standard remains welcome from individual practitioners and from trade associations, unions and guilds, festivals, awards bodies, commissioners, funders, and other industry organisations. Companies considering adopting HPF can also send technical and implementation feedback. Email contact@humanprovenance.film, or open an issue or pull request in the [GitHub repository](https://github.com/human-provenance-in-film/hpf-taxonomy).

Earlier consultation wording is preserved in the release tags. The [version history](GOVERNANCE.md#version-history) records subsequent changes.

After v1.0, HPF intends to consider substantive changes through an annual review, with guidance and documented corrections possible between reviews. A new version of the standard does not by itself require an existing declaration to be remade. The [amendment process in GOVERNANCE.md](GOVERNANCE.md#amendment-process) sets this out.

---

## Licence

CC BY 4.0. See [LICENSE.md](LICENSE.md).

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
