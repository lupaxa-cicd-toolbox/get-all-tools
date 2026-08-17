"""Tool catalogue and download URL helpers.

Pipeline scripts live at ``src/pipeline.sh`` in each tool repository under
``lupaxa-cicd-toolbox`` (not at the repository root).
"""

from __future__ import annotations

ORG = "lupaxa-cicd-toolbox"
BASE_URL = f"https://raw.githubusercontent.com/{ORG}"
DEFAULT_REF = "master"
PIPELINE_FILE = "src/pipeline.sh"

# Pipeline tools under https://github.com/lupaxa-cicd-toolbox
TOOLS: list[str] = [
    "action-lint",
    "awesomebot",
    "bandit",
    "hadolint",
    "json-lint",
    "makefile-lint",
    "markdown-lint",
    "mypy",
    "perl-lint",
    "php-lint",
    "puppet-lint",
    "pur",
    "pycodestyle",
    "pydocstyle",
    "pylama",
    "pylint",
    "reek",
    "rubocop",
    "ruff",
    "shellcheck",
    "validate-citations-file",
    "yaml-lint",
]


def pipeline_url(tool_name: str, *, ref: str = DEFAULT_REF) -> str:
    """Return the raw GitHub URL for a tool's ``src/pipeline.sh``.

    Parameters
    ----------
    tool_name
        Repository name under lupaxa-cicd-toolbox.
    ref
        Git ref to fetch: branch name (default ``master``) or a release tag.
    """
    return f"{BASE_URL}/{tool_name}/{ref}/{PIPELINE_FILE}"
