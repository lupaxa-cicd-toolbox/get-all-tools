<p align="center">
    <a href="https://github.com/lupaxa-cicd-toolbox">
        <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/cicd-toolbox/readme-logo.png" alt="Organisation Logo" />
    </a>
</p>

<h1 align="center">get-all-tools</h1>

## Overview

A small Python helper that downloads every Lupaxa [CICD Toolbox](https://github.com/lupaxa-cicd-toolbox) pipeline script into `~/bin/cicd-toolbox` (ideally on your `$PATH`).

Each tool is saved as `cicd-<tool-name>` and marked executable.

> **Note:** Pipeline scripts live under `src/pipeline.sh` in each tool repository (not at the repository root). For example, with default ref `master`:
>
> `https://raw.githubusercontent.com/lupaxa-cicd-toolbox/shellcheck/master/src/pipeline.sh`

## Requirements

- Python 3.13+
- [`requests`](https://pypi.org/project/requests/)

## Usage

```bash
pip install -e ".[dev]"
cicd-toolbox-sync
```

Or without installing the console script:

```bash
python -m lupaxa.get_all_tools
```

Runtime-only install (no editable package):

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m lupaxa.get_all_tools
```

After a successful run you can invoke tools locally, for example:

```bash
cicd-shellcheck
cicd-ruff
```

## Source selection

By default each pipeline is fetched from the `master` branch.

| Flag        | Behaviour                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| *(none)*    | `master` HEAD                                                                                                                                       |
| `--latest`  | Latest **stable** GitHub release tag per tool (`/releases/latest`). If a tool has no releases yet, falls back to `master` with a warning on stderr. |
| `--ref REF` | Explicit branch or tag for **every** tool (e.g. `--ref v0.1.0`)                                                                                     |

`--latest` and `--ref` are mutually exclusive.

```bash
cicd-toolbox-sync --latest
cicd-toolbox-sync --ref v0.1.0
```

## Current toolset

| Name                                                                                      | Purpose                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [action-lint](https://github.com/lupaxa-cicd-toolbox/action-lint)                         | Validate GitHub Actions workflows with [actionlint](https://github.com/rhysd/actionlint). |
| [awesomebot](https://github.com/lupaxa-cicd-toolbox/awesomebot)                           | Link-check files with [awesome_bot](https://rubygems.org/gems/awesome_bot).               |
| [bandit](https://github.com/lupaxa-cicd-toolbox/bandit)                                   | Find security issues in Python with [bandit](https://pypi.org/project/bandit/).           |
| [hadolint](https://github.com/lupaxa-cicd-toolbox/hadolint)                               | Lint Dockerfiles with [hadolint](https://github.com/hadolint/hadolint).                   |
| [json-lint](https://github.com/lupaxa-cicd-toolbox/json-lint)                             | Validate JSON with [jq](https://stedolan.github.io/jq/).                                  |
| [makefile-lint](https://github.com/lupaxa-cicd-toolbox/makefile-lint)                     | Lint Makefiles with [checkmake](https://github.com/checkmake/checkmake).                  |
| [markdown-lint](https://github.com/lupaxa-cicd-toolbox/markdown-lint)                     | Lint Markdown with [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli). |
| [mypy](https://github.com/lupaxa-cicd-toolbox/mypy)                                       | Type-check Python with [mypy](https://mypy.readthedocs.io/).                              |
| [perl-lint](https://github.com/lupaxa-cicd-toolbox/perl-lint)                             | Lint Perl with the native Perl checker.                                                   |
| [php-lint](https://github.com/lupaxa-cicd-toolbox/php-lint)                               | Lint PHP with the native PHP checker.                                                     |
| [puppet-lint](https://github.com/lupaxa-cicd-toolbox/puppet-lint)                         | Lint Puppet with [puppet-lint](https://rubygems.org/gems/puppet-lint).                    |
| [pur](https://github.com/lupaxa-cicd-toolbox/pur)                                         | Check `requirements.txt` updates with [pur](https://pypi.org/project/pur/).               |
| [pycodestyle](https://github.com/lupaxa-cicd-toolbox/pycodestyle)                         | Style-check Python with [pycodestyle](https://pypi.org/project/pycodestyle/).             |
| [pydocstyle](https://github.com/lupaxa-cicd-toolbox/pydocstyle)                           | Check Python docstrings with [pydocstyle](https://pypi.org/project/pydocstyle/).          |
| [pylama](https://github.com/lupaxa-cicd-toolbox/pylama)                                   | Run the [pylama](https://pypi.org/project/pylama/) code audit suite.                      |
| [pylint](https://github.com/lupaxa-cicd-toolbox/pylint)                                   | Analyse Python with [pylint](https://pypi.org/project/pylint/).                           |
| [reek](https://github.com/lupaxa-cicd-toolbox/reek)                                       | Find Ruby code smells with [reek](https://rubygems.org/gems/reek).                        |
| [rubocop](https://github.com/lupaxa-cicd-toolbox/rubocop)                                 | Lint Ruby with [rubocop](https://rubygems.org/gems/rubocop).                              |
| [ruff](https://github.com/lupaxa-cicd-toolbox/ruff)                                       | Lint Python with [Ruff](https://docs.astral.sh/ruff/).                                    |
| [shellcheck](https://github.com/lupaxa-cicd-toolbox/shellcheck)                           | Analyse shell scripts with [ShellCheck](https://github.com/koalaman/shellcheck).          |
| [validate-citations-file](https://github.com/lupaxa-cicd-toolbox/validate-citations-file) | Validate `CITATION.cff` with [cffconvert](https://pypi.org/project/cffconvert/).          |
| [yaml-lint](https://github.com/lupaxa-cicd-toolbox/yaml-lint)                             | Lint YAML with [yamllint](https://pypi.org/project/yamllint/).                            |

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
