# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.7",
# ]
# ///

import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework0.pdf"), width="100%", height="50vh")
    return


@app.cell
def _(np):
    def unit_gridcircle_mask(N):
        ruler = np.arange(-(N + 1.5), (N + 2.5)) / N
        xx, yy = np.meshgrid(ruler, ruler)
        mask = np.sqrt(np.square(xx) + np.square(yy)) <= 1
        return mask

    return (unit_gridcircle_mask,)


@app.cell
def _(np, unit_gridcircle_mask):
    def unit_gridcircle_area(N):
        area = float(np.sum(unit_gridcircle_mask(N), dtype=float) / N**2)
        return area

    return (unit_gridcircle_area,)


@app.cell
def _(np, plt, unit_gridcircle_mask):
    plt.matshow(unit_gridcircle_mask(5), cmap=plt.cm.gray_r)
    plt.grid(visible=True, color="cyan")
    plt.xticks(ticks=(np.arange(14) - 0.5))
    plt.yticks(ticks=(np.arange(14) - 0.5))
    f = plt.gca()
    f.axes.xaxis.set_ticklabels([])
    f.axes.yaxis.set_ticklabels([])
    plt.show()
    return


@app.cell
def _(np, plt, unit_gridcircle_area):
    Npts = 100
    Ns = np.unique(np.floor(np.logspace(np.log10(2), np.log10(2000), Npts)).astype(int))
    As = list(map(unit_gridcircle_area, Ns))

    plt.figure(figsize=(8,6))
    plt.semilogx(Ns, As, 'o-', color='steelblue', markerfacecolor='lightblue', markersize=12)
    xlim = plt.gca().get_xlim()
    plt.semilogx((xlim[0], xlim[1]), (np.pi, np.pi), ':', linewidth=2.5, color='darkorange')
    plt.xlabel('N', fontsize=14)
    plt.ylabel('Area', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
