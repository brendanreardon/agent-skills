---
name: python-import-conventions
description: Import root modules/packages (e.g. `import pathlib`) and reference members via their full dotted path (`pathlib.Path`) instead of importing specific names out of them (`from pathlib import Path`). Use whenever writing new Python import statements or editing existing ones, for standard library, third-party, and local modules alike.
---

# Import Root Modules, Not Names

Import the root module or package with a plain `import`, then reference every
member through its full dotted path at the point of use. Avoid pulling
specific names out with `from module import name`.

## Rule

- Write `import module` (e.g. `import pathlib`, `import os`, `import json`),
  never `from module import name` (e.g. `from pathlib import Path`).
- Reference the member through the full dotted path every time it's used:
  `pathlib.Path(...)`, `os.path.join(...)`, `json.JSONDecodeError`.
- This applies regardless of nesting depth — `import collections` then
  `collections.abc.Mapping`, not `from collections.abc import Mapping`.
- This applies the same way to standard library, third-party, and local
  project modules.

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
- `if typing.TYPE_CHECKING:` guarded blocks — prefer `import module` over
  `from module import Name` where practical, but a name imported purely for
  a string-quoted type annotation (never referenced as a runtime dotted
  path) may reasonably use `from module import Name`.

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
import pathlib
import collections

p = pathlib.Path("foo")
m: collections.abc.Mapping = {}
```

Allowed alias exception:
```python
import numpy as np

arr = np.array([1, 2, 3])
```
