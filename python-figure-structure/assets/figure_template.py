"""Template for a publication figure. Copy into a notebook or module and replace the data.

Each numbered section is one step of the python-figure-structure checklist. Setup comes first.
"""

import pathlib

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import PIL.Image

# --- Setup: fonts and sizes, set once at the top ---------------------------------------------
matplotlib.rcParams["font.family"] = "Arial"
matplotlib.rcParams["font.size"] = 6
matplotlib.rcParams["axes.titlesize"] = 7
matplotlib.rcParams["axes.labelsize"] = 6
matplotlib.rcParams["legend.fontsize"] = 6

# In a notebook, also run: %matplotlib inline

MM_TO_INCH = 1 / 25.4
DPI_OUTPUT = 500

# Paste a palette from the color-palette-tableau or color-palette-dfci skill.
palette = {'blue': '#4e79a7', 'orange': '#f28e2b', 'green': '#59a14f'}


def remove_spines(ax):
    for spine in ["top", "bottom", "right", "left"]:
        ax.spines[spine].set_visible(False)
    return ax


# --- Data (replace) --------------------------------------------------------------------------
data = pd.DataFrame(
    {'With approval': [12, 7, 3], 'Without approval': [5, 4, 6]},
    index=['Group A', 'Group B', 'Group C'],
)
data['total'] = data.sum(axis=1)

# 1. Color palette -----------------------------------------------------------------------------
colors = {
    'With approval': palette['orange'],
    'Without approval': palette['green'],
}

# 2. Title and axis labels ---------------------------------------------------------------------
title = f"Example counts by group ($N$={int(data['total'].sum())})"
xlabel = "Group"
ylabel = "Count"

# 3. Figure size in mm -------------------------------------------------------------------------
figure_width = 90
figure_height = 60

# 4. Set up the figure -------------------------------------------------------------------------
fig = plt.figure(
    figsize=(figure_width * MM_TO_INCH, figure_height * MM_TO_INCH),
    constrained_layout=True,
)
ax = fig.add_subplot()

# 5. Plot --------------------------------------------------------------------------------------
data.loc[:, list(colors)].plot(kind='bar', ax=ax, color=colors, stacked=True, width=0.85)

# 6. Annotate the plot -------------------------------------------------------------------------
for i, total in enumerate(data['total']):
    ax.text(i, total + 0.5, f"{total}", ha='center', va='bottom', fontsize=5)

# 7. Labels, spines, tick params ---------------------------------------------------------------
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_ylim([0, data['total'].max() * 1.15])
remove_spines(ax)
ax.tick_params(axis='x', which='both', length=0)
ax.tick_params(axis='y', which='both', length=0)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# 8. Legend ------------------------------------------------------------------------------------
ax.legend(frameon=False)

# 9. Output folder and files -------------------------------------------------------------------
output_folder = pathlib.Path("example-figure")
output_filename = "example-figure"
output_folder.mkdir(parents=True, exist_ok=True)

for image_format, kwargs in [
    ("eps", dict(dpi=DPI_OUTPUT)),
    ("pdf", dict(transparent=False)),
    ("png", dict(dpi=DPI_OUTPUT, transparent=False)),
    ("png", dict(dpi=DPI_OUTPUT, transparent=True)),
    ("svg", dict(transparent=False)),
]:
    filename = output_filename
    if kwargs.get('transparent', False):
        filename = f"{output_filename}.transparent"
    fig.savefig(
        output_folder / f"{filename}.{image_format}",
        bbox_inches='tight',
        format=image_format,
        **kwargs,
    )

# 10. Output for PowerPoint --------------------------------------------------------------------
# DPI metadata makes PowerPoint place the image at its true width: pixels / dpi == inches.
with PIL.Image.open(output_folder / f"{output_filename}.transparent.png") as img:
    width_px, height_px = img.size
    dpi_for_ppt = width_px / (figure_width * MM_TO_INCH)
    img.save(output_folder / f"{output_filename}.ppt.png", dpi=(dpi_for_ppt, dpi_for_ppt))
print("pixels:", (width_px, height_px), "dpi_for_ppt:", dpi_for_ppt)

plt.show()
plt.close()
