---
name: color-palette-tableau
description: Tableau10 (the 2016 "new Tableau 10") and Tableau20 color palettes as hex dictionaries, with rules for assigning colors to categories. Use when choosing colors for a chart, figure, or slide in matplotlib, pandas, or any plotting library, unless the user asks for Dana-Farber colors (see color-palette-dfci).
---

# Tableau color palette

Default palette for papers and general figures. It shares its schema with `color-palette-dfci`: a flat dict of lowercase color name to hex string, so switching palettes only changes the dict name.

## Palette

```python
tableau10 = {
    'blue': '#4e79a7', 'orange': '#f28e2b', 'red': '#e15759',
    'cyan': '#76b7b2', 'green': '#59a14f', 'yellow': '#edc948',
    'purple': '#b07aa1', 'pink': '#ff9da7', 'brown': '#9c755f',
    'grey': '#bab0ac', 'white': '#f0f0f0',
}
```

Tableau20 adds a light partner for each hue. Use it when a category needs a lighter shade (a subset, a secondary series, a partial bar):

```python
tableau20 = {
    'blue': '#4e79a7', 'light blue': '#a0cbe8',
    'orange': '#f28e2b', 'light orange': '#ffbe7d',
    'green': '#59a14f', 'light green': '#8cd17d',
    'yellow': '#b6992d', 'light yellow': '#f1ce63',
    'teal': '#499894', 'light teal': '#86bcb6',
    'red': '#e15759', 'light red': '#ff9d9a',
    'grey': '#79706e', 'light grey': '#bab0ac',
    'pink': '#d37295', 'light pink': '#fabfd2',
    'purple': '#b07aa1', 'light purple': '#d4a6c8',
    'brown': '#9d7660', 'light brown': '#d7b5a6',
}
```

## Ordering

When categories have no meaning attached, assign colors in this order:

```python
order = ['blue', 'orange', 'red', 'cyan', 'green', 'yellow', 'purple', 'pink', 'brown', 'grey']
```

## Neutrals

`grey` is for reference lines, benchmarks, and de-emphasised data. `white` (`#f0f0f0`) is a light background fill, not a data color.

## Rules

- Reference colors by key (`tableau10['blue']`), never by index or ad hoc hex codes.
- Give each category one color for the whole project. Define the mapping once as a dict keyed by category name and pass it straight to pandas (`color=colors`).
- Keep each figure to two to four colors.
- Pair a color with its `light` variant from `tableau20` rather than inventing a tint.

## Gotchas

- `tableau10` and `tableau20` use different hexes for the same name: Tableau10 `yellow` is `#edc948` and Tableau20 `yellow` is `#b6992d`; Tableau10 `grey` is `#bab0ac` and Tableau20 `grey` is `#79706e`. Don't mix a color from one dict with a `light` partner from the other; take both from `tableau20`.
- Tableau10 calls the blue-green `cyan`; Tableau20 calls it `teal`.
- Tableau10 `pink` is `#ff9da7`. Some copies list `#e19da7`, which is a typo.

## Source

- [Tableau 10 and 20 in ggthemes](https://jrnold.github.io/ggthemes/reference/tableau_color_pal.html)
- [Colors upgrade in Tableau 10](https://www.tableau.com/blog/colors-upgrade-tableau-10-56782)
