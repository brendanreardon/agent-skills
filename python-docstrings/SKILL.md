---
name: python-docstrings
description: Write or update Python function and method docstrings in Google-style format with Args, Returns, and Raises sections. Use when writing new functions or methods, adding missing docstrings, or updating existing ones, unless the project already uses a different docstring style.
---

# Docstring format

Write or update Python function and method docstrings using the following conventions. If the project already uses another style (NumPy, reST), match the project instead.

## Structure

- Put the opening `"""` on its own line, directly below the `def` line. The summary starts on the line after it.
- One or two sentences summarizing what the function does; ends with a period
- Blank line after the summary, before the first section
- Sections, in this order: `Args:`, `Returns:` (or `Yields:` for generators), `Raises:`. Include only sections that apply.
- One blank line between sections
- Closing `"""` on its own line, indented to match the function body

## Args section

- Each parameter: `    name (type): Description.`
- Leave out `self` and `cls`.
- Types use lowercase Python built-in generics: `list[dict]`, `str`, `bool`, `typing.Any`
- Write unions with `|`: `str | pathlib.Path`, `dict | None`.
- Note default values inline in the description: `(default: "id")`

## Returns section

- Format: `    type: Description.` (no parameter name)
- Omit entirely if the function returns `None`.
- For generators, use `Yields:` with the same format instead.

## Raises section

- Format: `    ExceptionType: Description.`
- Omit entirely if the function raises no exceptions

## Gotchas

- The summary never goes on the same line as the opening `"""`.

## Example

```python
def get_record_by_key_value(records: list[dict], value: typing.Any, key: str = "id", strict: bool = True) -> dict | None:
    """
    Retrieves a single record where a specified key matches the given value.
    Raises ValueError if zero or multiple matches are found, unless strict is False.

    Args:
        records (list[dict]): A list of dictionaries to search.
        value (typing.Any): The value to match.
        key (str): The key to check (default: "id").
        strict (bool): If True, raise a ValueError when not exactly one match is found.

    Returns:
        dict | None: A dictionary of the matching record, or None if no matches are found.

    Raises:
        ValueError: If the number of results is not exactly 1, and strict is enabled.
    """
```
