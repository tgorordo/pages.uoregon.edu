import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import matplotlib, matplotlib.pyplot as plt
    plt.ion()
    return (plt,)


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _():
    from skimage import io
    from skimage.filters import threshold_otsu, threshold_local

    return io, threshold_local, threshold_otsu


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework2.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Thresholding
    """)
    return


@app.cell
def _(io):
    robert_mapplethrope_calla_lily_1984_png = io.imread("robert-mapplethrope-calla-lily-1984.png", as_gray=True)
    return (robert_mapplethrope_calla_lily_1984_png,)


@app.cell
def _(plt, robert_mapplethrope_calla_lily_1984_png):
    fig1, ax1 = plt.subplots()
    p1 = ax1.imshow(robert_mapplethrope_calla_lily_1984_png, cmap="gray")
    fig1.colorbar(p1, ax=ax1)
    fig1
    return


@app.cell
def _(robert_mapplethrope_calla_lily_1984_png, threshold_otsu):
    robert_mapplethrope_calla_lily_global_threshold = threshold_otsu(robert_mapplethrope_calla_lily_1984_png)
    robert_mapplethrope_calla_lily_global_threshold # print
    return (robert_mapplethrope_calla_lily_global_threshold,)


@app.cell
def _(
    plt,
    robert_mapplethrope_calla_lily_1984_png,
    robert_mapplethrope_calla_lily_global_threshold,
):
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(8, 4))
    ax2a.hist(robert_mapplethrope_calla_lily_1984_png.flatten(), log=True, bins="auto")
    ax2a.vlines(robert_mapplethrope_calla_lily_global_threshold, 0, 80_000, color="r")
    p2b = ax2b.imshow(robert_mapplethrope_calla_lily_1984_png > robert_mapplethrope_calla_lily_global_threshold, cmap="gray")
    fig2.colorbar(p2b, ax=ax2b)
    fig2
    return


@app.cell
def _(io, plt):
    fig3, ax3 = plt.subplots()
    istanbul_arch_museum_gray_crop_png = io.imread("istanbul_arch_museum_gray_crop.png", as_gray=True)
    p3 = ax3.imshow(istanbul_arch_museum_gray_crop_png, cmap="gray")
    fig3.colorbar(p3, ax=ax3)
    fig3
    return (istanbul_arch_museum_gray_crop_png,)


@app.cell
def _(istanbul_arch_museum_gray_crop_png, threshold_otsu):
    istanbul_global_threshold = threshold_otsu(istanbul_arch_museum_gray_crop_png)
    istanbul_global_threshold # print
    return (istanbul_global_threshold,)


@app.cell
def _(istanbul_arch_museum_gray_crop_png, istanbul_global_threshold, plt):
    fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(8, 4))
    ax4a.hist(istanbul_arch_museum_gray_crop_png.flatten(), log=True, bins="auto")
    ax4a.vlines(istanbul_global_threshold, 0, 300_000, color='r')
    p4b = ax4b.imshow(istanbul_arch_museum_gray_crop_png > istanbul_global_threshold, cmap="gray")
    fig4.colorbar(p4b, ax=ax4b)
    fig4
    return


@app.cell
def _(io):
    robert_mapplethrope_calla_lily_1984_crop_png = io.imread("robert-mapplethrope-calla-lily-1984_CROP.png", as_gray=True)
    return (robert_mapplethrope_calla_lily_1984_crop_png,)


@app.cell
def _(plt, robert_mapplethrope_calla_lily_1984_crop_png):
    fig5, ax5 = plt.subplots()
    p5 = ax5.imshow(robert_mapplethrope_calla_lily_1984_crop_png, cmap="gray")
    fig5.colorbar(p5, ax=ax5)
    fig5
    return


@app.cell
def _(robert_mapplethrope_calla_lily_1984_crop_png, threshold_otsu):
    robert_mapplethrope_calla_lily_crop_global_threshold = threshold_otsu(robert_mapplethrope_calla_lily_1984_crop_png)
    robert_mapplethrope_calla_lily_crop_global_threshold # print
    return (robert_mapplethrope_calla_lily_crop_global_threshold,)


@app.cell
def _(
    plt,
    robert_mapplethrope_calla_lily_1984_crop_png,
    robert_mapplethrope_calla_lily_crop_global_threshold,
):
    fig6, (ax6a, ax6b) = plt.subplots(1, 2, figsize=(8, 4))
    ax6a.hist(robert_mapplethrope_calla_lily_1984_crop_png.flatten(), log=True, bins="auto")
    ax6a.vlines(robert_mapplethrope_calla_lily_crop_global_threshold, 0, 80_000, color="r")
    p6b = ax6b.imshow(robert_mapplethrope_calla_lily_1984_crop_png > robert_mapplethrope_calla_lily_crop_global_threshold, cmap="gray")
    fig6.colorbar(p6b, ax=ax6b)
    fig6
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Thresholding, again
    """)
    return


@app.cell
def _(
    istanbul_arch_museum_gray_crop_png,
    plt,
    robert_mapplethrope_calla_lily_1984_crop_png,
    robert_mapplethrope_calla_lily_1984_png,
    threshold_local,
):
    fig7, (ax7a, ax7b, ax7c) = plt.subplots(1, 3, figsize=(12, 4))
    p7a = ax7a.imshow(robert_mapplethrope_calla_lily_1984_png > threshold_local(robert_mapplethrope_calla_lily_1984_png, block_size=123), cmap="gray")
    fig7.colorbar(p7a, ax=ax7a)
    p7b = ax7b.imshow(istanbul_arch_museum_gray_crop_png > threshold_local(istanbul_arch_museum_gray_crop_png, block_size=123), cmap="gray")
    fig7.colorbar(p7b, ax=ax7b)
    p7c = ax7c.imshow(robert_mapplethrope_calla_lily_1984_crop_png > threshold_local(robert_mapplethrope_calla_lily_1984_crop_png, block_size=123), cmap="gray")
    fig7.colorbar(p7c, ax=ax7c)
    fig7
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Protein density
    """)
    return


@app.cell
def _(io, plt):
    fig8, ax8 = plt.subplots()
    microarray_crop_png = io.imread("microarray_crop.png", as_gray=True)
    p8 = ax8.imshow(microarray_crop_png, cmap="gray")
    fig8.colorbar(p8, ax=ax8)
    fig8
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Non-uniform background subtraction
    """)
    return


@app.cell
def _(io, plt):
    fig9, ax9 = plt.subplots()
    GUV24_bead_crop_png = io.imread("GUV24_bead_Crop.png", as_gray=True)
    p9 = ax9.imshow(GUV24_bead_crop_png, cmap="gray")
    fig9.colorbar(p9, ax=ax9)
    fig9
    return (GUV24_bead_crop_png,)


@app.cell
def _(GUV24_bead_crop_png, np):
    x = np.arange(GUV24_bead_crop_png.shape[0])
    y = np.arange(GUV24_bead_crop_png.shape[1])
    xs, ys = np.meshgrid(x, y)
    return x, xs, ys


@app.cell
def _(GUV24_bead_crop_png, plt, xs, ys):
    fig10, ax10 = plt.subplots()
    ax10 = plt.axes(projection ='3d')
    p10 = ax10.plot_surface(xs, ys, GUV24_bead_crop_png, cmap="viridis")
    fig10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### b.
    """)
    return


@app.cell
def _(GUV24_bead_crop_png, np, xs):
    w = np.vstack([xs.ravel(), np.ones(xs.size)]).T
    mx, c = np.linalg.lstsq(w, GUV24_bead_crop_png.ravel())[0] # (c-410) 3pt alternative
    (mx, c)
    return c, mx


@app.cell
def _(GUV24_bead_crop_png, c, mx, plt, x, xs, ys):
    fig11, (ax11a, ax11b) = plt.subplots(1, 2, figsize=(8, 4))
    ax11a.plot(x, mx * x + c, c='r')
    ax11a.scatter(xs.ravel(), GUV24_bead_crop_png.ravel(), s=4)
    ax11b.scatter(ys.ravel(), GUV24_bead_crop_png.ravel(), s=4)
    fig11
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### c.
    #### 410:
    """)
    return


@app.cell
def _(GUV24_bead_crop_png, np, xs, ys):
    # z = m @ w + c
    w2 = np.vstack([xs.ravel(), ys.ravel(), np.ones(GUV24_bead_crop_png.size)]).T
    mx2, my2, c2 = np.linalg.lstsq(w2, GUV24_bead_crop_png.ravel())[0]
    (mx2, my2, c2)
    return c2, mx2, my2


@app.cell
def _(GUV24_bead_crop_png, c2, mx2, my2, plt, xs, ys):
    fig12, ax12 = plt.subplots()
    ax12 = plt.axes(projection ='3d')
    ax12.plot_surface(xs, ys, GUV24_bead_crop_png, cmap="viridis", alpha=0.3)
    ax12.plot_surface(xs, ys, mx2 * xs + my2 * ys + c2, cmap="plasma")
    fig12
    return


@app.cell
def _(GUV24_bead_crop_png, c2, mx2, my2, plt, xs, ys):
    fig13, ax13 = plt.subplots()
    ax13 = plt.axes(projection ='3d')
    ax13.plot_surface(xs, ys, GUV24_bead_crop_png - (mx2 * xs + my2 * ys + c2), cmap="viridis")
    fig13
    return


@app.cell
def _(GUV24_bead_crop_png, c2, mx2, my2, plt, xs, ys):
    fig14, ax14 = plt.subplots()
    p14 = ax14.imshow(GUV24_bead_crop_png - (mx2 * xs + my2 * ys + c2), cmap="gray")
    fig14.colorbar(p14, ax=ax14)
    fig14
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 510:
    """)
    return


@app.cell
def _(GUV24_bead_crop_png, np, xs, ys):
    # z = m @ w + c
    w3 = np.vstack([xs.ravel(), np.square(xs.ravel()), 
                   ys.ravel(), np.square(ys.ravel()), 
                   np.ones(GUV24_bead_crop_png.size)]).T
    mx3, mx3x, my3, my3y, c3 = np.linalg.lstsq(w3, GUV24_bead_crop_png.ravel())[0]
    (mx3, mx3x, my3, my3y, c3)
    return c3, mx3, mx3x, my3, my3y


@app.cell
def _(GUV24_bead_crop_png, c3, mx3, mx3x, my3, my3y, np, plt, xs, ys):
    fig15, ax15 = plt.subplots()
    ax15 = plt.axes(projection ='3d')
    ax15.plot_surface(xs, ys, GUV24_bead_crop_png, cmap="viridis", alpha=0.3)
    ax15.plot_surface(xs, ys, mx3 * xs + mx3x * np.square(xs) + my3 * ys + my3y * np.square(ys) + c3, cmap="plasma")
    return


@app.cell
def _(GUV24_bead_crop_png, c3, mx3, mx3x, my3, my3y, np, plt, xs, ys):
    fig16, ax16 = plt.subplots()
    p16 = ax16.imshow(GUV24_bead_crop_png - (mx3 * xs + mx3x * np.square(xs) + my3 * ys + my3y * np.square(ys) + c3), cmap="gray")
    fig16.colorbar(p16, ax=ax16)
    fig16
    return


@app.cell
def _(GUV24_bead_crop_png, c3, mx3, mx3x, my3, my3y, np, plt, xs, ys):
    fig17, ax17 = plt.subplots()
    ax17 = plt.axes(projection ='3d')
    ax17.plot_surface(xs, ys, GUV24_bead_crop_png - 
                    (mx3 * xs + mx3x * np.square(xs) + my3 * ys + my3y * np.square(ys) + c3), cmap="viridis")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
