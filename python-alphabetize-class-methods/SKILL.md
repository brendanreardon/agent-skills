---
name: python-alphabetize-class-methods
description: Sorts method definitions within each Python class into strict alphabetical (A-Z, case-sensitive, ASCII) order. Use whenever writing or editing Python code that defines a class with more than one method — this includes new classes being written from scratch and existing classes being edited or refactored. Also trigger on explicit requests to "alphabetize", "sort", or "reorganize" methods/functions in a class.
---

# Alphabetize Class Methods

Whenever Python code is written or edited that defines a class containing more
than one method, reorder the methods within that class body into strict
alphabetical order before presenting the final code.

## Sorting rule

- Sort key is the literal method name string, compared case-sensitively by
  codepoint (Python's default `str` ordering / ASCII order).
- Do **not** special-case `__init__`, other dunder methods, or
  `_private`/`__mangled` methods. Sort every method name the same way,
  including `__init__`.
- A side effect of ASCII order: `_` (underscore, codepoint 95) sorts before
  lowercase letters (97+). This means dunder and underscore-prefixed methods
  will generally end up before plain public methods — but this falls out of
  the sort automatically. Don't write separate grouping logic to enforce it,
  and don't assume `__init__` lands first among dunders (e.g. `__eq__` sorts
  before `__init__`).
- Methods that share a name (a `@property` and its `@x.setter` /
  `@x.deleter`, or `@typing.overload` stubs and their implementation) keep
  their original relative order. Treat the sort as stable: getter, then
  setter, then deleter; overload stubs before the implementation.

## What moves together as a unit

When a method moves, everything that belongs to it moves with it, in this
order, still directly attached:
1. Any comment lines immediately above the method (no blank line between them)
2. Decorators (`@property`, `@staticmethod`, `@classmethod`, custom decorators)
3. The `def` line and full method body, including its docstring

## What does NOT get reordered

- Class-level attributes/constants defined before the methods — leave these
  where they are, at the top of the class body.
- Class-body statements that refer to methods, such as aliases
  (`__radd__ = __add__`) and `area = property(_get_area)`. Leave them after all the methods, in their
  original order, so every name they use is already defined.
- Methods in different classes — sort each class independently; never
  interleave methods across classes.
- Nested classes — apply this same sort recursively to their bodies too, but
  keep each nested class's methods separate from the outer class's.

## Formatting

Preserve PEP 8 spacing: one blank line between methods inside a class, two
blank lines between top-level classes/functions.

## Before sorting: check for order-sensitive patterns

Most Python classes don't care about method definition order, so most of the
time just sort silently as a normal part of writing/editing the code — no
need to ask permission. But before reordering, scan for these specific
patterns where order *can* matter, and if found, stop and flag it to the
user (name the methods involved and why) instead of silently reordering:

- `@functools.singledispatchmethod` and its `@x.register` overloads — these
  rely on registration order at class-definition time.
- `__init_subclass__`, metaclass hooks, or any class-body code that runs at
  definition time and references sibling methods defined earlier in the file.
- Any method that dynamically looks up a *later*-defined sibling by name at
  class-definition time (rare, but reorder-unsafe if present).

If none of these patterns are present, proceed with the sort without asking.

## Example

Before:
```python
class Widget:
    def render(self):
        ...

    def __init__(self, name):
        self.name = name

    def _validate(self):
        ...

    def __repr__(self):
        return f"Widget({self.name})"
```

After:
```python
class Widget:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Widget({self.name})"

    def _validate(self):
        ...

    def render(self):
        ...
```
