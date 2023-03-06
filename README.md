# Ruff integration in pantsbuild only fails on auto-fixable errors
## Introduction
This document aims to clarify a potential bug related to the Ruff linter integration in the Pantsbuild system. The bug occurs when the linter fails to detect non-auto-fixable linting errors and falsely allows the build to pass. This behaviour is also inconsistent with how the flake8 linter behaves in pants.

## Description
The Ruff linter integration in Pantsbuild only fails the build when it encounters a linting rule that it can automatically fix. If the linter comes across a rule that it cannot fix on its own, it falsely allows the build to pass. This behavior is not desirable and can lead to potentially unnoticed linting errors.

## Steps
To illustrate the issue, let us take the example of a Python file called hello_ruff.py that has two different linting rule violations. The first violation is a fixable "unused-import" rule (F401), and the second violation is an unfixable "import-star-usage" rule (F405).

When we run the command `pants lint ::` with the following pyproject.toml file:
```
[tool.ruff]
select = ["F401"]
```
and the following .flake8:
```
[flake8]
select: F401
```
we expect both the Flake8 and Ruff linters to fail, which is the observed behavior:
```shell
✕ flake8 failed.
✕ ruff failed.
```
However, if we change pyproject.toml and .pants to select the (unfixable) F405 rule and run the same command again `pants lint ::`, we see that Flake8 fails as expected, but Ruff succeeds, falsely allowing the build to pass. 
```
✕ flake8 failed.
✓ ruff succeeded.
```
This behavior is the bug that needs to be fixed.
