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
    return np, rng


@app.cell
def _():
    import matplotlib
    import matplotlib.pyplot as plt
    plt.ion();
    return (plt,)


@app.cell
def _():
    from skimage import io, restoration
    import scipy.ndimage as nd

    return io, nd, restoration


@app.cell
def _():
    import scipy as si
    import scipy.optimize as sio

    return si, sio


@app.cell
def _():
    import timeit

    return


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework7.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Gaussian MLE and number of photons
    """)
    return


@app.cell
def _(np, si):
    def airypsf(xy, l=0.51, NA=0.9, side=0.7, N=210):
        center = xy
        xs, ys = np.meshgrid(np.linspace(- side * (1 - 1/N) / 2, side * (1 - 1/N)/2, N), 
                             np.linspace(- side * (1 - 1/N) / 2, side * (1 - 1/N)/2, N))
        r2s = np.square(xs - center[0]) + np.square(ys - center[1])
        v = 2 * np.pi * NA * np.sqrt(r2s) / l
        psf = 4 * np.square(si.special.j1(v) / v)
        nans = np.isnan(psf)
        psf[nans] = 1
        scale = side / N
        return psf / np.sum(psf), scale

    return (airypsf,)


@app.cell
def _(np):
    def pixelate(image, inscale, shape=(7, 7)):
        outscale = image.shape[0] * inscale / shape[0]
        assert image.shape[0] / image.shape[1] == shape[0] / shape[1], "Aspect Ratio must be preserved!"

        out = np.sum(image.reshape(shape[0], int(image.shape[0] / shape[0]), 
                                   shape[1], int(image.shape[1] / shape[1])), 
                     axis=(1, 3))

        return out, outscale

    return (pixelate,)


@app.cell
def _(np):
    def fishify(image, N=1, rng=np.random.default_rng()):
        return rng.poisson(lam=N * (image / np.sum(image)))

    return (fishify,)


@app.cell
def _(airypsf, fishify, np, pixelate):
    def simage4(xc, yc, N=7, Np = 1000, B=10):
        a, iscale = airypsf(np.array([xc, yc]))
        p, scale = pixelate(a, iscale, shape=(N, N))
        return fishify(p, Np) + fishify(np.ones((N, N)),N=(B * (N ** 2))), scale

    return (simage4,)


@app.cell
def _(np):
    def gausspsf(xc, yc, A0, s, B, N=210, side=0.7):
        xs = np.linspace(- side * (1 - 1/N) / 2, side * (1 - 1/N) / 2, N)
        ys = np.linspace(- side * (1 - 1/N) / 2, side * (1 - 1/N) / 2, N)
        xx, yy = np.meshgrid(xs, ys)
        g =  A0 * np.exp(-(np.square(xx - xc) + np.square(yy - yc)) / (2.0 * np.square(s))) + B
        return g, (side / N)

    return (gausspsf,)


@app.cell
def _(gausspsf, np):
    def objgauss(params, im, side):
        xc, yc, A0, s, B = params
        p, sc = gausspsf(xc, yc, A0, s, B, side=side, N=im.shape[0])
        #A, _ = pixelate(p, sc, shape=im.shape)

        mlogp = np.sum(p - im * np.log(p))
        #mlogp = np.sum(A - im * np.log(A))
        return mlogp

    return (objgauss,)


@app.cell
def _(np, objgauss, sio):
    def MLElocalize_gauss(im, side=0.7, guess=None):
        if guess is None:
            guess = np.array([0, 0, np.max(im), 0.1, np.min(im)])
        bnd = ((-side / 2, side / 2), (-side / 2, side / 2), (0, np.max(im)), (1e-2, None), (0, None))
        res = sio.minimize(objgauss, guess, args = (im, side), bounds= bnd)
        return res

    return (MLElocalize_gauss,)


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### a.
    See solution from last week! Looks unbiased:
    """)
    return


@app.cell
def _(MLElocalize_gauss, np, plt, rng, simage4):
    figr, axr = plt.subplots()
    xs = rng.uniform(-0.5 * 0.1, 0.5 * 0.1, 100)
    ys = rng.uniform(-0.5 * 0.1, 0.5 * 0.1, 100)
    ims = [simage4(xs[i], ys[i])[0] for i in range(100)]
    es = np.array([MLElocalize_gauss(image).x[0] for image in ims])
    axr.scatter(xs, es - xs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### b.
    """)
    return


@app.cell
def _(np):
    def RMSE(xs, ts=None):
        if ts is None:
            ts = np.zeros_like(xs)
        return np.sqrt(np.mean(np.square(xs - ts), axis=1))

    return (RMSE,)


@app.cell
def _(MLElocalize_gauss, np, simage4):
    Nps = np.logspace(1, 5, 30)
    imss = [simage4(0, 0, Np=i)[0] for i in Nps]
    ess = np.array([MLElocalize_gauss(image).x for image in imss])[:,0:2]
    return Nps, ess


@app.cell
def _(Nps, RMSE, ess, np, plt):
    fig2, ax2 = plt.subplots()
    ax2.loglog(Nps, RMSE(ess))
    ax2.loglog(Nps, 0.51 / 2 / 0.9 / np.sqrt(Nps)) # theoretical baseline
    return


@app.cell
def _(mo):
    mo.md(r"""
    TODO: Need to RMSE over multiple samples for each Np, not just one like this, but trend is already looking on-point.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Radial-symmetry-based particle localization
    TODO: Mostly running Prof. code.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Assessing Deconvolution
    """)
    return


@app.cell
def _(np):
    def gausspsff(xc, yc, A0, s, B, N=210, side=0.7):
        xs = np.linspace(- side * (1 - 1/N) / 2, side * (1 - 1/N) / 2, N)
        ys = np.linspace(- side * (1 - 1/N) / 2, side * (1 - 1/N) / 2, N)
        xx, yy = np.meshgrid(xs, ys)
        g =  A0 * np.exp(-(np.square(xx - xc) + np.square(yy - yc)) / (2.0 * np.square(s))) + B
        return g / np.sum(g), (side / N)

    return (gausspsff,)


@app.cell
def _(np):
    def fishifyf(image, N=1, rng=np.random.default_rng()):
        return rng.poisson(lam=N * (image / np.sum(image)))

    return


@app.cell
def _(gausspsff, plt):
    fig, ax = plt.subplots()
    gpsf = gausspsff(0, 0, 1, 7, 0, 35, 35)[0]
    gpsf2 = gausspsff(0, 0, 1, 5, 0, 35, 35)[0]
    ax.imshow(gpsf)
    return (gpsf,)


@app.cell
def _(io):
    mouse_glial_cells_crop_png = io.imread("mouse_glial_cells_RBurdan_crop.png", as_gray=True)
    return (mouse_glial_cells_crop_png,)


@app.cell
def _(mouse_glial_cells_crop_png, plt):
    fig3, ax3 = plt.subplots()
    ax3.imshow(mouse_glial_cells_crop_png, cmap="gray")
    return


@app.cell
def _(gpsf, mouse_glial_cells_crop_png, nd):
    mouse_glial_cells_crop_conv = nd.convolve(mouse_glial_cells_crop_png, gpsf, mode="constant")
    return (mouse_glial_cells_crop_conv,)


@app.cell
def _(mouse_glial_cells_crop_conv, plt):
    fig4, ax4 = plt.subplots()
    ax4.imshow(mouse_glial_cells_crop_conv, cmap="gray")
    return


@app.cell
def _(mouse_glial_cells_crop_conv, rng):
    mouse_glial_cells_crop_fish = rng.poisson(mouse_glial_cells_crop_conv)
    return (mouse_glial_cells_crop_fish,)


@app.cell
def _(mouse_glial_cells_crop_fish, plt):
    fig5, ax5 = plt.subplots()
    ax5.imshow(mouse_glial_cells_crop_fish, cmap="gray")
    return


@app.cell
def _(gpsf, mouse_glial_cells_crop_fish, restoration):
    mouse_glial_cells_crop_restored = restoration.richardson_lucy(mouse_glial_cells_crop_fish, gpsf, num_iter=20, clip=False)
    return (mouse_glial_cells_crop_restored,)


@app.cell
def _(mouse_glial_cells_crop_restored, plt):
    fig6, ax6 = plt.subplots()
    ax6.imshow(mouse_glial_cells_crop_restored, cmap="gray")
    return


@app.cell
def _(
    gpsf,
    mouse_glial_cells_crop_fish,
    mouse_glial_cells_crop_png,
    np,
    restoration,
):
    rmss = []
    imsi = []
    for i in range(1, 250, 10):
        mouse_glial_cells_crop_restorei = restoration.richardson_lucy(mouse_glial_cells_crop_fish, gpsf, num_iter=i, clip=False)
        mouse_glial_cells_crop_restorei = mouse_glial_cells_crop_restorei[35:-35, 35:-35]
        mouse_glial_cells_crop_restorei -= np.min(mouse_glial_cells_crop_restorei)
        mouse_glial_cells_crop_restorei *= (np.max(mouse_glial_cells_crop_png[35:-35, 35:-35]) - np.min(mouse_glial_cells_crop_png[35:-35, 35:-35])) / np.max(mouse_glial_cells_crop_restorei)
        mouse_glial_cells_crop_restorei += np.min(mouse_glial_cells_crop_png[35:-35, 35:-35])
        imsi.append(mouse_glial_cells_crop_restorei)
        rms = np.sqrt(np.mean(np.square(mouse_glial_cells_crop_restorei - mouse_glial_cells_crop_png[35:-35, 35:-35])))
        rmss.append(rms)
    return imsi, rmss


@app.cell
def _(plt, rmss):
    fig7, ax7 = plt.subplots()
    ax7.scatter(range(1, 250, 10), rmss)
    return


@app.cell
def _(imsi, np, plt, rmss):
    fig8, ax8 = plt.subplots()
    ax8.imshow(imsi[np.argmin(rmss)], cmap="gray")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
