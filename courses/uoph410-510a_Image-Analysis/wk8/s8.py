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
    rng = np.random.default_rng()
    return


@app.cell
def _():
    import scipy as si

    return


@app.cell
def _():
    from skimage import io, morphology as mf

    return io, mf


@app.cell
def _():
    import matplotlib
    import matplotlib.pyplot as plt
    plt.ion();
    return (plt,)


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework8.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Spot Removal
    """)
    return


@app.cell
def _(io, plt):
    lichtenstein_imageduplicator_1963_png = io.imread("Lichtenstein_imageDuplicator_1963.png")
    lichtenstein_imageduplicator_1963_gray = io.imread("Lichtenstein_imageDuplicator_1963_gray.png")
    fig0, (ax0a, ax0b) = plt.subplots(1, 2)
    ax0a.imshow(lichtenstein_imageduplicator_1963_png)
    ax0b.imshow(lichtenstein_imageduplicator_1963_gray, cmap="gray")
    return (lichtenstein_imageduplicator_1963_gray,)


@app.cell
def _(lichtenstein_imageduplicator_1963_gray, mf):
    lichtenstein_imageduplicator_1963_close = mf.closing(lichtenstein_imageduplicator_1963_gray, mf.disk(4))
    lichtenstein_imageduplicator_1963_close = mf.closing(lichtenstein_imageduplicator_1963_gray, mf.disk(2))
    return (lichtenstein_imageduplicator_1963_close,)


@app.cell
def _(lichtenstein_imageduplicator_1963_close, plt):
    fig1, ax1 = plt.subplots()
    ax1.imshow(lichtenstein_imageduplicator_1963_close, cmap="gray")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
