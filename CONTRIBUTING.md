# Contributing Guidelines

This project uses standard Odoo 18 workflows. To help keep the repository healthy, please review the following policies before submitting code or documentation changes.

## Development Workflow

1. Install dependencies from `requirements.txt` and ensure an Odoo 18 instance is available.
2. Run `flake8` and `pytest` before every commit to catch linting and test issues.
3. Verify that your changes do not disrupt existing functionality. If your update alters behaviour, include appropriate tests and documentation.

## Commit Messages

Each commit summary **must** clearly describe the purpose of the change. Avoid generic messages like `update` or `fix`. Use concise phrasing that explains what was modified and why. Well-written summaries help reviewers understand your contribution and maintain a clean project history.

## Pull Requests

- Ensure your branch is up to date with the main branch before opening a pull request.
- Provide context in the pull request description describing the problem solved or feature added.
- Confirm all checks pass and that your commit summaries follow the policy above.

