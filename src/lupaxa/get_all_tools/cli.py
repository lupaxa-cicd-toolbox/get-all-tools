"""CLI entry point for downloading CICD Toolbox pipelines."""

from __future__ import annotations

import argparse
import os
import sys

import requests
from requests.exceptions import HTTPError, Timeout

from .releases import latest_release_tag
from .tools import DEFAULT_REF, TOOLS, pipeline_url

FILE_PATH: str = os.path.join(os.environ["HOME"], "bin", "cicd-toolbox")
TIMEOUT = 10  # seconds


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="cicd-toolbox-sync",
        description=(
            "Download Lupaxa CICD Toolbox pipeline scripts (src/pipeline.sh) "
            "into ~/bin/cicd-toolbox."
        ),
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument(
        "--latest",
        action="store_true",
        help=(
            "Download from each tool's latest GitHub release tag "
            "(falls back to master if a tool has no releases)."
        ),
    )
    source.add_argument(
        "--ref",
        metavar="REF",
        help="Download from an explicit git ref (branch or tag) for every tool.",
    )
    return parser


def resolve_download_ref(
    tool_name: str,
    *,
    latest: bool,
    ref: str | None,
) -> str:
    """
    Choose the git ref used when downloading ``tool_name``.

    Precedence: explicit ``ref``, then latest release (if requested), else master.
    """
    if ref is not None:
        return ref
    if latest:
        tag = latest_release_tag(tool_name)
        if tag is None:
            print(
                f"No release found for {tool_name}; falling back to {DEFAULT_REF}",
                file=sys.stderr,
            )
            return DEFAULT_REF
        return tag
    return DEFAULT_REF


def download_tool(tool_name: str, *, ref: str) -> None:
    """
    Download the tool's pipeline script and save it under ~/bin/cicd-toolbox.

    Parameters
    ----------
    tool_name
        Repository / tool name under lupaxa-cicd-toolbox.
    ref
        Branch or tag to fetch.
    """
    url: str = pipeline_url(tool_name, ref=ref)
    destination: str = os.path.join(FILE_PATH, f"cicd-{tool_name}")

    try:
        response: requests.Response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        with open(destination, "wb") as file:
            file.write(response.content)
        os.chmod(destination, 0o700)
        print(f"Successfully downloaded {tool_name}@{ref}")

    except HTTPError as http_err:
        print(f"HTTP error occurred while downloading {tool_name}@{ref}: {http_err}")
    except Timeout as timeout_err:
        print(f"Timeout error occurred while downloading {tool_name}@{ref}: {timeout_err}")
    except OSError as err:
        print(f"An error occurred while downloading {tool_name}@{ref}: {err}")


def main(argv: list[str] | None = None) -> None:
    """Create ~/bin/cicd-toolbox if needed and download all pipeline tools."""
    args = build_parser().parse_args(argv)
    try:
        os.makedirs(FILE_PATH, exist_ok=True)
        for tool in TOOLS:
            ref = resolve_download_ref(tool, latest=args.latest, ref=args.ref)
            download_tool(tool, ref=ref)
    except OSError as exc:
        print(f"An error occurred while setting up tools directory or downloading tools: {exc}")
        sys.exit(1)
    except HTTPError as exc:
        print(f"Failed to resolve a release tag: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
