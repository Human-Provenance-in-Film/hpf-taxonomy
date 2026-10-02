# HPF AI Disclosure Taxonomy

**Version 0.9.3, draft for consultation**
Updated October 2026. Consultation closes 31 October 2026.

Human Provenance in Film (HPF) is a free, open standard for declaring AI output present in finished film and television productions. It gives audiences and receiving organisations a common record of how AI was used. The producer selects one of three categories and records it in one signed declaration. The declaration travels with the production in existing deal, delivery and other production paperwork, so every recipient reads the same record.

This document sets out the classification, the declaration and the machine-readable record. HPF is a self-declaration standard. It does not certify productions, audit workflows, or determine consent, rights or regulatory compliance.

---

## Organising principle

> Is AI output present in the named finished version? If so, did the AI process human-created material or originate new content?

The producer answers two questions of fact about the version the declaration names. Is any AI output present in that version as distributed? If not, it is No AI Used. If it is, did the AI process human-created material (Assistive AI) or originate new content that appears in the finished work (Generative AI)? The producer signs the declaration and is responsible for its accuracy. HPF does not verify it.

HPF classifies how AI was used, not the underlying model or product. The same AI system can support an Assistive use in one production and a Generative use in another.

### Key terms

**Artificial intelligence**, for the purposes of this taxonomy, means software systems that use machine learning, neural networks, or similar techniques trained on data to generate, synthesise, enhance, or analyse content, as distinct from deterministic software that applies fixed rules or algorithms without learned models. Where a tool offers both conventional and AI-powered modes, only the AI-powered mode's output is in scope.

**AI tool** means any software that uses artificial intelligence, as defined above, to produce, modify or optimise content. Standard digital tools that do not use it are not AI tools.

**Released version** means a separately released editorial edition or substantive localisation of a work, identified by its picture, sound and, where relevant, embedded audience-facing text.

**Finished production**, also called the finished film or the finished work, means the released version a declaration covers, as distributed or exhibited. This taxonomy covers film and television.

---

## Released versions and declarations

One signed declaration covers one released version of a work and may travel with every delivery of that version. A later released version, such as a later editorial edition or a substantive localisation, has its own signed declaration, even where the classification and factual summary are unchanged; the new declaration may repeat those facts. It does not change the record for the earlier version; the earlier declaration continues to cover its version. HPF does not require the producer to notify recipients of an earlier version, although contracts or distribution arrangements may.

How this rule applies to episodic works, to selectable subtitles and captions, and at the boundary between technical and substantive localisation is open under [consultation question 4](#consultation). [Classify and declare your production](https://humanprovenance.film/resources/classify-and-declare-your-production/#released-versions) gives informative examples of releases that normally do and do not need a new declaration.

---

## Classification test

For the released version the declaration covers:

1. Is any AI output present in the finished film? If not: `no_ai`.
2. If yes: did the AI process human-created material, or originate new content that appears in the finished work?
3. Processing human material: `assistive_ai`. Originating new content: `generative_ai`.

The test turns on what is in the finished film, not on whether a human would otherwise have performed the function. AI-generated content that appears in the finished work is `generative_ai` whether or not a human could have produced it.

A production is classified at the highest category applicable to any element. Where in-scope AI output is present, the declaration includes a concise factual summary of what the AI did and what output reached the released version. A film with AI-assisted colour grading (`assistive_ai`) and an AI-generated score (`generative_ai`) is `generative_ai`. There is no percentage threshold and no de minimis exception.

Where the answer is unknown or the records are incomplete, the classification is unresolved. Missing, uncertain or absent information is never No AI Used. A `no_ai` declaration records that no in-scope AI output was found, not that nothing is known.

---

## Categories

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

These values correspond to `hpf_classification` in [schema.json](schema.json). A record made under this version carries three fields: `hpf_standard_version`, which names the version of this taxonomy that was applied; `hpf_released_version`, which identifies the released version the declaration covers; and `hpf_classification`. `hpf_released_version` was added in 0.9.3. A record made under 0.9.2 carries the other two fields only and is read under the version it names. The version field was named `hpf_taxonomy_version` before 0.9.2.

### `no_ai`: No AI Used

No AI output is present in the finished film. No AI tool produced any element of the finished work as distributed.

No AI Used applies to the named released version. AI may have been used during development or elsewhere in the production workflow without its output being incorporated into that version (see [Scope](#scope)). The classification describes the finished version. It does not describe the whole production process, how the work was staffed, or its rights position.

**Examples:** editing, colour grading, compositing, sound design, music recording, and visual effects performed without AI tools.

### `assistive_ai`: Assistive AI

AI output is present in the finished film, but the AI processed or optimised material created by human crew rather than originating new content. A human held the creative or production role; the AI worked from their material.

**Examples:** AI-assisted colour grading; AI-assisted sound clean-up; de-flickering and archival restoration that repair supplied footage; cosmetic de-ageing of a performance captured in full, where AI refines appearance without rebuilding or generating any part of the performance; in animation, AI used to clean up or optimise frames created by animators. Some processing functions remain under consultation: see [The reconstruction test](#the-reconstruction-test).

**Not `assistive_ai`:** if AI originated new content that appears in the finished work, the classification is `generative_ai`, even where human-created material was used as an input, and regardless of how the tool is marketed.

### `generative_ai`: Generative AI

AI originated content that appears in the finished film, rather than processing human-created material. If any qualifying AI-originated content appears in the finished work, the production is `generative_ai` regardless of duration, prominence, or proportion. A film using human-shot footage alongside a single AI-generated environment, title sequence or insert is `generative_ai` overall.

**Examples:** AI-generated backgrounds, environments, crowd scenes, or set extensions; AI-written screenplay elements present in the finished film; synthesised or cloned actor performances; AI voice cloning; AI-generated music present in the finished film; de-ageing or posthumous synthesis that fabricates part of a performance rather than refining one fully captured on set; in animation, AI-generated characters, environments, or sequences present in the finished work.

**Not `generative_ai`:** cosmetic enhancement of a performance that was captured in full is `assistive_ai`. Established machine-learning tools that process human-created material, such as denoising, upscaling, or tracking, are not `generative_ai`; whether they require `assistive_ai` disclosure is not settled in v0.9.3 and is the classification-scope part of [consultation question 1](#consultation).

---

## The reconstruction test

Some AI tools work on footage, audio, or images that already exist. For these, classification turns on whether the tool reconstructs content already present or fabricates content that is not.

**Reconstruction** restores, cleans, or repairs content that was captured or created by a human, such as de-flickering, artefact removal, or format conversion. The output is the same content in better condition. This is `assistive_ai`.

**Fabrication** invents content that was never captured or created, such as painting in a background revealed by removing an object, generating frames or detail with no source, or synthesising a performance element the performer did not give. This is `generative_ai`.

Classification turns on this distinction, not on whether the software technically synthesised pixels, frames or audio, and not on the label a vendor applies. Where a tool both reconstructs and fabricates, the fabrication determines the category.

Two kinds of case remain open. Whether established machine-learning functions such as denoising, upscaling and tracking require Assistive AI disclosure at all is the classification-scope part of [consultation question 1](#consultation). Hybrid restoration, where repair and newly originated content are hard to separate, and the treatment of automated subtitles and captions in a released version, are part of question 4.

---

## Descriptors

**Provisional, optional, and under consultation.** The descriptors were introduced in the August 2026 revision. The terms and definitions may change before v1.0. Where a record carries them, they go in the provisional `hpf_descriptors` array, which is not required.

Descriptors add factual context about the type of AI output present in the finished work. They never determine or change the classification and carry no threshold. More than one descriptor may apply where each records a distinct fact. `altered_performance` may be recorded on an Assistive AI or a Generative AI production. Every other descriptor applies only to Generative AI. None applies to No AI Used.

| Descriptor | Applies to | What it indicates |
|---|---|---|
| Altered performance (`altered_performance`) | Assistive or Generative AI | AI was used to modify a captured or recorded performance by an identifiable person in the finished production. The classification still depends on whether the AI processed captured human material or originated new content. |
| Digital replica (`digital_replica`) | Generative AI | AI was used to generate a representation of an identifiable person present in the finished production. |
| Synthetic performance (`synthetic_performance`) | Generative AI | AI was used to generate performance content that does not represent an identifiable person. |
| Generated voice (`generated_voice`) | Generative AI | AI was used to generate spoken or vocal content present in the finished production. It is a modality descriptor: use it alongside Digital replica or Synthetic performance where generated spoken or vocal content is involved. |
| Generated writing (`generated_writing`) | Generative AI | AI was used to generate written content embodied in the finished production. Development-only text not reflected in the finished production is out of scope. |
| Generated music (`generated_music`) | Generative AI | AI was used to generate music present in the finished production. |
| Generated visual content (`generated_visual_content`) | Generative AI | AI was used to generate visual content present in the finished production. This term is provisional and should be tested for breadth and for how it is used alongside other descriptors. |

**Worked descriptor examples**

| What happened | Classification and descriptors |
|---|---|
| Cosmetic AI de-ageing of a performance captured in full. | Assistive AI, Altered performance |
| AI-generated speech representing an identifiable actor, inserted into footage of their captured performance. | Generative AI, Digital replica, Generated voice, Altered performance |
| A wholly generated performer who does not represent an identifiable person. | Generative AI, Synthetic performance |
| A wholly generated fictional narrator. | Generative AI, Synthetic performance, Generated voice |

In the second example each descriptor records a different fact: Digital replica, that the generated material represents an identifiable person; Generated voice, that spoken content was generated; Altered performance, that a performance the actor gave on camera was modified. Generated writing spoken by a human actor in the usual way is different: it is Generated writing, not Generated voice or Digital replica.

Descriptors are factual provenance terms. Where a descriptor resembles a term in a collective agreement or contract, it takes its meaning from this standard alone. Descriptors do not state whether consent was obtained or whether rights, contractual or collective-agreement requirements were met, and they do not replace contracts, releases, consent records or chain-of-title documentation. [Consultation questions 2 and 3](#consultation) ask whether the definitions, examples and combination guidance allow consistent use.

---

## Scope

This taxonomy covers AI output reflected in the named finished version as distributed or exhibited, from development through to post-production.

AI used only in development, administration, production management or ideation, and unused concept material, are outside the finished-work record where no AI output reached or is embodied in the named finished version. This does not prevent a No AI Used declaration. Development-stage AI is in scope where its output is embodied in the finished version, for example generated dialogue performed in the final film, or pitch visuals reused as a title sequence. Influence alone is not incorporation. Human modification of an AI output does not by itself answer whether that output reached the finished version; the question is what, if anything, was incorporated into the version being declared.

**In scope**

- AI output from development, pre-production, principal photography and post-production that is present or embodied in the released version a declaration covers
- AI output supplied by the production company, a co-producer or a third-party contractor

**Out of scope**

- Marketing and promotion: posters, trailers, and social media assets
- Distribution materials: sales decks, EPKs, festival submissions, and audience-facing promotional content
- Basic automation in standard long-standing industry use: loudness normalisation, timecode tools, spell-check
- Development, administration, production management and ideation AI, and unused concept material, where no AI output reached or is embodied in the named finished version

AI used to make marketing or distribution materials is outside scope unless its output is also incorporated into the finished film or programme.

The production company or lead producer records one classification for the finished production, using the highest applicable category. Who produced a given element does not change the classification.

Rights, consent, contracts, insurance and legal compliance remain outside HPF. Organisations address them through their own processes. HPF does not assess the licensing of AI training data.

---

## Edge cases

These cases need judgement or remain open. The test is the same in each: is AI output present in the finished work, and did the AI originate it or process human-created material?

### Archival and found footage

AI restoration performed on the footage processes existing human-created material, so it is `assistive_ai`, subject to the open questions in [The reconstruction test](#the-reconstruction-test). Where a third-party archive performed it before the footage was licensed and the producer cannot establish what was done, the treatment is under consultation.

### Restored and re-released versions

A restored or remastered edition that changes the released picture or sound is a later released version and has its own declaration. AI processing or reconstruction of supplied footage is an Assistive use, subject to the open questions about processing functions. The version's overall classification depends on all in-scope AI output it contains, including output retained from the original version.

### Re-edits and director's cuts

A director's cut, extended edition, revised edit or other re-edit released after the original is a later released version with its own declaration, as set out in [Released versions and declarations](#released-versions-and-declarations).

### Episodic and series content

How the taxonomy applies to episodic and series content is open for consultation. The provisional position is that classification applies per episode, with the highest category across any episode applying where a series is classified as a whole. Whether classification should be required at title, season or episode level, and how the released-version rule applies to episodes, seasons and series, are part of question 4.

### De-ageing: restorative or fabricated

De-ageing that adjusts or restores the captured appearance is reconstruction, so `assistive_ai`. Where AI fabricates part of a performance the performer did not give, including posthumous synthesis or dialogue replacement, it is `generative_ai`.

### Established machine-learning tools in VFX and animation

Many VFX and animation tools have used machine learning for years, for example denoising, upscaling, motion estimation, tracking, deep compositing, and rotoscoping assistance. Where such a tool processes footage or elements captured or created by human crew, it is not `generative_ai`. Whether these features should require `assistive_ai` disclosure, or sit with the routine automation outside scope, is not settled in v0.9.3: the classification-scope part of question 1 asks which, if any, should require disclosure, and its declaration-basis part asks how far enquiry should go where they are built into established software. Such a tool becomes `generative_ai` only where it originates new content that appears in the finished work.

### Animation

The test applies as for live action. AI processing or refining work created by animators is `assistive_ai`, subject to the open questions about established machine-learning functions. AI originating characters, environments, or sequences that appear in the finished work is `generative_ai`. Animation workflows where the relationship is harder to determine are part of question 4.

---

## The declaration

A declaration identifies the work, the released version it covers, the classification, the party making it, and the date it was made. It is signed by someone authorised to declare on behalf of the production. Where in-scope AI use is present, it carries a short factual summary of what the AI did and what output reached the finished work. Tool names can support the summary but do not replace it.

**Basis of reliance.** The disclosure rests on the producer's signed declaration, which sits alongside other producer representations in existing deal, delivery and other production paperwork. HPF does not verify the declaration or audit the production's tools or workflows. A declaration is not by itself a contractual warranty. Parties may incorporate the classification into their representations and warranties, and any remedy for misrepresentation is then a matter for their contract.

**Existing productions.** An authorised party may make a declaration for a production already released, where it can establish the relevant facts. The declaration carries the date it was made, not the release date. No one may infer a classification from a release date, detection output or incomplete catalogue information, or apply one in bulk across a catalogue. Where no declaration has been made, there is no record. An absent declaration establishes neither that AI was used nor that it was not used.

**Audience disclosure.** HPF records provenance information that can be shown to audiences. HPF encourages platforms and distributors to display the classification but does not require display or prescribe a label, format or placement.

Technical implementation, including how a record is stored and carried, is in [INTEGRATION.md](INTEGRATION.md).

---

## Relationship to regulation

HPF is a voluntary disclosure standard for AI output in finished film and television. An HPF declaration does not establish legal compliance or replace obligations under applicable law.

---

## Glossary and definitions

Definitions of terms used around AI disclosure in film. Terms defined earlier in this document are not restated.

### Different kinds of transparency

- **Regulatory transparency**: disclosure or marking required by law, such as Article 50 of the EU AI Act.
- **Technical provenance**: records of a digital asset's origin and history. Content Credentials can carry such records. Watermarking and fingerprinting can support identification or link content to records, but do not necessarily provide a provenance history themselves.
- **Consent and compensation**: rights mechanisms, such as collective-bargaining provisions, licences and permissions, that govern whether material, performances or data may be used and on what terms.
- **Production disclosure**: information about how a finished work was made, supplied by the party responsible for it. HPF provides this form of production disclosure. The producer's signed declaration is the record, and existing deal, delivery and other production paperwork is the route by which it reaches the organisations and audiences that use it.

HPF complements technical provenance and regulatory disclosure and does not replace them. It does not determine consent, compensation or underlying rights.

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

Where recognised definitions for these terms exist or emerge in the creative sectors, HPF will seek to align with them rather than create a competing vocabulary. The glossary remains under consultation. Reference to an external standard, technology, organisation or regulatory framework does not imply coordination with or endorsement by that body.

---

## Consultation

v0.9 is a draft for consultation. Send feedback to contact@humanprovenance.film or through the GitHub repository (issues or pull requests). Responses received before 31 October 2026 will inform the v1.0 revision. Performers, casting professionals, agents, union representatives and business-affairs practitioners are invited to help test whether the factual vocabulary is clear and usable.

### Current v0.9.3 rules

v0.9.3 establishes the current consultation-draft rules below. Like all pre-v1 provisions, they remain subject to evidence received during consultation, but they are not listed as unresolved questions.

- No percentage threshold: the highest applicable category applies to any AI output present, however small ([Classification test](#classification-test)).
- More than one descriptor may apply where each provides distinct factual information ([Descriptors](#descriptors)).
- One declaration covers one released version, and a later released version has its own declaration ([Released versions and declarations](#released-versions-and-declarations)).

### Outside the consultation

- HPF does not determine contractual permission, consent, compensation, rights, or legal compliance, although its terminology may be useful in conversations between producers, performers, representatives and other parties.
- HPF does not currently prescribe an audience-facing label, display format, or placement rule.

### Remaining questions for consultation

1. **Reasonable enquiry and established machine learning.** This question has two parts. Neither is settled in v0.9.3, and concrete workflow examples are welcome for both.
   - **Declaration basis:** Is reasonable enquiry the appropriate basis for a No AI Used declaration where AI functions may be built into software, enabled by default, or difficult to identify? Reasonable enquiry is not a current HPF requirement.
   - **Classification scope:** Which established machine-learning functions, if any, should require Assistive AI disclosure when they process picture or sound retained in the released version?
2. **Performance-related descriptors.** Are the current performance descriptors sufficiently clear for altered performances, digital replicas, synthetic performances, and combined uses? What examples are needed to support consistent application? This includes when Generated Visual Content should be used alongside Altered performance, Digital replica, Synthetic performance, or other descriptors.
3. **Human contribution to synthetic performance.** How should HPF describe cases where human performance inputs contribute to a synthetic performance without representing the performer as an identifiable person? This may be resolved through guidance, factual-summary practice or worked examples; a new descriptor is not assumed.
4. **Complex finished-work and version cases.** What further guidance is needed for transformed output, intermediate VFX control data, restoration and reconstruction, localisation, subtitles and captions, episodic releases, animation workflows, and other cases where the relationship between AI output and the released version is difficult to determine? How HPF should treat AI-generated or AI-segmented mattes, masks, or similar control data that shape a delivered composite is not settled in v0.9.3. Questions about episodic works, selectable subtitles and captions, dubbing and other localisation, and the boundary between a technical delivery variation and a substantively different released version concern applying the released-version rule, not reconsidering it.
5. **Implementation.** What information can producers reasonably establish when preparing a declaration, and what information is useful to organisations receiving it?

If a real production use does not fit the current categories, we want to hear about it.

Earlier drafts asked some of these questions in other words and numbered them differently. The wording as asked is preserved in each release tag, and the version history in [GOVERNANCE.md](GOVERNANCE.md#version-history) records where each now sits.

---

## Licence

CC BY 4.0. See [LICENSE.md](LICENSE.md).

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
