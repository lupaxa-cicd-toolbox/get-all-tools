"""Resolve the latest published GitHub release tag for a tool repo."""

from __future__ import annotations

import requests
from requests.exceptions import HTTPError

from .tools import ORG

TIMEOUT = 10  # seconds


def latest_release_tag(tool_name: str) -> str | None:
    """
    Return the latest non-prerelease tag for ``tool_name``, or None if none.

    Uses GitHub's ``/releases/latest`` endpoint. A 404 means the repository has
    no published releases yet.
    """
    url = f"https://api.github.com/repos/{ORG}/{tool_name}/releases/latest"
    response = requests.get(url, timeout=TIMEOUT)
    try:
        response.raise_for_status()
    except HTTPError as exc:
        status = getattr(exc.response, "status_code", None)
        if status == 404:
            return None
        raise
    payload = response.json()
    tag = payload.get("tag_name")
    if not isinstance(tag, str) or not tag:
        return None
    return tag
