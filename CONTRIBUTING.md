# Contributing to the HPF AI disclosure taxonomy

Thank you for your interest. HPF v0.9 is a pre-v1 draft. The public consultation closed on 31 October 2026, and feedback on the standard remains welcome from trade associations, unions and guilds, festivals, awards bodies, commissioners, funders, and other industry organisations. Companies in the screen industries that are considering adopting HPF, including C2PA and CAI members, are welcome to send technical and implementation feedback.

## Ways to contribute

- Open an issue using the **change proposal** template to propose a change to the taxonomy, schema, descriptors or supporting documentation.
- Open an issue using the **bug or inconsistency** template when something is wrong, broken or contradicted elsewhere.
- Open a pull request to propose specific wording or schema changes. The pull request template lists what a reviewer checks.
- Email contact@humanprovenance.film if you would rather respond privately or at length.

Partial feedback is welcome. If you are answering one of the numbered open questions in [taxonomy.md](taxonomy.md#consultation), please say which one. The numbering changed in the September 2026 revision; if you are answering a question as an earlier draft numbered it, say so.

Separately from the consultation, HPF is recruiting pre-v1 working groups to test the classifications, descriptors, and declaration form against production cases in November and December 2026. Participants contribute through written case reviews, with an optional meeting. Sign up through the [working-group form](https://docs.google.com/forms/d/e/1FAIpQLSfmNKsb34zoS0FGGF23m4fJ3pRihP6YE4_SkH0hK_-VFPgQjw/viewform) by 13 November 2026. Worked examples are welcome at contact@humanprovenance.film by the same date; they can be anonymised and may contain incomplete information. The groups are advisory. They are not the future governing body, and participation does not imply endorsement of HPF. See [GOVERNANCE.md](GOVERNANCE.md).

To report a suspected security vulnerability, use the private route in [SECURITY.md](SECURITY.md) rather than a public issue.

## Where feedback is most useful

The open questions are listed in the [feedback and testing section of taxonomy.md](taxonomy.md#consultation). In short:

- Practical checks and established machine learning, in two parts. Practical checks: what can producers establish in difficult workflows, particularly when software includes AI features that may run automatically? Classification scope: which established functions, such as denoising and tracking, should require Assistive AI disclosure? Concrete workflow examples are especially useful here.
- Whether the adopted performance descriptors can be applied consistently, what examples would help, and when Generated visual content adds information alongside them. More than one descriptor may already apply where each adds a distinct fact.
- Whether factual summaries describe clearly what human acting, voice or motion capture contributed to a synthetic performance. A new descriptor is not assumed.
- Complex finished-work and version cases: intermediate VFX control data such as mattes and masks, autonomous editing, substantially transformed output, difficult restoration cases, localisation, subtitles and captions, and episodic releases. These are also the subject of the working groups' case reviews.
- Implementation: what producers can establish, how to proceed when a supplier cannot answer, and what receiving organisations find useful.

If a real production use does not fit the current categories, we want to hear about it. Comments on any glossary definition are also welcome, particularly where a term is already used differently in your part of the industry.

Technical implementers can comment on the proposed C2PA mapping in [c2pa-mapping.md](c2pa-mapping.md) and on the technical implementation questions in [INTEGRATION.md](INTEGRATION.md). These are integration matters, separate from the open questions in the standard.

Performers, casting professionals, agents, union representatives and business-affairs practitioners are welcome to help test whether the factual vocabulary is clear and usable. HPF does not determine contractual permission, consent, compensation, rights or legal compliance, and those questions are outside the standard.

## How proposals are handled

Every proposal is read. Not every proposal is adopted, and opening an issue or a pull request does not commit HPF to making the change. A well-argued proposal can still be declined because it conflicts with a settled boundary, because it would add work for producers out of proportion to what it gives recipients, or because it belongs to a system other than HPF.

Each proposal is recorded with one of these outcomes, and the reasoning is recorded with it:

**Accepted**, **Accepted with changes**, **Declined**, **Deferred**, **Duplicate**, or **Outside HPF scope**.

Two boundaries decline proposals often enough to be worth stating in advance.

**HPF records what AI output is present in the finished production.** It does not request, store, disclose, validate or carry consent, authorisation, licensing, compensation, rights ownership or compliance information. Those belong in contracts, collective agreements, chain-of-title records and rights-management systems. A proposal to add them is declined as Outside HPF scope, however useful the information is.

**A new structured field has to earn its place.** HPF structures a fact that more than one part of the supply chain needs to read the same way, not every decision that might follow from it. The change proposal template sets out the five questions a new field has to pass.

Until v1.0, the draft is revised directly in response to feedback, with each change recorded in the version history in [GOVERNANCE.md](GOVERNANCE.md). From v1.0, the maintenance and amendment process in the [amendment process section of GOVERNANCE.md](GOVERNANCE.md#amendment-process) applies. We read every proposal but do not promise a response time or an implementation date for each one.

Feedback that arrives too late for one revision is recorded against the next. A published tag is never rewritten to fit something in.

## Licensing and rights in what you submit

By contributing, you agree that your contribution is licensed under CC BY 4.0, the same licence as the project. This applies to anything you submit through an issue, a pull request or by email with the intention that it be used in HPF. See [LICENSE.md](LICENSE.md).

You are responsible for having the right to submit what you send. Only submit material that is your own work, or that you are otherwise entitled to contribute under CC BY 4.0. Do not paste in an employer's confidential material, a third party's copyrighted text, or an organisation's internal policy document that you are not free to share. If you want to describe a policy you cannot share, summarise its effect in your own words.

## Confidentiality and personal data

Issues and pull requests in this repository are public and are indexed by search engines. Do not put names, contact details, an unpublished policy, a commercial term or anyone else's personal data into one.

Private consultation responses stay private. They are held in HPF's consultation record and are not copied into public issues. Where a private response leads to implementation work, a summarised issue is opened describing the change alone, without the source's identity or wording. If you would rather your response were not reflected publicly at all, even in summary, say so when you send it.

## Conflicts of interest

If you have an interest in the outcome of a proposal, say so in the issue. Examples: you work for or advise an organisation whose policy or product would be affected, you sell a tool whose classification is in question, or you represent a body whose members are. A stated interest is not a problem and does not weigh against a proposal. An unstated one damages the record afterwards, and this consultation's record is meant to be readable years from now.

The same applies to us. HPF was developed by The Mise En Scène Company, an international film sales agency, which owns the copyright and has its own commercial interest in AI disclosure. That is stated in [GOVERNANCE.md](GOVERNANCE.md) and on the website.

## Running the checks

```
python3 tools/check_standard.py
```

Python 3, no dependencies. It checks that the schema still states the controlled values the taxonomy defines, that the records in `examples/` validate or fail as their names say, that no withdrawn classification or undefined descriptor value appears, that every file names the same taxonomy version, that no superseded language survives, that there are no em dashes, that links resolve, and that no record pinned in `tools/frozen.txt` has changed.

The same checks run on every push and pull request through `.github/workflows/standard-checks.yml`.

These checks detect objective inconsistency. They make no judgement about writing quality or about what the taxonomy should say. If a finding is a deliberate exception, record it in `tools/check-allowlist.txt` with a reason. Do not delete a check to silence it.

One exception: a `frozen` finding is not allowlistable. A version-history entry for a released revision is the record of what that revision changed, and is not edited afterwards, for the same reason a published tag never moves. `tools/frozen.txt` pins each released entry by hash; the newest entry stays a working draft until its revision is tagged. `python3 tools/check_standard.py --frozen-hashes` reprints the manifest with current hashes and writes nothing.

## Scope of this repository

This repository holds the technical specification: the taxonomy, JSON schema, C2PA mapping, and integration and governance documents. Plain-language guidance for productions and the producer declaration form are at [humanprovenance.film](https://humanprovenance.film).

## House style

UK English. No em dashes. Direct, specific sentences.

HPF is a self-declaration standard. Nothing here may say or imply that HPF verifies, certifies, approves or determines eligibility, or that it records consent, authorisation, licensing, compensation or rights ownership. Do not claim adoption, endorsement, partnership, accreditation or independent governance that does not yet exist.

---

CC BY 4.0. See [LICENSE.md](LICENSE.md). contact@humanprovenance.film | [humanprovenance.film](https://humanprovenance.film)
