# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib>=3.6",
#   "pillow",
# ]
# ///
"""Helpers for the python-figure-structure skill.

Copy remove_spines and save_figure into a notebook or module, or import this file.
Run `uv run scripts/figure_helpers.py --self-test` to write a demo figure to a temporary folder and check the outputs.
"""

import argparse
import pathlib
import sys
import tempfile

import matplotlib
import matplotlib.pyplot as plt
import PIL.Image

DPI_OUTPUT = 500
MM_TO_INCH = 1 / 25.4


def remove_spines(ax):
    """
    Hides all four spines of an axis.

    Args:
        ax (matplotlib.axes.Axes): The axis to style.

    Returns:
        matplotlib.axes.Axes: The same axis.
    """
    for spine in ["top", "bottom", "right", "left"]:
        ax.spines[spine].set_visible(False)
    return ax


def save_figure(fig, figure_width_mm, output_folder, output_filename, dpi_output=DPI_OUTPUT):
    """
    Writes a figure as eps, pdf, png, transparent png, svg, and a PowerPoint-sized png.

    Args:
        fig (matplotlib.figure.Figure): The figure to save.
        figure_width_mm (float): Intended physical width in millimetres, used for the .ppt.png DPI.
        output_folder (str | pathlib.Path): Folder to write into; created if missing.
        output_filename (str): File name without extension.
        dpi_output (int): Resolution for raster and eps output (default: 500).

    Returns:
        list[pathlib.Path]: The files written.
    """
    output_folder = pathlib.Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    written = []
    for image_format, kwargs in [
        ("eps", dict(dpi=dpi_output)),
        ("pdf", dict(transparent=False)),
        ("png", dict(dpi=dpi_output, transparent=False)),
        ("png", dict(dpi=dpi_output, transparent=True)),
        ("svg", dict(transparent=False)),
    ]:
        filename = output_filename
        if kwargs.get("transparent", False):
            filename = f"{output_filename}.transparent"
        path = output_folder / f"{filename}.{image_format}"
        fig.savefig(path, bbox_inches="tight", format=image_format, **kwargs)
        written.append(path)

    # PowerPoint sizes an image from its DPI metadata: pixels / dpi must equal the width in inches.
    transparent_path = output_folder / f"{output_filename}.transparent.png"
    with PIL.Image.open(transparent_path) as img:
        width_px, _ = img.size
        dpi_for_ppt = width_px / (figure_width_mm * MM_TO_INCH)
        ppt_path = output_folder / f"{output_filename}.ppt.png"
        img.save(ppt_path, dpi=(dpi_for_ppt, dpi_for_ppt))
    written.append(ppt_path)
    return written


def _self_test(output_folder):
    """
    Writes a demo figure and verifies all six files and the PowerPoint DPI.

    Args:
        output_folder (str | pathlib.Path): Folder to write the demo figure into.

    Raises:
        AssertionError: If a file is missing or the PowerPoint DPI is wrong.
    """
    figure_width = 90
    fig = plt.figure(
        figsize=(figure_width * MM_TO_INCH, 60 * MM_TO_INCH),
        constrained_layout=True,
    )
    ax = fig.add_subplot()
    ax.bar(["A", "B", "C"], [12, 7, 3], color="#4e79a7", width=0.85)
    remove_spines(ax)
    ax.tick_params(axis="both", which="both", length=0)

    written = save_figure(fig, figure_width, output_folder, "self-test")
    plt.close(fig)

    assert len(written) == 6 and all(path.exists() for path in written), written
    with PIL.Image.open(written[-1]) as img:
        width_px, _ = img.size
        dpi_x, _ = img.info["dpi"]
    assert abs(width_px / dpi_x * 25.4 - figure_width) < 0.5, (width_px, dpi_x)
    print(f"ok: wrote {len(written)} files to {output_folder}; ppt.png dpi={dpi_x:.1f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="Write a demo figure and verify it.")
    parser.add_argument(
        "--output-folder",
        default=None,
        help="Folder for the demo figure (default: a new temporary folder).",
    )
    args = parser.parse_args()
    if not args.self_test:
        parser.print_help()
        sys.exit(0)
    matplotlib.use("Agg")
    _self_test(args.output_folder or tempfile.mkdtemp(prefix="figure-self-test-"))
