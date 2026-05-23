---
name: python-docstrings
description: Write or update Python function docstrings in Google-style format with Args, Returns, and Raises sections. Use when writing new functions, adding missing docstrings, or updating existing ones to match project conventions.
---

# Docstring format

Write or update Python function docstrings using the following style conventions.

## Structure

- Opening `"""` on the line immediately after the function signature; summary text starts on the next line as `"""`
- One or two sentences summarizing what the function does; ends with a period
- Blank line after the summary, before the first section
- Sections: `Args:`, `Raises:`, `Returns:` — include only sections that apply
- No blank lines between sections
- Closing `"""` on its own line, indented to match the function body

## Args section

- Each parameter: `    name (type): Description.`
- Types use lowercase Python built-in generics: `list[dict]`, `str`, `bool`, `typing.Any`
- Note default values inline in the description: `(default: "id")`

## Raises section

- Format: `    ExceptionType: Description.`
- Omit entirely if the function raises no exceptions

## Returns section

- Format: `    type: Description.` (no parameter name)
- Optional: `    type or None: Description.`

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

    Raises:
        ValueError: If the number of results is not exactly 1, and strict is enabled.

    Returns:
        dict or None: A dictionary of the matching record, or None if no matches are found.
    """
```
