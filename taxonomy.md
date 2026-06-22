# HPF AI Disclosure Taxonomy

**Version 0.9, draft for consultation**
Consultation closes 31 October 2026.

---

## Organising principle

> Is AI output present in the finished film, and did it process human work or originate new content?

The producer answers two questions of fact. First, is any AI output present in the finished film as distributed? If not, the film is No AI Used. If it is, did the AI process human-created material (Assistive AI) or originate new content that appears in the finished work (Generative AI)? The legal weight sits in the warranty the producer signs; the test is simply how they reach an answer they can stand behind.

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

**Examples:** AI-assisted colour grading; noise reduction; automated subtitling and captioning; script analysis tools used by a human writer; de-flickering; archival restoration; AI-assisted sound clean-up; automated camera tracking in VFX prep. Cosmetic de-ageing of a performance captured in full, where AI refines appearance without rebuilding or generating any part of the performance. In animation: AI used to clean up or optimise frames created by animators.

**Not `assistive_ai`:** any AI output that the AI originated rather than deriving from human-created material. If the AI made new content that appears in the finished film, the classification is `generative_ai` regardless of how the tool is marketed.

AI used solely in development that leaves no trace in the finished film does not require classification.

---

### `generative_ai`: Generative AI

AI originated content that appears in the finished film, rather than processing human-created material. The AI made new content rather than refining work created by human crew.

If any AI-originated content is present in the finished work, the production is `generative_ai` regardless of proportion. A film using human-shot footage alongside AI-generated environments is `generative_ai` overall.

**Examples:** AI-generated backgrounds, environments, crowd scenes, or set extensions; AI-written screenplay elements present in the finished film; synthesised or cloned actor performances; AI voice cloning; AI-generated music replacing a composer; de-ageing or posthumous synthesis that fabricates or generates any part of a performance rather than refining one fully captured on set. In animation: AI generating characters, environments, or sequences that animators would otherwise have created.

**Not `generative_ai`:** cosmetic enhancement of a performance that was captured in full (minor de-ageing that does not fabricate part of a performance) is `assistive_ai`. AI used in development only, where no AI-generated content appears in the finished film, does not require `generative_ai` classification.

---

## The reconstruction test

Some AI tools operate on footage, audio, or images that already exist rather than producing content from a prompt. For these, classification turns on whether the tool reconstructs content already present or fabricates content that is not.

Reconstruction restores, cleans, or repairs content that was captured or created by a human: noise reduction, de-flickering, artefact removal, upscaling that sharpens detail already in the source, format conversion. The output is the same content in better condition. This is `assistive_ai`.

Fabrication invents content that was never captured or created: painting in a background revealed by removing an object, generating frames or detail with no source, synthesising a performance element the performer did not give. The output contains material that did not exist before. This is `generative_ai`.

The label a vendor applies does not decide the category. Where a tool both reconstructs and fabricates, the fabrication determines the category.

---

## Scope

This taxonomy covers AI use in development, production, and post-production of the finished film as distributed and exhibited.

**In scope**

- Development, pre-production, and principal photography
- Post-production: editing, colour, sound, VFX, and music
- All co-producers and third-party contractors (aggregated by the lead producer)
- Every distributed or exhibited version of the film

**Out of scope**

- Marketing and promotion: posters, trailers, and social media assets
- Basic automation in standard long-standing industry use: loudness normalisation, timecode tools, spell-check
- AI used solely in development that leaves no trace in the finished film

The lead producer must use the highest category applicable across all co-producers and contractors. This prevents co-production structures from obscuring AI use that would otherwise require disclosure.

Where classification is incorporated into a deal or licensing agreement as a producer representation, misclassification is a matter of contractual liability. This gives the framework legal enforceability without requiring new regulatory infrastructure.

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

### Animation

The test applies in the same way as for live-action. AI processing or refining work created by animators is `assistive_ai`. AI originating characters, environments, or sequences that appear in the finished work is `generative_ai`.

---

## Regulatory scope

HPF covers production-level AI disclosure: what AI was used in making the finished work, declared by the producer. It does not address tool-level obligations. Where a production uses a general-purpose AI model (GPAI) to generate content, the provider of that model may have independent disclosure obligations under applicable regulation, for example under Article 50 of the EU AI Act. HPF and tool-level obligations operate in parallel and are not substitutes for each other.

**Verification standard:** verification under HPF means reasonable commercial reliance on the producer's signed declaration, not a technical audit of the production's tools or workflows. This is the same standard that applies to all producer representations in chain of title documentation. The remedy for misrepresentation is a matter for the contract between the parties. HPF does not operate an independent verification or audit function.

**Audience disclosure:** HPF governs how classification travels through the distribution chain, from producer to platform. It does not currently mandate how platforms surface classification to audiences. Display standards are an open question for the consultation; the framework's open questions list addresses this explicitly. Productions and platforms seeking to make audience-facing disclosure are encouraged to engage with the consultation on what display standards should require.

**Jurisdiction:** HPF is designed to be jurisdiction-agnostic. The classification standard applies regardless of where the production originates or is distributed. It is intended to support disclosure obligations across multiple regulatory regimes, including the EU AI Act, UK AI regulatory frameworks, and platform-level obligations under applicable broadcasting and online safety legislation. Producers and platforms should take independent legal advice on how HPF adoption interacts with their specific regulatory obligations.

The framework is prospective in nature. It applies to productions that adopt it from the point of adoption forward. It does not provide a mechanism for retroactive disclosure of historical catalogue content, and absent values for unclassified historical content should not be read as an absence of AI use.

---

## Consultation

v0.9 is a draft for consultation. Feedback can be submitted to contact@humanprovenance.film or via the GitHub repository (issues or pull requests). Responses received before 31 October 2026 will inform the v1.0 revision.

The questions we most want input on:

1. Does the present-and-originated principle, and the three categories it produces, capture the distinction that matters to your organisation? Is anything missing, such as a fourth category?
2. Is the declaration mechanism workable in your part of the industry, and if not, what would need to change? In particular, for a `no_ai` declaration, software now switches AI features on by default, so would a "reasonable enquiry" standard, the same one used for other chain-of-title warranties, be a fair basis?
3. Two scope boundaries are open. Should any pre-production AI use that never reaches the screen still be disclosed? And how urgent is it to bring marketing materials (trailers, posters, social cuts) into scope?
4. Are the edge cases classified correctly, and are there other situations that need guidance before v1.0? Animation, and content built on human work but newly synthesised (in-betweening, style transfer), is where we most want input.
5. For platforms, broadcasters, and distributors: would you use the `assistive_ai` classification, and would you surface it to audiences?
6. Which ways of showing the disclosure are practical and clear, from end credits to delivery metadata to a platform label, and what would meet your regulatory obligations?
7. Does the chain-of-title mechanism work outside the UK and US, where co-production paperwork differs? Are there regulatory, contractual, or collective-bargaining frameworks HPF needs to account for in v1.0?

For technical implementation guidance: [INTEGRATION.md](INTEGRATION.md).

---

## Licence

CC BY 4.0. See [LICENSE.md](LICENSE.md).

contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
