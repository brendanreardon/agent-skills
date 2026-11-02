---
name: python-figure-structure
description: House style and step order for matplotlib/pandas figures — Arial 6–7 pt, sizes in millimetres, no spines or tick marks, and export to eps, pdf, png, svg plus a PowerPoint-sized png. Use whenever writing or editing Python code that makes a plot, chart, graph or histogram, calls savefig, or produces a figure for a paper, poster or slides, even if the user doesn't mention style or export.
---

# Figure structure

Every figure follows the same order, whether it is a notebook cell or a plotting function. Use matplotlib, with pandas `.plot(kind=..., ax=ax)` for bars and histograms. Don't use seaborn.

## Setup (once, at the top of the file)

Fonts and sizes are set here, not per figure:

```python
import pathlib

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import PIL.Image

matplotlib.rcParams["font.family"] = "Arial"
matplotlib.rcParams["font.size"] = 6
matplotlib.rcParams["axes.titlesize"] = 7
matplotlib.rcParams["axes.labelsize"] = 6
matplotlib.rcParams["legend.fontsize"] = 6
```

- For large, full-page figures, set all four sizes to 7. Small annotations (value labels, notes) use `fontsize=5`.
- In notebooks, add `%matplotlib inline`.
- Define `remove_spines` and `save_figure` once. Copy them from `scripts/figure_helpers.py`.
- For a new notebook, start from `assets/figure_template.py`, which has every step below filled in and runs as is.

## Checklist

Work through these in order. Each is a comment-headed block.

- [ ] 1. **Color palette.** Name the colors by category, taking values from `color-palette-tableau` (default) or `color-palette-dfci` (Dana-Farber material).
  ```python
  colors = {
      'Market authorisation and reimbursement': palette['orange'],
      'Reimbursement only (HSE)': palette['green'],
  }
  ```
- [ ] 2. **Title and axis labels** as variables. Titles are full sentences with the sample size as `$N$={n}`; follow the project's spelling convention.
  ```python
  title = f"Most treatment indications are reimbursed through the HSE scheme ($N$={total})"
  xlabel = "Reimbursement funding scheme"
  ylabel = "Indication count"
  ```
- [ ] 3. **Figure size in mm.** Widths: 90 mm for one column, 140 mm for 1.5, 190 mm for two. Pick the height for the content.
  ```python
  mm_to_inch = 1 / 25.4
  figure_width = 90
  figure_height = 120
  ```
- [ ] 4. **Set up the figure.** For several panels, use a gridspec (`references/layouts.md`).
  ```python
  fig = plt.figure(
      figsize=(figure_width * mm_to_inch, figure_height * mm_to_inch),
      constrained_layout=True,
  )
  ax = fig.add_subplot()
  ```
- [ ] 5. **Plot.** Pass the `colors` dict straight to pandas, and keep the plotted columns in dict order.
  ```python
  data.loc[:, list(colors)].plot(kind='bar', ax=ax, color=colors, stacked=True, width=0.85)
  ```
- [ ] 6. **Annotate.** Label values directly with `ax.text(..., fontsize=5)` and leave headroom with `set_ylim`; draw reference lines dashed, thin, `zorder=0`.
  ```python
  for i, total in enumerate(totals):
      ax.text(i, total + 0.8, f"{total}", ha='center', va='bottom', fontsize=5)
  ```
- [ ] 7. **Labels, spines, tick params.** Hide all spines. Remove tick marks but keep labels, usually. Rotate long x labels.
  ```python
  ax.set_title(title)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_ylim([0, totals.max() * 1.15])
  remove_spines(ax)
  ax.tick_params(axis='x', which='both', length=0)
  ax.tick_params(axis='y', which='both', length=0)
  plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
  ```
- [ ] 8. **Legend.** `ax.legend(frameon=False)`; add `alignment='center'` for a titled legend.
- [ ] 9. **Output folder and files.** Folder named after the figure, next to the notebook. Write `.eps`, `.pdf`, `.png`, `.transparent.png`, `.svg` at 500 dpi with `bbox_inches='tight'`.
  ```python
  output_folder = pathlib.Path("hse-reimbursement-schemes")
  output_filename = "hse-reimbursement-schemes"
  ```
- [ ] 10. **Output for PowerPoint.** Reopen the transparent PNG and save `<name>.ppt.png` with its DPI set to pixel width / width in inches, so PowerPoint places it at its true size.

Steps 9 and 10 are what `save_figure(fig, figure_width, output_folder, output_filename)` does. Use it in functions and when several figures are saved; use the expanded form from `assets/figure_template.py` when the user wants the notebook to show each step. End with `plt.show()` then `plt.close()`.

## As a function

Keep the same ten steps inside the function. Size, title, labels, output folder and file name become parameters, and the docstring follows `python-docstrings`:

```python
plot_histogram(
    data=data,
    figure_width=140,
    figure_height=80,
    title=f"Time from approval to reimbursement ($N$={data.shape[0]})",
    xlabel="Years",
    output_folder="time-to-reimbursement",
    output_filename="time-to-reimbursement",
)
```

Fonts stay in the file's setup block, not in the function. Palette stays a module-level dict, passed in or read from the same dict every time, so a category keeps its color across figures.

## Gotchas

- Pass `figure_width` to `save_figure` in **millimetres**. Passing inches makes the `.ppt.png` the wrong physical size.
- The `colors` dict keys must equal the plotted column names, or pandas silently falls back to the default cycle.
- Reorder columns and rows before plotting (`.loc[:, y_order]`); bar order follows the DataFrame, not the dict.
- `legend(alignment=...)` needs matplotlib 3.6 or later.
- Arial is missing on many Linux machines; matplotlib then silently uses DejaVu Sans. Check with `matplotlib.font_manager.findfont("Arial", fallback_to_default=False)` if text looks different from the expected output.
- Use `pathlib` and `mkdir(parents=True, exist_ok=True)`, not `!mkdir`, so the code runs outside Jupyter.
- Color a category once per project and keep that mapping in every figure. Use `grey` for reference and de-emphasised data.

## Validate

After saving, confirm before reporting the figure done:

1. The folder holds six files: `.eps`, `.pdf`, `.png`, `.transparent.png`, `.svg`, `.ppt.png`.
2. The `.ppt.png` pixel width divided by its DPI equals the target width in inches (`figure_width / 25.4`). `scripts/figure_helpers.py --self-test` checks this on a demo figure.
3. Look at the PNG: no clipped labels, value labels not overlapping, legend not covering data. Fix and re-save if any are wrong.

## Layouts and chart types

Read `references/layouts.md` for multi-panel figures, spacer rows, shared axes, panel letters, histograms, horizontal bars, and reference lines.
