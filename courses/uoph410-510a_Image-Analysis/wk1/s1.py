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
    mo.pdf(src=Path("Homework1.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Puzzles
    ### a.
    """)
    return


@app.cell
def _(plt):
    im_A_png = plt.imread("AuLait_gray.png")
    im_A_tif = plt.imread("AuLait_gray.tif")
    return im_A_png, im_A_tif


@app.cell
def _(im_A_png, plt):
    plt.imshow(im_A_png, "gray")
    return


@app.cell
def _(im_A_tif):
    im_A_tif.shape
    return


@app.cell
def _(im_A_png, np):
    np.max(im_A_png)
    return


@app.cell
def _(im_A_tif, plt):
    plt.imshow(im_A_tif, "gray")
    return


@app.cell
def _(im_A_tif):
    im_A_tif.shape
    return


@app.cell
def _(im_A_tif, np):
    np.max(im_A_tif)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## b.
    """)
    return


@app.cell
def _():
    from skimage import io

    return (io,)


@app.cell
def _(im_A_png, io):
    io.imsave("AuLait_gray_png_skout_unscaled.tif", im_A_png)
    return


@app.cell
def _(plt):
    im_A_sk_tif_unscaled = plt.imread("AuLait_gray_png_skout_unscaled.tif")
    return (im_A_sk_tif_unscaled,)


@app.cell
def _(im_A_sk_tif_unscaled):
    im_A_sk_tif_unscaled.shape
    return


@app.cell
def _(im_A_sk_tif_unscaled, plt):
    plt.imshow(im_A_sk_tif_unscaled)
    return


@app.cell
def _(im_A_png, io):
    io.imsave("AuLait_gray_png_skout_scaledup.tif", im_A_png * 255)
    return


@app.cell
def _(plt):
    im_A_sk_tif_scaled = plt.imread("AuLait_gray_png_skout_scaledup.tif")
    return (im_A_sk_tif_scaled,)


@app.cell
def _(im_A_sk_tif_scaled):
    im_A_sk_tif_scaled.shape
    return


@app.cell
def _(im_A_sk_tif_scaled, plt):
    plt.imshow(im_A_sk_tif_scaled)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
