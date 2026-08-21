# Security

Report a suspected vulnerability privately. Do not open a public issue for one.

## How to report

Use GitHub private vulnerability reporting on this repository, under the
Security tab, or email **contact@humanprovenance.film** with `Security` in the
subject line. Either route reaches the maintainer directly and is not public.

Tell us what you found, where, and how to reproduce it. A proof of concept
helps. If you cannot share details over email, say so and we will arrange
another route.

We aim to acknowledge a report within five working days, the same commitment
made for issues and pull requests in [CONTRIBUTING.md](CONTRIBUTING.md). We
will tell you what we intend to do and when, and we will credit you when the
fix is published unless you would rather we did not.

Please give us a reasonable opportunity to fix the problem before describing it
publicly. Do not access, alter or retain anyone else's data while
investigating, and do not run tests that degrade the service for other people.

## What is in scope

- **humanprovenance.film**, including the producer declaration form and any
  downloadable document served from it.
- **`schema.json` and the checks in `tools/`**, where a defect could cause a
  record to be accepted or rejected wrongly, or could execute unintended code
  in a system that consumes them.
- **This repository's GitHub Actions workflows**, where a defect could allow
  an untrusted change to run with elevated permissions.
- **The Policy Translator and the classification and declaration builder**,
  once they are published. Neither is live yet. When they are, they belong here
  and this section will name them without the qualification.

If you are not sure whether something is in scope, report it.

## What is not in scope

- Findings that require a compromised device, a compromised email account or a
  person to be deceived into acting against their own interest.
- Missing hardening headers, or the output of an automated scanner, with no
  demonstrated effect.
- Denial of service through volume alone.
- Anything about a third-party service HPF uses rather than operates. Report
  those to the service concerned. Tell us as well if it affects HPF.

## A note on scope of a different kind

A vulnerability report is about a technical defect. An objection to what the
standard says, or to how a production has been classified, is not a security
matter. Those go through the routes in [CONTRIBUTING.md](CONTRIBUTING.md).

HPF is a self-declaration standard. It does not verify declarations, so an
inaccurate declaration is not a vulnerability in HPF. Responsibility for the
accuracy of a declaration sits with the producer who signed it, and the remedy
is a matter for the parties to the agreement that carries it. Report a defect
that would let a system alter, misread or fabricate a declaration record, which
is a different thing.

## No bounty

HPF does not operate a bug bounty and cannot pay for reports. We would still
rather hear from you.
