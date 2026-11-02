---
name: color-palette-dfci
description: Dana-Farber Cancer Institute (DFCI) brand colors (primary, secondary, tertiary accent) as a hex dictionary, with rules for using them in charts. Use when the user asks for Dana-Farber or DFCI colors, or is making slides, posters, or figures for a Dana-Farber audience.
---

# Dana-Farber color palette

Brand colors from the [Dana-Farber Brand Resource Center](https://brand.dana-farber.org/). It shares its schema with `color-palette-tableau`: a flat dict of lowercase color name to hex string, so switching palettes only changes the dict name. The keys `blue`, `light blue`, `orange` and `grey` exist in both.

## Palette

```python
dfci = {
    # Primary
    'blue': '#00629b',          # PMS 3015, Dana-Farber Blue
    'light blue': '#41b6e6',    # PMS 298
    'orange': '#ffa300',        # PMS 137, Dana-Farber Orange
    'grey': '#63666a',          # PMS Cool Gray 10
    # Secondary
    'blue tint': '#4c91b9',     # PMS 3015, 70%
    'light blue tint': '#79caeb',  # PMS 298, 70%
    'orange tint': '#ffbe5f',   # PMS 137, 70%
    'grey tint': '#919496',     # PMS Cool Gray 10, 70%
    'dark blue': '#003354',     # PMS 540
    'dark grey': '#4d4d4f',     # PMS 7540
    # Tertiary accent (charts and graphs only)
    'teal': '#6dcdb8',          # PMS 3248
    'purple': '#9678d3',        # PMS 2655
    'green': '#789f90',         # PMS 624
    'pink': '#c9809e',          # PMS 7431
    'tan': '#ddcba4',           # PMS 468
}
```

## Ordering

For categories with no meaning attached, assign colors in this order (it follows the brand guide's 9–11 color chart examples):

```python
order = ['blue', 'orange', 'light blue', 'dark blue', 'teal', 'purple', 'tan', 'dark grey', 'green', 'pink']
```

## Neutrals

`grey` and `grey tint` are for reference lines, benchmarks, and de-emphasised data. `dark grey` is for text.

## Rules

- Reference colors by key (`dfci['blue']`), never by index or ad hoc hex codes.
- Give each category one color for the whole project. Define the mapping once as a dict keyed by category name and pass it straight to pandas (`color=colors`).
- Keep each figure to two to four colors, drawn from primary and secondary first.
- Tertiary colors are for charts and graphs only, and only when many colors are needed for contrast. Text, headlines and other graphic elements use primary and secondary only.
- Use a `tint` as the lighter partner of its base color rather than inventing one.

## Gotchas

- The brand guide's secondary swatches print wrong RGB values for the two blue tints: PMS 3015 (70%) lists `(0, 98, 155)`, which is the primary blue, and PMS 298 (70%) lists `(76, 145, 185)`, which is the 3015 tint's value. PMS 137 (70%) lists `(251, 190, 95)` against hex `#ffbe5f` (255, 190, 95). Use the hex values above; the correct RGB is computed from the hex (e.g. `#79caeb` is (121, 202, 235)).
- `light blue` (`#41b6e6`) is a primary color; `light blue tint` (`#79caeb`) is its 70% secondary. Don't confuse the two.
- `green` and `pink` here are muted tertiary accents, not the same hues as Tableau's `green` and `pink`.

## When to use

Dana-Farber slides, posters, and branded figures. For papers and general analysis figures, use `color-palette-tableau`.

## Source

- [Dana-Farber Cancer Institute Brand Resource Center](https://brand.dana-farber.org)
