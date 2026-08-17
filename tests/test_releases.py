"""Tests for resolving the latest GitHub release tag."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
import requests

from lupaxa.get_all_tools.releases import latest_release_tag


def test_release_tag_from_api_payload() -> None:
    """Use the tag_name from GitHub's latest release endpoint."""
    response = MagicMock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"tag_name": "v0.2.0"}

    with patch("lupaxa.get_all_tools.releases.requests.get", return_value=response) as get:
        tag = latest_release_tag("shellcheck")

    assert tag == "v0.2.0"
    get.assert_called_once()
    args, kwargs = get.call_args
    assert args[0] == (
        "https://api.github.com/repos/lupaxa-cicd-toolbox/shellcheck/releases/latest"
    )
    assert kwargs["timeout"] == 10


def test_missing_release_returns_none() -> None:
    """No published release means None so callers can fall back to master."""
    response = MagicMock()
    error = requests.HTTPError(response=response)
    response.raise_for_status.side_effect = error
    response.status_code = 404

    # Attach response to the error the way requests does
    error.response = response

    with patch("lupaxa.get_all_tools.releases.requests.get", return_value=response):
        assert latest_release_tag("shellcheck") is None


def test_non_404_http_errors_propagate() -> None:
    """Non-404 HTTP failures surface to the caller."""
    response = MagicMock()
    response.status_code = 500
    error = requests.HTTPError(response=response)
    error.response = response
    response.raise_for_status.side_effect = error

    with (
        patch("lupaxa.get_all_tools.releases.requests.get", return_value=response),
        pytest.raises(requests.HTTPError),
    ):
        latest_release_tag("shellcheck")
