# Contributing to vntext

Thanks for taking the time to contribute! This guide explains how we work.
Please read it fully before your first pull request — following it makes
review much faster for everyone.

## 1. Before you start

- **Look for an existing issue.** Every pull request should be linked to an issue.
  If none exists, open one first and describe the problem or the idea.
- **Claim the issue.** Leave a comment such as "I'd like to work on this" and wait
  until a maintainer assigns it to you. This avoids two people doing the same work.
- **One issue = one pull request.** If you find another problem while working,
  open a separate issue instead of fixing it in the same PR.

## 2. Development setup

```bash
# 1. Fork the repository on GitHub, then clone YOUR fork
git clone https://github.com/<your-username>/vntext.git
cd vntext

# 2. Keep a reference to the original repository
git remote add upstream https://github.com/thienta-oss-lab/vntext.git

# 3. Create a virtual environment and install dev dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# 4. Install the git hooks (runs ruff automatically before each commit)
pre-commit install
```

## 3. Making a change

1. Sync with upstream and create a branch from the latest `main`:

   ```bash
   git switch main
   git pull upstream main
   git switch -c fix/<issue-number>-short-description
   ```

   Branch prefixes: `fix/`, `feat/`, `docs/`, `test/`, `refactor/`.

2. Write your change. **Bug fixes must include a test** that fails before the fix
   and passes after it. New features must include tests and documentation.

3. Run all checks locally — CI runs exactly the same commands:

   ```bash
   ruff check .
   ruff format --check .
   pytest
   ```

   Coverage must stay at or above 90%.

4. Add a line under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## 4. Commit messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short summary in imperative mood>

<optional body: what and why, not how>

Fixes #<issue-number>
```

Types: `fix`, `feat`, `docs`, `test`, `refactor`, `chore`, `ci`.

Good: `fix: convert đ to d in remove_accents`
Bad: `update code`, `fixed bug`, `WIP`

## 5. Pull requests

- Push the branch to **your fork** and open a PR against `thienta-oss-lab/vntext:main`.
- Fill in the PR template completely. Write `Fixes #<number>` so the issue closes
  automatically on merge.
- Keep PRs small and focused. Large PRs take much longer to review.
- **CI must be green.** A PR with failing checks will not be reviewed.
- `main` is protected: your branch must be up to date with `main` before merging.
  If it is behind, rebase it:

  ```bash
  git fetch upstream
  git rebase upstream/main
  git push --force-with-lease
  ```

## 6. Code review

- Every comment from a reviewer must be answered — either by changing the code or
  by explaining why you think the current approach is better. Both are fine.
- Push follow-up commits for review changes; do not open a new PR.
- Mark a conversation as resolved only after the reviewer's concern is addressed.
  All conversations must be resolved before merging.
- PRs are **squash-merged** by a maintainer, so the final commit message is taken
  from the PR title. Make the title a good Conventional Commit.

## 7. Code of Conduct

By participating you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).
