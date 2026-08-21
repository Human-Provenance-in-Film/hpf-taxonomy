# Release-candidate checklist

**Checklist version 1.0. Applies to taxonomy version 0.9 and its revisions.**

Run this before tagging any revision of the consultation draft, and again
before the final consultation tag on 31 October 2026. Every step is a gate.
Do not tag until all of them pass.

A published tag never moves. That is the whole reason this checklist exists:
once the artefact is out, the only way to correct it is another revision.

## Scope

This applies to a `v0.9.x` pre-release tag on `hpf-taxonomy`. The taxonomy
version stays `0.9` for the whole consultation; the tag identifies which
revision of it a reader has. Those are different things, and the checklist
keeps them from being conflated. See [GOVERNANCE.md](../GOVERNANCE.md).

The site is released separately by deploying `hpf-site`. Step 5 is the point
where the two have to agree.

---

## 1. Content freeze

- [ ] Announce the freeze date. After it, only release-blocking fixes go in.
- [ ] No open pull request changes taxonomy meaning, controlled values or schema fields.
- [ ] Every change since the last tag is recorded in an issue, and every one of those issues is closed or explicitly deferred.
- [ ] Feedback that arrived too late is recorded against the next revision, not slipped in.

## 2. Issue closure or deferral

- [ ] Every open issue on the **v0.9 consultation close** milestone is closed, or moved off the milestone and labelled `deferred-v1.0`.
- [ ] No issue labelled `release-blocker` is open.
- [ ] Each deferred issue records why it was deferred and what would settle it. A deferral with no reason is an unmade decision, not a decision.
- [ ] Every accepted meaning change since the last tag is linked from the version-history entry drafted in step 6.

## 3. Canonical tests

- [ ] `python3 tools/check_standard.py` passes on a clean checkout of the release commit.
- [ ] `python3 tools/check_site.py` passes in `hpf-site`, including the taxonomy parity check, which needs network access and is skipped when run through the desktop bridge.
- [ ] Both GitHub Actions jobs are green on the release commit: `standard-schema-and-examples` and `standard-consistency`.
- [ ] The `site-consistency` job is green in `hpf-site`.
- [ ] Every allowlist entry in either repository still has a reason that is still true. Remove any that no longer applies.
- [ ] `examples/` covers any rule added or changed in this revision, in both directions.

## 4. Documentation consistency

- [ ] `taxonomy.md`, `schema.json`, `README.md`, `INTEGRATION.md`, `c2pa-mapping.md` and the site state the same controlled values and the same taxonomy version.
- [ ] Any field marked provisional is still marked provisional everywhere, or has been promoted everywhere by an explicit decision.
- [ ] Version histories in `GOVERNANCE.md`, `INTEGRATION.md` and `c2pa-mapping.md` each record this revision where the file changed.
- [ ] No unresolved conflict remains in the documentation conflict register.

## 5. Live-site and download verification

Do this against the deployed site, not a local preview.

- [ ] `hpf-site` is deployed and the live site serves this revision's content.
- [ ] `humanprovenance.film/taxonomy` and `taxonomy.md` in this repository match, apart from the three links deliberately made absolute for the web.
- [ ] Every download the site offers resolves and opens: the declaration form and any published document.
- [ ] Every rule in `hpf-site/site/_redirects` still resolves, including the legacy withdrawn-document routes and the sample template, and none exposes withdrawn material.
- [ ] The site and the repository name the same taxonomy version, the same consultation close date, and the same document status.
- [ ] `llms.txt` and `sitemap.xml` list the pages that exist, and none that do not.

## 6. Unresolved-issue review

- [ ] Read the open issues that are not on this milestone. Confirm none of them describes something this release would make wrong.
- [ ] Confirm no claim in the release exceeds what is true today: no adoption, endorsement, partnership, accreditation or independent governance that has not happened.
- [ ] Draft the version-history entry for `GOVERNANCE.md`. State what changed, and state plainly where categories and the organising principle are unchanged.
- [ ] Confirm `CITATION.cff` will name this release once it is published, and not before.

## 7. Human approval

- [ ] The release owner reads the full diff since the previous tag.
- [ ] The release owner records approval in the release issue, by name and date, stating the commit being tagged.

No automated check approves a release. The checks establish that the repository
is internally consistent. Whether the standard should say what it now says is a
judgement, and a person makes it.

## 8. Tag and publish

- [ ] Commit the version-history entry and the `CITATION.cff` date.
- [ ] `git tag -a v0.9.x -m "<Month Year> consultation revision"` and push the tag.
- [ ] Draft the GitHub release against that tag, marked pre-release, matching how `v0.9.0` is marked.
- [ ] Attach or link the taxonomy, schema and version history.
- [ ] Publish the news post announcing the revision.
- [ ] Archive the release record and the decision record in the private Drive.

## 9. After the final consultation tag

Only for the 31 October 2026 release.

- [ ] The tagged artefact is the record of what was consulted on. It does not change afterwards.
- [ ] Every consultation response is recorded in the consultation tracker with a status and a decision.
- [ ] Anything unresolved is routed to v1.0 or to a version after it, with a reason.
- [ ] Registered-interest contacts are notified when v1.0 is published, not at this tag.

---

## What this checklist does not do

It does not check that the taxonomy is right, that the wording is good, or that
a classification decision was sound. It checks that what is published is
internally consistent, that nothing is claimed that is not true, and that a
person has looked at it and said so.
