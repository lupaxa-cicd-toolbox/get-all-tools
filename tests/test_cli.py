"""Tests for CLI argument parsing and download ref selection."""

from __future__ import annotations

from unittest.mock import patch

from lupaxa.get_all_tools.cli import build_parser, resolve_download_ref


def test_parser_defaults_to_master() -> None:
    """Without flags, downloads come from master."""
    args = build_parser().parse_args([])
    assert args.latest is False
    assert args.ref is None


def test_parser_accepts_latest_and_explicit_ref() -> None:
    """--latest and --ref are mutually exclusive options."""
    parser = build_parser()
    assert parser.parse_args(["--latest"]).latest is True
    assert parser.parse_args(["--ref", "v9.9.9"]).ref == "v9.9.9"


def test_resolve_download_ref_prefers_explicit_ref() -> None:
    """An explicit --ref wins without calling the releases API."""
    with patch("lupaxa.get_all_tools.cli.latest_release_tag") as latest:
        assert resolve_download_ref("shellcheck", latest=False, ref="v1.0.0") == "v1.0.0"
        latest.assert_not_called()


def test_resolve_download_ref_uses_latest_when_available() -> None:
    """--latest uses the published release tag when one exists."""
    with patch("lupaxa.get_all_tools.cli.latest_release_tag", return_value="v3.0.0"):
        assert resolve_download_ref("shellcheck", latest=True, ref=None) == "v3.0.0"


def test_resolve_download_ref_falls_back_to_master_without_release() -> None:
    """--latest with no releases falls back to master."""
    with patch("lupaxa.get_all_tools.cli.latest_release_tag", return_value=None):
        assert resolve_download_ref("shellcheck", latest=True, ref=None) == "master"


def test_resolve_download_ref_defaults_to_master() -> None:
    """Default mode is master HEAD."""
    assert resolve_download_ref("shellcheck", latest=False, ref=None) == "master"
