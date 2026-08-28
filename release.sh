#!/bin/bash
# Tag a revision of the HPF AI Disclosure Taxonomy.
#
# Run it from a terminal, from anywhere:
#
#     ~/Documents/GitHub/HPF/hpf-taxonomy/release.sh 0.9.3
#
# docs/release-checklist.md is the process. This script is the part of it a
# machine can enforce. On 28 August 2026 a tag was cut with most of that
# checklist unrun, and the missing steps had to be reconstructed afterwards in
# the wrong order. A checklist that asks nicely gets skipped. Gates do not.
#
# Nine gates, in order:
#
#   1. A version argument that looks like MAJOR.MINOR.PATCH.
#   2. On main, nothing uncommitted, in sync with GitHub.
#   3. The tag does not already exist, here or on GitHub. A tag never moves.
#   4. taxonomy.md, CITATION.cff and GOVERNANCE.md all name this version.
#   5. GOVERNANCE.md has a version-history row for it.
#   6. That row is pinned in tools/frozen.txt. It becomes a record at the tag.
#   7. tools/check_standard.py passes.
#   8. tools/check_site.py passes in hpf-site, parity check included, so the
#      published standard and the site agree before the tag fixes either.
#   9. An open issue named "Release v<version>" carries an approval line with a
#      person, a date and the commit about to be tagged.
#
# Then it prints the steps no machine can do, asks you to confirm, tags and
# pushes.
#
# To release something that fails a gate, fix the gate. Do not edit this script.

set -euo pipefail
cd "$(dirname "$0")"

fail() { echo; echo "STOPPED: $1"; echo; exit 1; }

[ -f taxonomy.md ] || fail "no taxonomy.md here. Run this from the hpf-taxonomy repository."

version="${1:-}"
[ -n "$version" ] || fail "give the version to release.
  ./release.sh 0.9.3"
[[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || fail "'$version' is not MAJOR.MINOR.PATCH.
Every revision carries its own patch number. See docs/release-checklist.md."
tag="v$version"

echo "HPF standard release, $tag"
echo

# ---------------------------------------------------------------- repository

branch=$(git rev-parse --abbrev-ref HEAD)
[ "$branch" = "main" ] || fail "you are on '$branch', not main.
  git switch main"

[ -z "$(git status --porcelain)" ] || fail "you have uncommitted changes.
A tag must name a commit, and this working tree is not one.
  git status"

git fetch --quiet origin main
local_head=$(git rev-parse main)
remote_head=$(git rev-parse origin/main)
if [ "$local_head" != "$remote_head" ]; then
  if git merge-base --is-ancestor "$remote_head" "$local_head"; then
    fail "you have commits that are not on GitHub.
  git push"
  else
    fail "GitHub has commits you do not.
  git pull"
  fi
fi

if git rev-parse -q --verify "refs/tags/$tag" >/dev/null; then
  fail "$tag already exists on this machine.
A published tag never moves. If this revision needs a change, it needs a new
patch number.
  git tag -l"
fi
if git ls-remote --exit-code --tags origin "refs/tags/$tag" >/dev/null 2>&1; then
  fail "$tag already exists on GitHub.
A published tag never moves. Release the next patch number instead."
fi

# ------------------------------------------------------------------ contents

grep -q "Version $version" taxonomy.md \
  || fail "taxonomy.md does not state Version $version."
grep -q "version: \"$version\"" CITATION.cff \
  || fail "CITATION.cff does not name $version.
It carries the version being released, and it is committed before the tag."
grep -q "Version $version" GOVERNANCE.md \
  || fail "GOVERNANCE.md does not state Version $version."

grep -q "^| $version |" GOVERNANCE.md \
  || fail "GOVERNANCE.md has no version-history row for $version.
Write it before tagging. It is the record of what this revision changed, and
after the tag it is not edited again. See step 6 of docs/release-checklist.md."

grep -q "| $version |" tools/frozen.txt \
  || fail "the $version version-history row is not pinned in tools/frozen.txt.
A row is a working draft until its revision is tagged and a closed record after.
Pin it now, in the same commit as the row.

  1. Add this line to tools/frozen.txt, next to the other GOVERNANCE.md rows:

     row :: GOVERNANCE.md :: | $version | <Month> 2026 | :: PENDING :: released in $tag

  2. Recompute the hashes. --frozen-hashes fills in values for rows that are
     already listed; it does not add new ones, which is why step 1 comes first.

     python3 tools/check_standard.py --frozen-hashes > /tmp/frozen.new
     cp /tmp/frozen.new tools/frozen.txt

  3. Commit and push, then run this script again."

# -------------------------------------------------------------------- checks

echo "Running the standard checks."
python3 tools/check_standard.py || fail "the checks failed. Fix the findings, or add
an allowlist entry with a reason. Do not release around a finding."
echo

site="../hpf-site"
if [ -d "$site/site" ]; then
  echo "Running the site checks, parity included."
  ( cd "$site" && python3 tools/check_site.py ) || fail "the site checks failed.
If taxonomy-parity is the finding, the site and the standard disagree. The
standard merges first, then the site follows it. Fix the site, then release."
  echo
else
  echo "NOTE: hpf-site is not beside this repository, so the parity check was"
  echo "      skipped. Run tools/check_site.py there before you continue."
  echo
fi

# ------------------------------------------------------------------ approval

short=$(git rev-parse --short main)
echo "Looking for the approval issue."
remote_url=$(git config --get remote.origin.url)
slug=$(echo "$remote_url" | sed -E 's#^.*github.com[:/]##; s#\.git$##')
issues=$(curl -fsS "https://api.github.com/repos/$slug/issues?state=open&per_page=100" 2>/dev/null || echo "")

if [ -z "$issues" ]; then
  echo "NOTE: could not reach the GitHub API, so the approval issue was not"
  echo "      checked. Confirm it yourself before continuing."
  echo
else
  # The issue body must name this commit. An approval that does not say what it
  # approved is not an approval.
  if echo "$issues" | grep -q "\"title\": *\"Release $tag\""; then
    if echo "$issues" | grep -q "$short"; then
      echo "Found an open 'Release $tag' issue naming commit $short."
      echo
    else
      fail "the 'Release $tag' issue does not name commit $short.
Approval records what was approved. If the commit moved after it was written,
read the diff again and update the issue."
    fi
  else
    fail "no open issue titled 'Release $tag'.
No automated check approves a release. Open one and record your approval by
name, date and commit:

  Approved for release by <name>, <date>.
  Commit being tagged: $short

  https://github.com/$slug/issues/new"
  fi
fi

# ------------------------------------------------------------------- confirm

subject=$(git log -1 --pretty=%s main)
echo "About to tag $short  $subject"
echo "               as $tag"
echo
echo "Still to do by hand, after this script:"
echo "  1. Publish the GitHub release against $tag, marked pre-release."
echo "  2. Deploy hpf-site so the live site serves this revision."
echo "  3. Publish the news post, then pin it in the site's tools/frozen.txt."
echo "  4. Close the release issue."
echo
read -r -p "Type release to tag and push, anything else to stop: " answer
[ "$answer" = "release" ] || fail "nothing was tagged."
echo

git tag -a "$tag" -m "$(date +'%B %Y') consultation revision"
git push --quiet origin "$tag"

echo "Tagged $short as $tag and pushed it."
echo
echo "Release notes: https://github.com/$slug/releases/new?tag=$tag"
