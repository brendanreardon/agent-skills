# Layouts and chart types

Read this when the figure has more than one panel, is a histogram or horizontal bar chart, or needs reference lines or panel letters. The ten-step order in `SKILL.md` still applies; these notes change step 4 (set up) and step 6 (annotate).

## Multiple panels

Use a gridspec in step 4 and one `add_subplot` per panel. Run steps 5–8 once per axis.

```python
fig = plt.figure(figsize=(figure_width * mm_to_inch, figure_height * mm_to_inch), constrained_layout=True)
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1])
ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1], sharey=ax_a)
```

- Use `sharex` / `sharey` when panels compare the same quantity.
- For extra vertical or horizontal space, add a spacer row or column and hide it with `ax.set_visible(False)`.
- For a figure-wide title, add a thin top row, call `ax.axis('off')` on it, and put the title there with `ax.text`.
- Panel letters go top-left in capitals: `ax.text(0, 1, "A", transform=ax.transAxes, va='top', ha='left', fontsize=6)`.
- Save once, with the full figure width in mm.

## Bar charts

- Vertical and stacked: `width=0.85`, headroom with `ax.set_ylim([0, total.max() * 1.15])`, value labels above each bar with `ax.text(i, total + offset, label, ha='center', va='bottom', fontsize=5)`.
- Horizontal: `kind='barh'`, `width=0.85`, `edgecolor='white'`, headroom with `ax.set_xlim`, labels with `ha='left', va='center'`.
- Label values directly on the bars instead of making the reader read an axis.
- Long category labels: `plt.setp(ax.get_xticklabels(), rotation=45, ha='right')`, or switch to horizontal bars.

## Histograms

`rwidth=0.90`. Use `ax.hist(...)` or `data.plot(kind='hist', ax=ax, rwidth=0.90)`. Annotate the median or a threshold with a reference line.

## Reference lines

```python
ax.axvline(median, linestyle='--', linewidth=0.5, color=palette['grey'], zorder=0)
ax.text(median, ax.get_ylim()[1], f" Median: {median:.1f}", ha='left', va='top', fontsize=5)
```

Use `linewidth` 0.5 to 0.75, `zorder=0`, grey, and a short label beside the line. For a horizontal reference use `axhline`.

## Titles

Titles are full descriptive sentences and include the sample size as `$N$={n}`. Follow the project's or venue's spelling convention in figure text (for example, "authorisation" in an Irish project).
