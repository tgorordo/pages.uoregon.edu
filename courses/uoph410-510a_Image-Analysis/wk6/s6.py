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
    from skimage import io
    import scipy.ndimage as nd

    return (io,)


@app.cell
def _():
    import scipy as si
    import scipy.optimize as sio

    return si, sio


@app.cell
def _():
    import timeit

    return (timeit,)


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework6.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cilia and temporal filtering
    """)
    return


@app.cell
def _(io):
    cilia_movie_crop = io.imread("cilia_movie_crop.tif", plugin="tifffile")
    cilia_movie_crop_nframes = cilia_movie_crop.shape[0]
    return cilia_movie_crop, cilia_movie_crop_nframes


@app.cell
def _(cilia_movie_crop_nframes, mo):
    i = mo.ui.slider(0, cilia_movie_crop_nframes - 1, 1)
    i
    return (i,)


@app.cell
def _(cilia_movie_crop, i, plt):
    figi, axi = plt.subplots()
    axi.imshow(cilia_movie_crop[0,:,:], cmap="gray")
    axi.imshow(cilia_movie_crop[i.value,:,:], cmap="gray")
    return


@app.cell
def _(cilia_movie_crop, np):
    cilia_movie_crop_med = np.median(cilia_movie_crop, axis=0)
    return (cilia_movie_crop_med,)


@app.cell
def _(cilia_movie_crop, cilia_movie_crop_med, cilia_movie_crop_nframes, np):
    cilia_movie_crop_mmed = cilia_movie_crop - np.tile(cilia_movie_crop_med, (cilia_movie_crop_nframes, 1, 1))
    return (cilia_movie_crop_mmed,)


@app.cell
def _(cilia_movie_crop_nframes, mo):
    ii = mo.ui.slider(0, cilia_movie_crop_nframes - 1, 1)
    ii
    return (ii,)


@app.cell
def _(cilia_movie_crop, cilia_movie_crop_mmed, ii, plt):
    figii, axii = plt.subplots()
    axii.imshow(cilia_movie_crop[0,:,:], cmap="gray")
    axii.imshow(cilia_movie_crop_mmed[ii.value,:,:], cmap="gray")
    return


@app.cell
def _(cilia_movie_crop_mmed, plt):
    fig1, (ax1a, ax1b) = plt.subplots(2, 1)
    ax1a.imshow(cilia_movie_crop_mmed[0,:,:], cmap="gray")
    ax1b.hist(cilia_movie_crop_mmed.flatten(), bins=100) #, log=True)
    fig1
    return


@app.cell
def _(cilia_movie_crop_mmed):
    cilia_imin = -15
    cilia_imax = 15
    cilia_movie_crop_mmed_scaled = 255 * (cilia_movie_crop_mmed - cilia_imin) / (cilia_imax - cilia_imin)
    return (cilia_movie_crop_mmed_scaled,)


@app.cell
def _(cilia_movie_crop_nframes, mo):
    iii = mo.ui.slider(0, cilia_movie_crop_nframes - 1, 1)
    iii
    return (iii,)


@app.cell
def _(cilia_movie_crop_mmed_scaled, iii, plt):
    fig4, ax4 = plt.subplots()
    ax4.imshow(cilia_movie_crop_mmed_scaled[0,:,:], cmap="gray")
    ax4.imshow(cilia_movie_crop_mmed_scaled[iii.value,:,:], cmap="gray")
    return


@app.cell
def _(cilia_movie_crop_mmed_scaled, np):
    cilia_movie_crop_mmed_scaled_std = np.std(cilia_movie_crop_mmed_scaled, 0)
    return (cilia_movie_crop_mmed_scaled_std,)


@app.cell
def _(cilia_movie_crop_mmed_scaled_std, plt):
    fig5, ax5 = plt.subplots()
    ax5.imshow(cilia_movie_crop_mmed_scaled_std, cmap="gray")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## MLE Practice
    """)
    return


@app.cell
def _(np):
    def A(x0, b, x = np.linspace(-3, 4, 100)):
        return 3 * np.power(np.abs(x - x0), b) + 4

    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Images for \#3-\#4
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Centroid Localization Timing
    """)
    return


@app.cell
def _(np):
    def centroid(im, scale=None):
        ys, xs = np.indices(im.shape)
        c = np.hstack([np.sum(xs * im), np.sum(ys * im)]) / np.sum(im)
        c = (im * np.mgrid[0:im.shape[0], 0:im.shape[1]]).sum(1).sum(1)/im.sum()
        return c if scale is None else scale * (c - np.array(im.shape) // 2)

    return (centroid,)


@app.cell
def _(centroid, rng, simage4, timeit):
    xys = list(zip(rng.uniform(-0.35, 0.35, 100), rng.uniform(-0.35, 0.35, 100)))
    ims = [simage4(x, y)[0] for x, y in xys]
    startt = timeit.default_timer()
    cs = [centroid(i) for i in ims]
    print(timeit.default_timer() - startt, "seconds")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Gaussian MLE for particle localization!
    """)
    return


@app.cell
def _(plt, simage4):
    fig2, ax2 = plt.subplots()
    im, sc = simage4(-0.08, 0.03)
    ax2.imshow(im)
    return (im,)


@app.cell
def _(airypsf, np, pixelate):
    def objcam(params, im, l, NA, side):
        x, y = params
        p, s = airypsf(np.array([x, y]), l=l, NA=NA, side=side)
        A, _ = pixelate(p, s, shape=im.shape)

        mlogp = np.sum(A - im * np.log(A))
        return mlogp

    return (objcam,)


@app.cell
def _(np, objcam, sio):
    def MLElocalize_knowcam(im, l=0.51, NA=0.9, side=0.7, guess=np.array([-0.05, 0.1])):
        bnd = ((-side / 2, side / 2), (-side / 2, side / 2))
        res = sio.minimize(objcam, guess, args=(im, l, NA, side), bounds= bnd)
        return res

    return (MLElocalize_knowcam,)


@app.cell
def _(MLElocalize_knowcam, im):
    MLElocalize_knowcam(im)
    return


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
def _(gausspsf, pixelate, plt):
    fig3, ax3 = plt.subplots()
    im3, sc3 = gausspsf(0, 0, 0.02, 0.1, 1) # initial guess
    im3p, _ = pixelate(im3, sc3, shape=(7, 7))
    ax3.imshow(im3p)
    return


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
def _(MLElocalize_gauss, im):
    res = MLElocalize_gauss(im)
    res
    return (res,)


@app.cell
def _(gausspsf, plt, res):
    fig8, ax8 = plt.subplots()
    im8, _ = gausspsf(*res.x, side=0.7, N=7)
    ax8.imshow(im8)
    return


@app.cell
def _(MLElocalize_gauss, simage4):
    resx = []
    for _ in range(100):
        im9, sc9 = simage4(0.03, 0.03)
        res9 = MLElocalize_gauss(im9)
        resx.append(res9.x[0] - 0.03)
    return (resx,)


@app.cell
def _(plt, resx):
    figh, axh = plt.subplots()
    axh.hist(resx, bins="auto")
    figh
    return


@app.cell
def _(MLElocalize_gauss, np, plt, simage4):
    figs, axs = plt.subplots()
    xs = np.linspace(-0.05, 0.05, 10)
    ys = np.zeros(10)
    imss = [simage4(xs[i], ys[i])[0] for i in range(10)]
    es = [MLElocalize_gauss(image).x[0] for image in imss]
    axs.scatter(xs, es - xs)
    #axs.set_ylim([-0.5, 0.5])
    return


@app.cell
def _(MLElocalize_gauss, np, plt, rng, simage4):
    figr, axr = plt.subplots()
    xss = rng.uniform(-0.5 * 0.1, 0.5 * 0.1, 100)
    yss = rng.uniform(-0.5 * 0.1, 0.5 * 0.1, 100)
    imsss = [simage4(xss[i], yss[i])[0] for i in range(100)]
    ess = np.array([MLElocalize_gauss(image).x[0] for image in imsss])
    axr.scatter(xss, ess - xss)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
