# HPF AI Disclosure Taxonomy

**Version 0.9.2, draft for consultation**
Updated August 2026. Consultation closes 31 October 2026.

A free, open standard for declaring AI output present in finished film and television productions. A producer makes one signed declaration using three categories. It travels with the production in chain-of-title and delivery documentation, so every recipient reads the same thing.

This document sets out HPF's three-category classification, the producer declaration process and the two machine-readable fields. It does not certify productions, audit workflows, or determine consent, rights or regulatory compliance.

---

## Organising principle

> Is AI output present in the finished film, and did it process human work or originate new content?

The producer answers two questions of fact. First, is any AI output present in the finished film as distributed? If not, the film is No AI Used. If it is, did the AI process human-created material (Assistive AI) or originate new content that appears in the finished work (Generative AI)? The producer signs the declaration and is responsible for its accuracy. Where the parties choose to, the classification can be incorporated into the representations and warranties in their agreement. The test is simply how the producer reaches an answer they can stand behind.

HPF classifies AI output reflected in the finished production an audience sees or hears, and it classifies how AI is used, not the underlying model or product: the same AI system can support an Assistive use in one production and a Generative use in another.

### Key terms

**Artificial intelligence**, for the purposes of this taxonomy, means software systems that use machine learning, neural networks, or similar techniques trained on data to generate, synthesise, enhance, or analyse content, as distinct from deterministic software that applies fixed rules or algorithms without learned models. Where a tool offers both conventional and AI-powered modes, only the AI-powered mode's output is in scope.

**AI tool** means any software that uses artificial intelligence, as defined above, to produce, modify or optimise content. Standard digital tools that do not use it are not AI tools.

**Finished production**, also called the finished film or the finished work, means the production as distributed or exhibited, including every version released after the original declaration was made. This taxonomy covers film and television, and uses finished production, finished film and finished work to mean the same thing.

---

## Classification test

For the finished film as distributed:

1. Is any AI output present in the finished film? If not: `no_ai`.
2. If yes: did the AI process human-created material, or originate new content that appears in the finished work?
3. Processing human material: `assistive_ai`. Originating new content: `generative_ai`.

The test turns on what is in the finished film, not on whether a human would otherwise have performed the function. AI-generated content that appears in the finished work is `generative_ai` whether or not a human could have produced it.

A production is classified at the highest category applicable to any element. A film with both AI noise reduction (`assistive_ai`) and an AI-generated score (`generative_ai`) is classified as `generative_ai`, with both uses described in the declaration.

Where the answer is unknown or the records are incomplete, the classification is unresolved. Missing, uncertain or absent information is never No AI Used. A `no_ai` declaration records that no in-scope AI output was found, not that nothing is known.

---

## Categories

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

These values correspond directly to `hpf_classification` in [schema.json](schema.json).

A record carries two fields: `hpf_standard_version`, which names the version of this taxonomy that was applied, and `hpf_classification`. The version field was named `hpf_taxonomy_version` before this revision.

---

### `no_ai`: No AI Used

No AI output is present in the finished film. No AI tool produced any element of the finished work as distributed. AI used only in development, leaving no trace in the finished film, is out of scope and does not prevent a No AI Used declaration.

Basic computational automation in standard long-standing industry use (loudness normalisation, timecode tools, spell-check) does not count as AI use.

**Examples:** editing, colour grading, compositing, sound design, music recording, and visual effects performed without AI tools.

---

### `assistive_ai`: Assistive AI

AI output is present in the finished film, but the AI processed or optimised material created by human crew rather than originating new content. A human held the creative or production role; the AI worked from their material.

**Examples:** AI-assisted colour grading; noise reduction; automated subtitling and captioning; de-flickering; archival restoration; AI-assisted sound clean-up; automated camera tracking in VFX prep. Cosmetic de-ageing of a performance captured in full, where AI refines appearance without rebuilding or generating any part of the performance. In animation: AI used to clean up or optimise frames created by animators.

**Not `assistive_ai`:** any AI output that the AI originated rather than deriving from human-created material. If the AI made new content that appears in the finished film, the classification is `generative_ai` regardless of how the tool is marketed.

AI used solely in development that leaves no trace in the finished film does not require classification.

---

### `generative_ai`: Generative AI

AI originated content that appears in the finished film, rather than processing human-created material. The AI made new content rather than refining work created by human crew. Where a tool both reconstructs supplied material and fabricates content that was never captured, the fabrication decides the category: see the reconstruction test.

If any qualifying AI-originated content appears in the finished work, the production is `generative_ai` regardless of duration, prominence, or proportion. There is no materiality or de minimis exception. A film using human-shot footage alongside a single AI-generated environment is `generative_ai` overall.

**Examples:** AI-generated backgrounds, environments, crowd scenes, or set extensions; AI-written screenplay elements present in the finished film; synthesised or cloned actor performances; AI voice cloning; AI-generated music present in the finished film; de-ageing or posthumous synthesis that fabricates part of a performance rather than refining one fully captured on set. In animation: AI-generated characters, environments, or sequences present in the finished work.

**Not `generative_ai`:** cosmetic enhancement of a performance that was captured in full (minor de-ageing that does not fabricate part of a performance) is `assistive_ai`. AI used in development only, where no AI-generated content appears in the finished film, does not require `generative_ai` classification. Established machine-learning tools that process human-created material, such as denoising, upscaling, or tracking, are not `generative_ai`; whether they require `assistive_ai` disclosure is an open question for consultation.

---

## The reconstruction test

Some AI tools operate on footage, audio, or images that already exist rather than producing content from a prompt. For these, classification turns on whether the tool reconstructs content already present or fabricates content that is not.

Reconstruction restores, cleans, or repairs content that was captured or created by a human: noise reduction, de-flickering, artefact removal, upscaling that sharpens detail already in the source, format conversion. The output is the same content in better condition. This is `assistive_ai`.

Fabrication invents content that was never captured or created: painting in a background revealed by removing an object, generating frames or detail with no source, synthesising a performance element the performer did not give. The output contains material that did not exist before. This is `generative_ai`.

Modern AI systems may technically synthesise pixels, frames, or audio while restoring or enhancing existing material. Classification turns on the HPF distinction between processing or reconstructing supplied material and originating new content for the finished production, not merely on whether the software technically generated data.

The label a vendor applies does not decide the category. Where a tool both reconstructs and fabricates, the fabrication determines the category.

---

## Descriptors

**Provisional. Under consultation.** New in the August 2026 revision and not yet part of the taxonomy. The terms and definitions below may change before v1.0.

Descriptors add factual context to a classification. They work like the short descriptors shown alongside a film rating: they identify the type or types of AI-generated or AI-modified content present. They never determine or change the classification, they carry no threshold, and a descriptor never converts an Assistive AI production into Generative AI. Where a record carries them they go in the provisional `hpf_descriptors` array, which is not required.

`altered_performance` may be recorded on an Assistive AI or a Generative AI production. Every other descriptor applies only to Generative AI. None applies to No AI Used. More than one may apply to the same production.

| Descriptor | Applies to | What it indicates |
|---|---|---|
| Altered performance (`altered_performance`) | Assistive or Generative AI | AI was used to modify a performance by an identifiable person present in the finished production. It records that a captured or recorded performance was modified. The classification still depends on whether the AI processed captured human material or originated new content. |
| Digital replica (`digital_replica`) | Generative AI | AI was used to generate a representation of an identifiable person present in the finished production. |
| Synthetic performance (`synthetic_performance`) | Generative AI | AI was used to generate performance content that does not represent an identifiable person. |
| Generated voice (`generated_voice`) | Generative AI | AI was used to generate spoken or vocal content present in the finished production. It is a modality descriptor: use it alongside Digital replica or Synthetic performance where generated spoken or vocal content is involved. |
| Generated writing (`generated_writing`) | Generative AI | AI was used to generate written content embodied in the finished production. Development-only text not reflected in the finished production is out of scope. |
| Generated music (`generated_music`) | Generative AI | AI was used to generate music present in the finished production. |
| Generated visual content (`generated_visual_content`) | Generative AI | AI was used to generate visual content present in the finished production. This term is provisional and should be tested for breadth and overlap. |

**Worked descriptor examples**

| What happened | Classification and descriptors |
|---|---|
| Cosmetic AI de-ageing of a performance captured in full. | Assistive AI, Altered performance |
| An identifiable actor made to speak dialogue they did not record. | Generative AI, Digital replica, Generated voice. Altered performance also applies where the generated material modifies captured footage. |
| A wholly generated performer who does not represent an identifiable person. | Generative AI, Synthetic performance |
| A wholly generated fictional narrator. | Generative AI, Synthetic performance, Generated voice |

Descriptors are factual provenance terms, not contractual definitions. Synthetic performance does not take its meaning from "synthetic performer", "synthetic" or any similar term in a SAG-AFTRA, Equity or other collective agreement.

Descriptors identify what is present in the finished production. They do not state whether consent was obtained. They do not indicate whether rights or contractual requirements were satisfied. They do not establish compliance with a collective agreement. They do not replace contracts, releases, consent records or chain-of-title documentation.

This is a substantive consultation update, not an illustrative example set. We welcome feedback on whether these terms are useful and distinct, where they overlap, and what is missing.

---

## Scope

This taxonomy covers AI output reflected in the finished film as distributed and exhibited, from development through to post-production. AI used only in development, administration, production management, or ideation, and unused concept material, is out of scope where it leaves no output in the finished film. Development-stage AI is in scope where its output is embodied in the finished film, for example generated screenplay dialogue performed in the final film.

**In scope**

- Development, pre-production, and principal photography
- Post-production: editing, colour, sound, VFX, and music
- All co-producers and third-party contractors (aggregated by the production company or lead producer)
- Every distributed or exhibited version of the film

**Out of scope**

- Marketing and promotion: posters, trailers, and social media assets
- Distribution materials: sales decks, EPKs, festival submissions, and audience-facing promotional content
- Basic automation in standard long-standing industry use: loudness normalisation, timecode tools, spell-check
- Development, administration, production management, and ideation AI, and unused concept material, that leaves no output in the finished film

The production company or lead producer must use the highest category applicable across all co-producers and contractors. This prevents co-production structures from obscuring AI use that would otherwise require disclosure.

Where classification is incorporated into a deal or licensing agreement as a producer representation, misclassification is a matter of contractual liability. This places the standard within existing contractual mechanisms rather than requiring new regulatory infrastructure.

---

## Edge cases

The following situations require case-by-case judgement. The classification test in each case is the same: is AI output present in the finished work, and did the AI originate it or process human-created material?

### Archival and found footage

If AI restoration was performed on the footage, the AI processed existing human-created material, so it is `assistive_ai`. If a third-party archive performed it before the footage was licensed and the producer cannot establish what was done: under active consultation.

### Restored and re-released versions

The classification applies to the version being distributed. A restored version using AI tools to process the existing footage is `assistive_ai` for that version, regardless of how the original was made.

### AI used in development only

If AI tools were used in development but no AI-generated content appears in the finished film, no classification is required.

AI-powered pre-production tools, such as script analysis, financial modelling, scheduling, and pitch deck generation, are out of scope provided their outputs do not appear in the finished film. Where a pre-production AI output is subsequently used in the finished work (for example, AI-generated pitch visuals repurposed as a title sequence or interstitial), that use is in scope and must be classified.

### Live-action with AI sequences

A live-action film with AI-generated title sequences, interstitials, or stylised inserts is `generative_ai` overall, because AI-generated content is present in the finished work.

### Episodic and series content

How the taxonomy applies to episodic and series content is an open question for the consultation. The provisional position is that classification applies per episode, with the highest category used across any episode applying where a series is classified as a whole. Whether classification should be required at the title, season, or episode level individually is unresolved. Input is welcome.

### Re-edits and director's cuts

If a new version is released after the original declaration was made, and that version contains AI-generated content not present in the original, the producer must notify all parties who received the original declaration and issue updated declarations.

### De-ageing: restorative vs. fabricated

De-ageing that adjusts or restores the captured appearance is reconstruction, so `assistive_ai`. Where AI fabricates part of a performance the performer did not give, including posthumous synthesis or dialogue replacement, it is `generative_ai`.

### Established machine-learning tools in VFX and animation

Many VFX and animation tools have used machine learning for years, for example denoising, upscaling, motion estimation, tracking, deep compositing, and rotoscoping assistance. Where such a tool processes footage or elements captured or created by human crew, it is not `generative_ai`. Whether these established, ubiquitous features should require `assistive_ai` disclosure, or sit with the routine automation the taxonomy treats as out of scope, is an open question for consultation. It becomes `generative_ai` only where it originates new content that appears in the finished work.

### Animation

The test applies in the same way as for live-action. AI processing or refining work created by animators is `assistive_ai`. AI originating characters, environments, or sequences that appear in the finished work is `generative_ai`.

---

## Regulatory scope

HPF covers production-level AI disclosure: what AI was used in making the finished work, declared by the producer. It does not address tool-level obligations. Where a production uses an AI system to generate content, obligations may fall elsewhere under applicable regulation. Article 50(2) of the EU AI Act places a machine-readable marking obligation on the provider of the AI system, not on the provider of an underlying general-purpose AI model as such. Article 50(4) places a disclosure obligation on the deployer of a system that generates or manipulates deepfake content, which in a production context is often the production itself, and where the content forms part of an evidently artistic, creative, satirical, fictional or analogous work that obligation is limited to disclosing the existence of the content. HPF and those obligations operate in parallel and are not substitutes for each other.

**What a declaration identifies:** the work, the version, cut, episode or edition it covers, the classification, the party making it, and the date it was made. It is signed by someone authorised to declare on behalf of the production. Where in-scope AI use is present it carries a short factual summary of what the AI did and what output reached the finished work. Tool names are useful supporting information and do not replace the summary.

**Basis of reliance:** HPF's disclosure model is based on the producer's signed declaration. A recipient may rely on that declaration in the same way they rely on other producer representations in chain of title documentation. HPF does not independently verify the accuracy of the declaration or audit the production's tools or workflows. An HPF declaration is not by itself a contractual warranty. Parties may incorporate the classification into their representations and warranties where they choose to, and any remedy for misrepresentation is then a matter for the contract between them.

**Audience disclosure:** HPF governs how classification travels through the distribution chain, from producer to platform. HPF encourages platforms and distributors to display the classification to audiences, and does not require it or mandate how they do so. Display standards are an open question for the consultation; the framework's open questions list addresses this explicitly. Productions and platforms seeking to make audience-facing disclosure are encouraged to engage with the consultation on what display standards should require.

**HPF and regulation:** HPF is a proposed voluntary industry standard, not a regulatory-compliance mechanism, and is not designed to satisfy any regulatory framework. It does not establish regulatory compliance. Its aim is commercial, and any regulatory usefulness is incidental. The classification applies wherever a production is made or distributed; producers and platforms should take their own legal advice on how it interacts with their obligations.

The framework applies to productions that adopt it from the point of adoption forward. An authorised party may also make a declaration for a production already released, where it can establish the relevant facts, and that declaration carries the date it was made rather than the release date. What nobody may do is infer a classification for a title: not from a release date, not from detection output, not from incomplete catalogue information, and not by applying a value in bulk across a catalogue. Where no declaration has been made there is no record, and an absent record should not be read as an absence of AI use.

---

## Glossary and definitions

Definitions of terms used around AI disclosure in film. Terms defined in the standard itself, including the three categories, the organising principle, the distinction between reconstruction and fabrication, and *finished work*, are not restated here; see the Organising principle, Key terms and Categories sections.

### Different kinds of transparency

Several distinct systems are often grouped together as “AI transparency”. They do different jobs:

- **Regulatory transparency** concerns disclosure or marking required by law. Article 50 of the EU AI Act, for example, includes requirements concerning machine-readable marking of certain AI-generated or manipulated outputs and disclosure of deepfakes, with specific treatment for evidently artistic, creative, satirical, fictional or analogous works.
- **Technical provenance** records information about the origin and history of a digital asset. Content Credentials, watermarking and fingerprinting can all contribute to this in different ways. They can help establish where an asset came from, how it has changed, or whether it matches a known reference. They do not, by themselves, establish that every claim about how a film was made is true.
- **Consent and compensation** govern whether material, performances or data may be used, and on what terms. Collective-bargaining provisions, licences and permissions belong here. These are rights mechanisms rather than disclosure standards.
- **Commercial disclosure** provides information about how a work was made to a party that can rely on it in a transaction. HPF operates at this layer: the producer makes a signed declaration that can travel with the film's chain of title. Where the parties incorporate it into their agreement, an inaccurate declaration can carry contractual consequences.

HPF is a commercial disclosure standard. It is intended to complement technical provenance and regulatory disclosure, not replace them, and it does not determine consent, compensation or underlying rights.

### How information is recorded

| Term | Meaning |
|---|---|
| Metadata | Information stored with a digital asset rather than forming part of the picture or sound itself. Examples include camera settings, timecode, software information and edit history. Ordinary metadata can be altered and is often lost when files are transcoded, exported or uploaded. Its evidential value therefore depends on how it was created and protected. |
| Provenance | A documented history of a digital asset: where it came from, what sources contributed to it, what happened to it, and who made the relevant claims. Provenance can provide evidence about origin and process. It does not necessarily establish that the record is complete, that the content depicts something true, or that the necessary rights and permissions were obtained. |
| C2PA and Content Credentials | **C2PA** is an open technical standard for recording signed provenance claims about digital content and validating their integrity and signer. **Content Credentials** is the commonly used presentation and implementation of this approach. C2PA manifests can contain cryptographically signed claims about an asset and its history, allowing a verifier to identify the signer and detect whether protected information has subsequently been altered. A valid signature establishes the integrity and source of the signed claims, not the truth of every claim they contain. C2PA 2.4 includes a standard assertion, `c2pa.ai-disclosure`, which carries model-level information about a generation step and is different information from a production-level HPF classification. |
| Ingredient | In C2PA terminology, an asset used in the creation of another asset. A composite asset may therefore have relationships to multiple ingredients and their associated provenance. This matters for film because a finished work combines picture, sound, music, VFX and other material from many sources. Provenance attached to an individual ingredient, such as a camera capture, does not by itself describe how the finished production was made. |
| Watermarking | Information embedded in the content itself rather than stored only as accompanying metadata. A watermark may be visible to a viewer or imperceptible and detectable by software. Depending on its design and the medium, it may remain detectable after transformations such as compression, re-encoding or cropping. Its function is to provide a detectable signal; what can be inferred from that signal depends on the watermarking system and how it is used. |
| Fingerprinting | A representation calculated from the content and compared with records held elsewhere, rather than information added to the asset itself. YouTube Content ID is a familiar example. Fingerprinting is principally a matching mechanism: it can identify content that corresponds to a known reference without requiring the person distributing the copy to attach provenance information to it. |
| Machine-readable marking | A marking intended to allow AI-generated or manipulated content to be identified by automated means. Article 50(2) of the EU AI Act requires providers of AI systems, including general-purpose AI systems, that generate synthetic audio, image, video or text to ensure the outputs are marked in a machine-readable format and detectable as artificially generated or manipulated; that obligation falls on the provider of the AI system, not on the provider of an underlying general-purpose AI model as such. Article 50(4) separately places a disclosure obligation on deployers of systems that generate or manipulate deepfakes, and where the content forms part of an evidently artistic, creative, satirical, fictional or analogous work that obligation is limited to disclosing the existence of the content. |

### How information is communicated

| Term | Meaning |
|---|---|
| Labelling | A statement presented to an audience about the nature or production of a work, for example through a caption, icon or end card. A label communicates a claim. How much confidence can be placed in it depends on the process and evidence behind that claim. |
| Disclosure | Providing defined information to a defined recipient. An audience label is one form of disclosure. A declaration supplied to a distributor, financier or other counterparty is another. The information, level of detail and consequences of an inaccurate disclosure can differ according to its purpose and recipient. |
| Self-declaration and certification | A **self-declaration** is a claim made by the person or organisation responsible for the work. **Certification** involves an independent body assessing conformity with specified requirements, normally under a defined certification scheme. The distinction matters because a self-declaration may use a standard without the standards body independently verifying the individual work. HPF uses self-declaration, not certification. |

### What it means commercially

| Term | Meaning |
|---|---|
| Warranted declaration | A statement made contractually by a party that accepts responsibility for its accuracy. Its force comes from the contractual consequences available if the statement proves false, rather than from an independent technical verification of the claim. An HPF declaration is not by itself a contractual warranty. HPF is designed so that parties can incorporate AI-use disclosure into their representations and warranties where they choose to, alongside other producer representations. |
| Chain of title | The collection of agreements, assignments, licences and other records used to establish the rights necessary to make and exploit a film. It is routinely examined in financing, distribution, acquisition and insurance. Technical provenance may contribute useful evidence, but it does not replace the legal documentation establishing those rights. |
| Clearance | The process of identifying third-party material or rights used in a production and obtaining any permissions required for their use. This may include music, artwork, trademarks, likenesses and underlying literary or other rights. Provenance information can help identify source material, but identifying a source and having permission to use it are separate questions. |
| Errors and omissions insurance | Insurance covering specified legal liabilities arising from the content and exploitation of a production, commonly including risks such as copyright infringement, invasion of privacy and defamation. E&O review commonly involves evidence of rights, permissions and chain of title. Provenance information may support that documentation, but it does not itself establish that the relevant rights have been cleared. |

### Alignment with existing definitions

Where recognised definitions for these terms already exist, or emerge, within the creative sectors, HPF will seek to align with them rather than create a competing vocabulary. HPF is not intended to lead a separate terminology-standardisation effort. These definitions exist to make the disclosure standard usable and to explain how its terms relate to adjacent technical, legal and commercial systems.

The glossary remains under consultation and these definitions are used for the purposes of HPF until v1.0. Reference to an external standard, technology, organisation or regulatory framework does not imply coordination with or endorsement by that body.

---

## Consultation

v0.9 is a draft for consultation. Feedback can be submitted to contact@humanprovenance.film or via the GitHub repository (issues or pull requests). Responses received before 31 October 2026 will inform the v1.0 revision.

The questions we most want input on:

1. Does the present-and-originated principle, and the three categories it produces, capture the distinction that matters to your organisation? Is anything missing, such as a fourth category?
2. Is the declaration mechanism workable in your part of the industry, and if not, what would need to change? In particular, for a `no_ai` declaration, software now switches AI features on by default, so would a "reasonable enquiry" standard, the same one used for other chain-of-title warranties, be a fair basis?
3. Marketing materials, such as trailers, posters, and social cuts, are currently out of scope. How urgent is it to bring them in?
4. For platforms, broadcasters, and distributors: would you use the `assistive_ai` classification, and would you surface it to audiences?
5. Which ways of showing the disclosure are practical and clear, from end credits to delivery metadata to a platform label, and what would sit alongside your regulatory obligations?
6. Does the chain-of-title mechanism work outside the UK and US, where co-production paperwork differs? Are there regulatory, contractual, or collective-bargaining frameworks HPF needs to account for in v1.0?
7. Should established, ubiquitous machine-learning features that process human-created material, such as denoising, upscaling, and tracking, require `assistive_ai` disclosure, or should they sit with the routine automation the taxonomy already treats as out of scope?
8. An objective measure of how much generative content a production contains has deliberately been left out: the category does not change with extent, and a small use is described in the declaration instead. Is that the right call, and if not, what observable facts could a measure be built from without adding significant work for producers?

For technical implementation guidance: [INTEGRATION.md](INTEGRATION.md).

---

## Licence

CC BY 4.0. See [LICENSE.md](LICENSE.md).

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
