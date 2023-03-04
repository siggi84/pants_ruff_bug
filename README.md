# README: Pants-Ruff Bug?
## Introduction

This document describes a potential bug related to the import order in hello_ruff.py when using the ruff command and pants command to sort the order.

## The Bug
When running the command below from src/python, the import order in hello_ruff.py changes as expected:

```shell
> ruff --config ../../ruff.toml . --fix
```

Before running the above command, the import order in hello_ruff.py is:

```python
from hello_user import hello_user
from scipy.special import cbrt
```

After running the above command, the import order in hello_ruff.py becomes:

```python
from scipy.special import cbrt

from hello_user import hello_user
```

However, when running the following command, scipy is treated as a first party import and the import order remains unchanged:

```shell
> pants fmt fix lint ::
```

As a result, the import order in hello_ruff.py remains as:

```python

from hello_user import hello_user
from scipy.special import cbrt
```

Furthermore, if these two commands are run alternately, the import order will alternate between the two forms described above.
