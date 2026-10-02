# Contributing to the HPF AI disclosure taxonomy

Thank you for your interest. HPF v0.9 is a draft open for public consultation until 31 October 2026. We welcome feedback from productions, distributors, platforms, festivals, regulators, and technical implementers, including C2PA and CAI members.

## Ways to contribute

- Open an issue using the **change proposal** template to propose a change to the taxonomy, schema, descriptors or supporting documentation.
- Open an issue using the **bug or inconsistency** template when something is wrong, broken or contradicted elsewhere.
- Open a pull request to propose specific wording or schema changes. The pull request template lists what a reviewer checks.
- Email contact@humanprovenance.film if you would rather respond privately or at length.
- Complete the descriptor survey, open until 31 October 2026 and linked from [humanprovenance.film](https://humanprovenance.film/taxonomy#consultation). It asks about the definitions and the provisional descriptors. The Pre-v1 Consultation Survey phase closed on 30 September 2026.

Partial feedback is welcome. If you are answering one of the numbered consultation questions in [taxonomy.md](taxonomy.md#consultation), please say which one. The numbering changed in the September 2026 revision; if you are answering a question as an earlier draft numbered it, say so.

HPF is also identifying a small pre-v1 working group to pressure-test the taxonomy, descriptors, and implementation against real production and institutional use cases, through case reviews in November and December 2026. Email contact@humanprovenance.film to register interest. The group is advisory. It is not the future governing body, and participation does not imply endorsement of HPF. See [GOVERNANCE.md](GOVERNANCE.md).

To report a suspected security vulnerability, use the private route in [SECURITY.md](SECURITY.md) rather than a public issue.

## Where feedback is most useful

The open questions are listed, with the points already settled, in the [consultation section of taxonomy.md](taxonomy.md#consultation). In short:

- Reasonable enquiry and established machine learning, in two parts. Declaration basis: is reasonable enquiry the appropriate basis for a No AI Used declaration where AI functions may be built into software, enabled by default, or difficult to identify? Classification scope: which established machine-learning functions, if any, should require Assistive AI disclosure when they process picture or sound retained in the released version? Concrete workflow examples are especially useful here.
- Whether the performance-related descriptors are clear, what examples would help, and when Generated Visual Content is used alongside them. More than one descriptor may already apply where each adds distinct factual information.
- How to describe human performance inputs that contribute to a synthetic performance without representing an identifiable person. Guidance may answer this rather than a new descriptor.
- Complex finished-work and version cases: transformed output, intermediate VFX control data, restoration and reconstruction, localisation, subtitles and captions, episodic releases, and animation workflows, including in-between cases where work builds on human input but adds something new. These are also the subject of the working group's case reviews.
- Implementation: what producers can establish, and what receiving organisations find useful.

If a real production use does not fit the current categories, we want to hear about it. Comments on any glossary definition are also welcome, particularly where a term is already used differently in your part of the industry.

Technical implementers can comment on the proposed C2PA mapping in [c2pa-mapping.md](c2pa-mapping.md) and on the technical implementation questions in [INTEGRATION.md](INTEGRATION.md). These are integration matters, separate from the consultation questions.

Performers, casting professionals, agents, union representatives and business-affairs practitioners are welcome to help test whether the factual vocabulary is clear and usable. HPF does not determine contractual permission, consent, compensation, rights or legal compliance, and those questions are not part of the consultation.

## How proposals are handled

Every proposal is read. Not every proposal is adopted, and opening an issue or a pull request does not commit HPF to making the change. A well-argued proposal can still be declined because it conflicts with a settled boundary, because it would add work for producers out of proportion to what it gives recipients, or because it belongs to a system other than HPF.

Each proposal is recorded with one of these outcomes, and the reasoning is recorded with it:

**Accepted**, **Accepted with changes**, **Declined**, **Deferred**, **Duplicate**, or **Outside HPF scope**.

Two boundaries decline proposals often enough to be worth stating in advance.

**HPF records what AI output is present in the finished production.** It does not request, store, disclose, validate or carry consent, authorisation, licensing, compensation, rights ownership or compliance information. Those belong in contracts, collective agreements, chain-of-title records and rights-management systems. A proposal to add them is declined as Outside HPF scope, however useful the information is.

**A new structured field has to earn its place.** HPF structures a fact that more than one part of the supply chain needs to read the same way, not every decision that might follow from it. The change proposal template sets out the five questions a new field has to pass.

While v0.9 is open for consultation, the draft is revised directly in response to feedback, with each change recorded in the version history in [GOVERNANCE.md](GOVERNANCE.md). From v1.0, the amendment process in GOVERNANCE.md applies. We aim to acknowledge issues and pull requests within five working days.

Feedback that arrives too late for one revision is recorded against the next. A published tag is never rewritten to fit something in.

## Licensing and rights in what you submit

By contributing, you agree that your contribution is licensed under CC BY 4.0, the same licence as the project. This applies to anything you submit through an issue, a pull request or by email with the intention that it be used in HPF. See [LICENSE.md](LICENSE.md).

You are responsible for having the right to submit what you send. Only submit material that is your own work, or that you are otherwise entitled to contribute under CC BY 4.0. Do not paste in an employer's confidential material, a third party's copyrighted text, or an organisation's internal policy document that you are not free to share. If you want to describe a policy you cannot share, summarise its effect in your own words.

## Confidentiality and personal data

Issues and pull requests in this repository are public and are indexed by search engines. Do not put names, contact details, an unpublished policy, a commercial term or anyone else's personal data into one.

Private consultation responses stay private. They are held in HPF's consultation record and are not copied into public issues. Where a private response leads to implementation work, a summarised issue is opened describing the change alone, without the source's identity or wording. If you would rather your response were not reflected publicly at all, even in summary, say so when you send it.

## Conflicts of interest

If you have an interest in the outcome of a proposal, say so in the issue. Examples: you work for or advise an organisation whose policy or product would be affected, you sell a tool whose classification is in question, or you represent a body whose members are. A stated interest is not a problem and does not weigh against a proposal. An unstated one damages the record afterwards, and this consultation's record is meant to be readable years from now.

The same applies to us. HPF was originated by The Mise En Scène Company, an international film sales agency, which owns the copyright and has its own commercial interest in AI disclosure. That is stated in [GOVERNANCE.md](GOVERNANCE.md) and on the website.

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
