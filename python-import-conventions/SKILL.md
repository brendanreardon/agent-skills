---
name: python-import-conventions
description: Import root modules/packages (e.g. `import pathlib`) and reference members via their full dotted path (`pathlib.Path`) instead of importing specific names out of them (`from pathlib import Path`). Use whenever writing new Python import statements or editing existing ones, for standard library, third-party, and local modules alike.
---

# Import Root Modules, Not Names

Import the module with a plain `import`, then reference every member through its full dotted path at the point of use. Avoid pulling specific names out with `from module import name`.

## Rule

- Write `import module` (e.g. `import pathlib`, `import os`, `import json`), never `from module import name` (e.g. `from pathlib import Path`).
- Reference the member through the full dotted path every time it's used:
  `pathlib.Path(...)`, `os.path.join(...)`, `json.JSONDecodeError`.
- For a member that lives in a submodule, import the submodule by its full dotted name, then use the full path: `import collections.abc` then
  `collections.abc.Mapping`, not `from collections.abc import Mapping`.
- This applies the same way to standard library, third-party, and local project modules.

## Gotcha: importing a package does not import its submodules

`import package` only binds what the package's `__init__.py` loads itself. Reaching a submodule through it fails unless something else happened to import that submodule first:

```python
import xml
xml.etree.ElementTree       # AttributeError: module 'xml' has no attribute 'etree'

import xml.etree.ElementTree
xml.etree.ElementTree.parse(...)   # works
```

`import collections` followed by `collections.abc` may appear to work only because the interpreter loaded `collections.abc` at startup. Don't rely on that; always import the submodule you use. `os.path` is the one common exception (`os` imports it itself), so `import os` is enough for it.

## Aliased imports (allowed exception)

Well-known short aliases for common ecosystem packages are permitted, since
they still import the root/entry-point object under a short name rather than
pulling individual names out of it:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Still reference every member off the alias — `np.array(...)`,
`pd.DataFrame(...)` — never `from numpy import array`.

## Other exceptions

A few import forms can't structurally take a "root module, dotted path"
form. These are not violations of the rule:

- `from __future__ import annotations` (and other `__future__` imports) —
  required syntax; there is no root-module form for these.
- Relative imports within a package (`from . import sibling_module`,
  `from .submodule import helper`) — package-relative imports have no
  equivalent root-module form; leave these as conventional relative imports.

`if typing.TYPE_CHECKING:` blocks follow the same rule as everywhere else: `import module` and dotted references in annotations. Only use `from module import Name` there if the dotted form causes a circular-import error.

## Example

Before:
```python
from pathlib import Path
from collections.abc import Mapping

p = Path("foo")
m: Mapping = {}
```

After:
```python
import collections.abc
import pathlib

p = pathlib.Path("foo")
m: collections.abc.Mapping = {}
```

Allowed alias exception:
```python
import numpy as np

arr = np.array([1, 2, 3])
```
