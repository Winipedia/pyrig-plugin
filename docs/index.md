# Home

<!-- project-status -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-plugin/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/pyrig-plugin/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/pyrig-plugin/release.yml?label=CD&logo=github)](https://github.com/Winipedia/pyrig-plugin/actions/workflows/release.yml)
[![ProjectTester](https://codecov.io/gh/Winipedia/pyrig-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/Winipedia/pyrig-plugin)
<!-- code-quality -->
[![ByteOrderMarkerFormatter](https://img.shields.io/badge/BOM-fix--byte--order--marker-orange)](https://github.com/j178/prek)
[![CICDLinter](https://img.shields.io/badge/CI/CD-actionlint-blue)](https://github.com/rhysd/actionlint)
[![CICDSecurityChecker](https://img.shields.io/badge/CI/CD--security-zizmor-yellow)](https://github.com/zizmorcore/zizmor)
[![CaseConflictChecker](https://img.shields.io/badge/case--conflict-check--case--conflict-blue)](https://github.com/j178/prek)
[![DeadCodeChecker](https://img.shields.io/badge/dead--code-vulture-blue)](https://github.com/jendrikseipp/vulture)
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![EndOfFileFormatter](https://img.shields.io/badge/EOF-end--of--file--fixer-orange)](https://github.com/j178/prek)
[![EndOfLineFormatter](https://img.shields.io/badge/EOL-mixed--line--ending-orange)](https://github.com/j178/prek)
[![JSONFormatter](https://img.shields.io/badge/JSON-pretty--format--json-orange)](https://github.com/j178/prek)
[![JSONLinter](https://img.shields.io/badge/JSON-check--json-blue)](https://github.com/j178/prek)
[![LargeFileChecker](https://img.shields.io/badge/large--files-check--added--large--files-blue)](https://github.com/j178/prek)
[![MarkdownLinter](https://img.shields.io/badge/Markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![MergeConflictChecker](https://img.shields.io/badge/merge--conflict-check--merge--conflict-blue)](https://github.com/j178/prek)
[![ModuleTestNamingChecker](https://img.shields.io/badge/test--naming-name--tests--test-blue)](https://github.com/pre-commit/pre-commit-hooks)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SecretsChecker](https://img.shields.io/badge/secrets-detect--secrets-blue)](https://github.com/Yelp/detect-secrets)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![ShellFormatter](https://img.shields.io/badge/shell-shfmt-orange)](https://github.com/mvdan/sh)
[![ShellLinter](https://img.shields.io/badge/shell-shellcheck-blue)](https://github.com/koalaman/shellcheck)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TOMLLinter](https://img.shields.io/badge/TOML-tombi-blueviolet)](https://github.com/tombi-toml/tombi)
[![TrailingWhitespaceFormatter](https://img.shields.io/badge/whitespace-trailing--whitespace-orange)](https://github.com/j178/prek)
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

Drop-in [pyrig](https://github.com/Winipedia/pyrig) plugin for projects that
are themselves pyrig plugins. Pyrig discovers plugin implementations in installed
packages that declare pyrig as a dependency. This plugin ensures the plugin
project has that required runtime dependency, while this plugin itself is
installed as a development dependency.
It depends on [`pyrig-pypi`](https://Winipedia.github.io/pyrig-pypi), so
installing `pyrig-plugin` also installs that plugin.

## Installation

```bash
uv add pyrig-plugin --dev
uv run pyrig sync
```

## How it works

The plugin subclasses pyrig's `Pyrigger` and sets `pyrig` as the project's
runtime dependency. When `pyrig sync` is invoked, the project's `pyproject.toml`
declares `pyrig` instead of `pyrig-runtime`. Since `pyrig` itself depends on
`pyrig-runtime`, plugin projects only need to declare `pyrig`.
When managing `pyproject.toml`, the plugin also adds `pyrig` to the project
keywords.

It also adds pyrig as an ignore entry to the `deptry` tool entry in the `pyproject.toml`.
This also happens automatically when `pyrig sync` is run.
This is needed so `deptry` does not mistakenly report `pyrig` as an unused dependency.

## API Reference

For class- and method-level details, see the [API Reference](api.md), generated
automatically from the source.
