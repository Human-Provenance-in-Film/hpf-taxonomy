# HPF AI Disclosure Taxonomy

**Version 0.9, draft for consultation**
Consultation closes 31 October 2026.

---

## Organising principle

> Is AI output present in the finished film, and did it process human work or originate new content?

The producer answers two questions of fact. First, is any AI output present in the finished film as distributed? If not, the film is No AI Used. If it is, did the AI process human-created material (Assistive AI) or originate new content that appears in the finished work (Generative AI)? The legal weight sits in the warranty the producer signs; the test is simply how they reach an answer they can stand behind.

HPF classifies AI output reflected in the finished production an audience sees or hears, and it classifies how AI is used, not the underlying model or product: the same AI system can support an Assistive use in one production and a Generative use in another.

For the purposes of this taxonomy, artificial intelligence is defined in the `no_ai` category below.

---

## Classification test

For the finished film as distributed:

1. Is any AI output present in the finished film? If not: `no_ai`.
2. If yes: did the AI process human-created material, or originate new content that appears in the finished work?
3. Processing human material: `assistive_ai`. Originating new content: `generative_ai`.

The test turns on what is in the finished film, not on whether a human would otherwise have performed the function. AI-generated content that appears in the finished work is `generative_ai` whether or not a human could have produced it.

A production is classified at the highest category applicable to any element. A film with both AI noise reduction (`assistive_ai`) and an AI-generated score (`generative_ai`) is classified as `generative_ai`, with both uses described in the declaration.

---

## Categories

| `hpf_classification` | Label |
|---|---|
| `no_ai` | No AI Used |
| `assistive_ai` | Assistive AI |
| `generative_ai` | Generative AI |

These values correspond directly to `hpf_classification` in [schema.json](schema.json).

---

### `no_ai`: No AI Used

No AI output is present in the finished film. No AI tool produced any element of the finished work as distributed. AI used only in development, leaving no trace in the finished film, is out of scope and does not prevent a No AI Used declaration.

Basic computational automation in standard long-standing industry use (loudness normalisation, timecode tools, spell-check) does not count as AI use.

For the purposes of this taxonomy, artificial intelligence means software systems that use machine learning, neural networks, or similar techniques trained on data to generate, synthesise, enhance, or analyse content, as distinct from deterministic software that applies fixed rules or algorithms without learned models. Where a tool offers both conventional and AI-powered modes, only the AI-powered mode's output is in scope.

**Examples:** editing, colour grading, compositing, sound design, music recording, and visual effects performed without AI tools.

---

### `assistive_ai`: Assistive AI

AI output is present in the finished film, but the AI processed or optimised material created by human crew rather than originating new content. A human held the creative or production role; the AI worked from their material.

**Examples:** AI-assisted colour grading; noise reduction; automated subtitling and captioning; de-flickering; archival restoration; AI-assisted sound clean-up; automated camera tracking in VFX prep. Cosmetic de-ageing of a performance captured in full, where AI refines appearance without rebuilding or generating any part of the performance. In animation: AI used to clean up or optimise frames created by animators.

**Not `assistive_ai`:** any AI output that the AI originated rather than deriving from human-created material. If the AI made new content that appears in the finished film, the classification is `generative_ai` regardless of how the tool is marketed.

AI used solely in development that leaves no trace in the finished film does not require classification.

---

### `generative_ai`: Generative AI

AI originated content that appears in the finished film, rather than processing human-created material. The AI made new content rather than refining work created by human crew.

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

## Generative AI descriptors

**Provisional. Under consultation.** New in the August 2026 revision and not yet part of the standard. The terms and definitions below may change before v1.0.

Descriptors apply only to productions already classified `generative_ai`. They work like the short descriptors shown alongside a film rating: they identify the type or types of generated content present, once a production is Generative AI. They do not determine classification, they carry no threshold, and they do not apply to Assistive AI.

| Descriptor | What it indicates |
|---|---|
| Synthetic performance | Generative AI was used to generate performance content present in the finished production. |
| Digital replica | Generative AI was used to generate a representation of an identifiable person present in the finished production. The descriptor does not indicate whether consent, rights, or contractual requirements were satisfied. |
| Generated writing | Generative AI was used to generate written content embodied in the finished production. Development-only text not reflected in the finished production is out of scope. |
| Generated music | Generative AI was used to generate music present in the finished production. |
| Generated visual content | Generative AI was used to generate visual content present in the finished production. This term is provisional and should be tested for breadth and overlap. |
| Generated voice | Generative AI was used to generate spoken or vocal content present in the finished production. This term is provisional and should be tested for overlap with Synthetic performance and Digital replica. |

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

HPF covers production-level AI disclosure: what AI was used in making the finished work, declared by the producer. It does not address tool-level obligations. Where a production uses a general-purpose AI model (GPAI) to generate content, the provider of that model may have independent disclosure obligations under applicable regulation, for example under Article 50 of the EU AI Act. HPF and tool-level obligations operate in parallel and are not substitutes for each other.

**Verification standard:** verification under HPF means reasonable commercial reliance on the producer's signed declaration, not a technical audit of the production's tools or workflows. This is the same standard that applies to all producer representations in chain of title documentation. The remedy for misrepresentation is a matter for the contract between the parties. HPF does not operate an independent verification or audit function.

**Audience disclosure:** HPF governs how classification travels through the distribution chain, from producer to platform. It does not currently mandate how platforms surface classification to audiences. Display standards are an open question for the consultation; the framework's open questions list addresses this explicitly. Productions and platforms seeking to make audience-facing disclosure are encouraged to engage with the consultation on what display standards should require.

**HPF and regulation:** HPF is a market standard, not a regulatory-compliance mechanism, and is not designed to satisfy any regulatory framework. Its aim is commercial, and any regulatory usefulness is incidental. The classification applies wherever a production is made or distributed; producers and platforms should take their own legal advice on how it interacts with their obligations.

The framework is prospective in nature. It applies to productions that adopt it from the point of adoption forward. It does not provide a mechanism for retroactive disclosure of historical catalogue content, and absent values for unclassified historical content should not be read as an absence of AI use.

---

## Glossary and alignment

Definitions of terms used around AI disclosure in film. Terms defined in the standard itself, such as the three categories, the organising principle, the reconstruction and fabrication distinction, and finished work, are not restated here; see the Organising principle and Categories sections.

**Kinds of transparency.** These terms serve several purposes that are easy to conflate:

- **Regulatory** transparency is a legal marking and disclosure obligation aimed at the viewer, such as the machine-readable marking and audience disclosure required under Article 50 of the EU AI Act, with a lighter duty for artistic and fictional works. It asks whether content is passing as something it is not.
- **Technical** provenance is information carried with or alongside the file, such as Content Credentials, watermarking, or fingerprinting. It can help establish origin and history and show whether a file has changed, but not whether a claim is true. Because a film is composite, built from many ingredients across picture, sound, music, and VFX, signing a single capture says little about how the whole production was made.
- **Consent and compensation** mechanisms, such as collective-bargaining provisions for performers and licensing protocols for training data, govern permission and payment. They are not disclosure standards.
- **Commercial** disclosure states how a work was made, to a counterparty who can act on it. HPF sits here: a producer's warranted declaration recorded in chain of title, with contractual remedy if it proves false.

HPF is a commercial disclosure standard. It complements the other layers but does not replace them or perform their functions, and it does not touch consent or compensation.

### How content is recorded

| Term | Meaning |
|---|---|
| Metadata | Information attached to a file, separate from the picture or sound itself, such as camera settings, timecode, software used, and edit history. Unsigned metadata can be written or altered by anyone with the file, and is routinely stripped when content is transcoded or uploaded to a platform. It establishes nothing on its own. |
| Provenance | A record of how a piece of content came to exist: what created it, what source material went into it, what was done to it afterwards, and who asserts each of those claims. It establishes a documented history that someone has vouched for. It does not establish that the history is complete, that the content is accurate, or that anyone holds rights in it. |
| Content Credentials and C2PA | C2PA is the technical specification; Content Credentials is the name commonly used for provenance data recorded under it. The data sits in a cryptographically signed manifest, so a checker can tell which identity signed the claims and whether the file has changed since. The signature verifies who made the assertions, not whether the assertions are true. |
| Ingredient | An asset incorporated into a larger asset, in C2PA's terminology. Where a composite is built from many ingredients, the provenance of those ingredients cannot be verified in the same way as the finished asset. A film is composite by default, across picture, sound, music, and VFX, which is why a signed camera capture says little about how the production was made. |
| Watermarking | A signal carried inside the content itself rather than attached to the file. Visible watermarks are seen by the viewer; imperceptible ones are detectable only by machine. Because the mark is in the pixels or the audio, it can survive re-encoding and screen capture, which metadata usually does not. It establishes that content carries a mark a detector recognises. Robustness varies by medium, and text is the weakest case, since paraphrase tends to remove the signal. |
| Fingerprinting | An identifier computed from the content and stored in an external database, adding nothing to the file. YouTube's Content ID is the familiar example. Used to match a work against a reference set, it works without any cooperation from whoever made the content. |
| Machine-readable marking | The obligation under Article 50 of the EU AI Act that outputs of generative systems be marked so they can be detected as artificially generated by automated means. Watermarking and signed metadata are two ways of meeting it. This marking duty sits with the provider of the AI system, not with the production that used it. A separate Article 50 obligation requires deployers to disclose deepfakes to audiences, which can fall on the production, with a lighter duty for artistic and fictional works. |

### How it is communicated

| Term | Meaning |
|---|---|
| Labelling | An audience-facing statement that AI was involved: a caption, an icon, an end card. It communicates and nothing more. Its credibility rests entirely on whatever process stands behind it; a label with no process behind it is a claim, not evidence. |
| Disclosure | Stating how a work was made, to a defined recipient, in a defined form. A label is disclosure aimed at an audience; a declaration in chain of title is disclosure aimed at a counterparty who can act on it. Different recipients, different consequences for being wrong. |
| Self-declaration and certification | A self-declaration is a statement by the party who made the thing. A certification is a statement by an independent body that has assessed the thing against a published standard, normally with audit and the power to withdraw. Organic and RSPCA Assured are certifications. Most AI labels now in circulation are self-declarations presented with the visual language of certification, which is where public understanding of them goes wrong. |

### What it means commercially

| Term | Meaning |
|---|---|
| Warranted declaration | A statement of fact made inside a contract, where the party making it is liable if it proves untrue. This is the standard other producer representations already meet. It is not verification; its force comes from contractual remedy rather than any technical check. |
| Chain of title | The documented set of agreements, assignments, and licences establishing who owns what in a film and on what terms. Buyers, financiers, and insurers review it before money moves. It is a legal record, and no technical artefact substitutes for it. |
| Clearance | Permission obtained for third-party material or rights appearing in the work: music, artwork, trademarks, locations, likeness, underlying literary rights. Separate from owning the footage. Provenance data can help document what went into a shot, which makes assembling a clearance case easier, but it does not establish that permission was obtained. |
| Errors and omissions insurance | Cover against claims arising from the content of a work, including infringement and defamation. Underwriters require clearance and chain-of-title documentation, and distributors normally require the policy. This is the practical reason overclaiming what provenance proves creates exposure rather than comfort. |

### Alignment with existing definitions

Where recognised definitions for these terms already exist, or later emerge, within the creative sectors, HPF will look to adopt or align with them rather than maintain its own. HPF is not leading, and does not intend to lead, any definition-standardisation effort; its aim is a usable disclosure standard, not a competing vocabulary. This is under consultation, and the definitions above remain authoritative for HPF until v1.0. Nothing here implies coordination with, or endorsement by, any external initiative.

---

## Consultation

v0.9 is a draft for consultation. Feedback can be submitted to contact@humanprovenance.film or via the GitHub repository (issues or pull requests). Responses received before 31 October 2026 will inform the v1.0 revision.

The questions we most want input on:

1. Does the present-and-originated principle, and the three categories it produces, capture the distinction that matters to your organisation? Is anything missing, such as a fourth category?
2. Is the declaration mechanism workable in your part of the industry, and if not, what would need to change? In particular, for a `no_ai` declaration, software now switches AI features on by default, so would a "reasonable enquiry" standard, the same one used for other chain-of-title warranties, be a fair basis?
3. Marketing materials, such as trailers, posters, and social cuts, are currently out of scope. How urgent is it to bring them in?
4. For platforms, broadcasters, and distributors: would you use the `assistive_ai` classification, and would you surface it to audiences?
5. Which ways of showing the disclosure are practical and clear, from end credits to delivery metadata to a platform label, and what would meet your regulatory obligations?
6. Does the chain-of-title mechanism work outside the UK and US, where co-production paperwork differs? Are there regulatory, contractual, or collective-bargaining frameworks HPF needs to account for in v1.0?
7. Should established, ubiquitous machine-learning features that process human-created material, such as denoising, upscaling, and tracking, require `assistive_ai` disclosure, or should they sit with the routine automation the taxonomy already treats as out of scope?

For technical implementation guidance: [INTEGRATION.md](INTEGRATION.md).

---

## Licence

CC BY 4.0. See [LICENSE.md](LICENSE.md).

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
