# README: Pants-Ruff Config Discovery bug
## Introduction

This document explains a potential bug related to the config discovery behind ruff in pants.

## Description
When running the command `pants fmt fix lint ::` with the following pyproject.toml file:
```
[tool.ruff]
select = ["E", "F"]
ignore = []

fixable = ["A", "B", "C", "D", "E", "F"]
unfixable = []

[tool.ruff.per-file-ignores]
"src/python/hello_ruff.py" = ["F401"]
```
and the following imports in src/python/hello_ruff.py file:
```
import numpy
from scipy.special import cbrt
from hello_user import hello_user
```
The command does not make any changes, as expected.

However, if we remove the [tool.ruff] section from the pyproject.toml file, leaving only:
```
[tool.ruff.per-file-ignores]
"src/python/hello_ruff.py" = ["F401"]
```
and run the same command pants `fmt fix lint ::`, the unused numpy import is removed and the file becomes:
```
from scipy.special import cbrt
from hello_user import hello_user
```
This indicates that Pants(with ruff) is not discovering the configuration file when the [tool.ruff] section is missing, causing it to miss the sub-table [tool.ruff.per-file-ignores] (or any sub-table).
