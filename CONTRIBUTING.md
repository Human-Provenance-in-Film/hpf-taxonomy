# Contributing to the HPF AI disclosure taxonomy

Anyone can contribute, whether individually or on behalf of an organisation. Feedback from production, performance, post-production, and technical implementation is welcome.

HPF is a pre-v1 draft, currently version 0.9.4. The public consultation closed on 31 October 2026, but feedback remains welcome.

## Ways to contribute

- Open an issue using the **change proposal** template to propose a change to the taxonomy, schema, descriptors or supporting documentation.
- Open an issue using the **bug or inconsistency** template when something is wrong, broken or contradicted elsewhere.
- Open a pull request to propose specific wording or schema changes. The pull request template lists what a reviewer checks.
- Email contact@humanprovenance.film if you would rather respond privately or at length.

For a small correction, such as a typo or a broken link, use the **bug or inconsistency** template: only what it says now and where it appears are required. A pull request opened through the GitHub web interface fills in its template; for a small correction, two or three sentences under "What this changes" and a one-line answer to the classification question are enough.

Partial feedback is welcome. If you are answering one of the numbered open questions in [taxonomy.md](taxonomy.md#consultation), please say which one. The numbering changed in revision 0.9.3; if you are answering a question as an earlier draft numbered it, say so.

Separately from the consultation, pre-v1 working groups are testing the classifications, descriptors, and declaration form against production cases. Current participation details are on the [HPF website](https://humanprovenance.film/taxonomy#working-groups). The groups are advisory. They are not the future governing body, and participation does not imply endorsement of HPF. See [GOVERNANCE.md](GOVERNANCE.md).

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

We read every proposal and assess whether it fits HPF's scope, provides useful information to recipients, and adds a proportionate amount of work for producers. Submitting an issue or pull request does not guarantee a change.

Each proposal receives a recorded outcome and reason: **Accepted**, **Accepted with changes**, **Declined**, **Deferred**, **Duplicate**, or **Outside HPF scope**.

HPF records AI output present in the finished production. It does not request, store, disclose, validate, or carry consent, authorisation, licensing, compensation, rights ownership, or compliance information. These belong in contracts, collective agreements, chain-of-title records, and rights-management systems. Proposals to add them are declined as **Outside HPF scope**.

A proposed structured field must record information that more than one part of the supply chain needs to interpret consistently. The change proposal template lists the five criteria it must meet.

Before v1.0, the draft is revised in response to feedback. Changes are recorded in [GOVERNANCE.md](GOVERNANCE.md). From v1.0, the [amendment process](GOVERNANCE.md#amendment-process) applies.

We cannot promise a response time or implementation date for each proposal. Feedback received too late for one revision is recorded for the next. Published release tags remain unchanged.

## Licensing and rights in what you submit

By contributing, you agree that your contribution is licensed under CC BY 4.0, the same licence as the project. This applies to anything you submit through an issue, a pull request or by email with the intention that it be used in HPF. See [LICENSE.md](LICENSE.md).

You are responsible for having the right to submit what you send. Only submit material that is your own work, or that you are otherwise entitled to contribute under CC BY 4.0. Do not paste in an employer's confidential material, a third party's copyrighted text, or an organisation's internal policy document that you are not free to share. If you want to describe a policy you cannot share, summarise its effect in your own words.

## Confidentiality and personal data

Issues and pull requests in this repository are public and are indexed by search engines. Do not put names, contact details, an unpublished policy, a commercial term or anyone else's personal data into one.

Private consultation responses stay private. They are held in HPF's consultation record and are not copied into public issues. Where a private response leads to implementation work, a summarised issue is opened describing the change alone, without the source's identity or wording. If you would rather your response were not reflected publicly at all, even in summary, say so when you send it.

## Conflicts of interest

If you have an interest in the outcome of a proposal, say so in the issue. Examples: you work for or advise an organisation whose policy or product would be affected, you sell a tool whose classification is in question, or you represent a body whose members are. A stated interest is not a problem and does not weigh against a proposal. Stating it keeps the decision record clear for later readers.

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
