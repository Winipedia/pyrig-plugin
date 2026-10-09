# pyrig-plugin

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-plugin/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-plugin/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-plugin/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-plugin/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-plugin)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://prek.j178.dev/reference/built-in-hooks/#fix-byte-order-marker)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/%F0%9F%8C%88-zizmor-white?labelColor=white)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-case-conflict)
[![DeadCodeChecker](https://img.shields.io/badge/dead--code-vulture-blue)](https://github.com/jendrikseipp/vulture)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://prek.j178.dev/reference/built-in-hooks/#end-of-file-fixer)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://prek.j178.dev/reference/built-in-hooks/#mixed-line-ending)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://prek.j178.dev/reference/built-in-hooks/#pretty-format-json)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-json)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-added-large-files)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://prek.j178.dev/reference/built-in-hooks/#check-merge-conflict)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks#name-tests-test)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace-orange)](https://prek.j178.dev/reference/built-in-hooks/#trailing-whitespace)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![YAMLLinter](https://img.shields.io/badge/YAML-ryl-red)](https://github.com/owenlamont/ryl)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Winipedia/pyrig/main/docs/assets/badge.json)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/pyrig-plugin?style=social)](https://github.com/Winipedia/pyrig-plugin)
[![VersionControlHookManager](https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge.svg)](https://github.com/j178/prek)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- project-info -->
[![DocsBuilder](https://img.shields.io/badge/Documentation-zensical-326CE5)](https://Winipedia.github.io/pyrig-plugin)
[![PackageIndex](https://img.shields.io/pypi/v/pyrig-plugin?logo=pypi&logoColor=white)](https://pypi.org/project/pyrig-plugin)
[![ProgrammingLanguage](https://img.shields.io/pypi/pyversions/pyrig-plugin)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/pyrig-plugin)](https://github.com/Winipedia/pyrig-plugin/blob/main/LICENSE)

---

> A pyrig plugin for pyrig plugins.

---

## Overview

`pyrig-plugin` is a [pyrig](https://github.com/Winipedia/pyrig) plugin for
projects that are themselves pyrig plugins. Pyrig discovers plugin implementations
across installed packages through their declared dependencies, so a package
that extends pyrig must declare pyrig as a runtime dependency.
It also includes [`pyrig-fixtures`](https://Winipedia.github.io/pyrig-fixtures),
providing reusable pytest fixtures to plugin projects.

## What it adds

- **pyrig runtime dependency** — It declares `pyrig` as a runtime dependency for
the plugin project.
- **Shared pytest fixtures** — It depends on
  [`pyrig-fixtures`](https://Winipedia.github.io/pyrig-fixtures), making its
  reusable pytest fixtures available to plugin projects.
- **deptry configuration** — It ignores `pyrig` in deptry so the runtime
  dependency is not reported as unused.
- **PyPI integration** — It depends on [`pyrig-pypi`](https://Winipedia.github.io/pyrig-pypi),
  so installing `pyrig-plugin` also installs that plugin.
- **pyrig project keyword** — It adds `pyrig` to the project keywords written
  to `pyproject.toml`.

## Usage

```bash
uv add pyrig-plugin --dev
uv run pyrig sync
```

## Documentation

Full documentation, including the auto-generated API reference, is available on
the [documentation site](https://Winipedia.github.io/pyrig-plugin).
