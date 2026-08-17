"""Tests for the tool catalogue and URL helpers."""

from __future__ import annotations

from lupaxa.get_all_tools.tools import TOOLS, pipeline_url


def test_tools_includes_legacy_and_new() -> None:
    """Catalogue covers the original set plus makefile-lint, ruff, and mypy."""
    for name in (
        "action-lint",
        "shellcheck",
        "yaml-lint",
        "makefile-lint",
        "ruff",
        "mypy",
    ):
        assert name in TOOLS


def test_tools_are_unique_and_sorted_enough() -> None:
    """No duplicate tool names."""
    assert len(TOOLS) == len(set(TOOLS))
    assert len(TOOLS) >= 22


def test_pipeline_url_defaults_to_master() -> None:
    """Default ref is master HEAD."""
    url = pipeline_url("shellcheck")
    assert url == (
        "https://raw.githubusercontent.com/lupaxa-cicd-toolbox/shellcheck/master/src/pipeline.sh"
    )


def test_pipeline_url_accepts_release_tag() -> None:
    """A release tag can replace master in the raw URL."""
    url = pipeline_url("shellcheck", ref="v1.2.3")
    assert url == (
        "https://raw.githubusercontent.com/lupaxa-cicd-toolbox/shellcheck/v1.2.3/src/pipeline.sh"
    )
