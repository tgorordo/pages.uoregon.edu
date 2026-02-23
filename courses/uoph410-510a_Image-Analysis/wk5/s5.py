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
    import scipy as si

    return (si,)


@app.cell
def _():
    import matplotlib
    import matplotlib.pyplot as plt
    plt.ion();
    return (plt,)


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework5.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Signal-to-Noise Ratio in Images
    """)
    return


@app.cell
def _(rng):
    xs = rng.poisson(lam=200, size=1000 * 500).reshape(1000, 500)
    xs.shape
    return (xs,)


@app.cell
def _(np, xs):
    np.mean(np.mean(xs, axis=0) / np.std(xs, axis=0))
    return


@app.cell
def _(np):
    As = np.logspace(-6, 6, 500)
    As.shape
    return (As,)


@app.cell
def _(As, np, xs):
    np.mean(np.mean(As * xs, axis=0) / np.std(As * xs, axis=0))
    return


@app.cell
def _(As, np, xs):
    ras = np.mean(xs, axis=0) / np.std(xs, axis=0) - np.mean(As * xs, axis=0) / np.std(As * xs, axis=0)
    np.mean(ras)
    return (ras,)


@app.cell
def _(plt, ras):
    fig, ax = plt.subplots()
    ax.hist(ras, bins="auto")
    fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Zero! To within typical machine error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Centroid Warmup
    """)
    return


@app.cell
def _(np):
    i = np.arange(0, 1000)
    I = 0.2 * np.sqrt(i)
    float(np.sum(i * I) / np.sum(I))
    return (i,)


@app.cell
def _(i, np, rng):
    J = 30 / (i + 20) + 0.05 * rng.poisson(lam=10, size=i.size)
    float(np.sum(i * J) / np.sum(J))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Centroid Localization
    """)
    return


@app.cell
def _(np, si):
    def psfker(l, NA=0.9, side=1.0, N=210, center=(0.0, 0.0)):
        xs, ys = np.meshgrid(np.linspace(- side / 2, side / 2, N), 
                             np.linspace(- side / 2, side / 2, N))
        r2s = np.square(xs - center[0]) + np.square(ys - center[1])
        v = 2 * np.pi * NA * np.sqrt(r2s) / l
        psf = 4 * np.square(si.special.j1(v) / v)
        psf[np.isnan(psf)] = 1
        scale = side / N
        return psf / np.sum(psf), scale

    return (psfker,)


@app.cell
def _(np):
    def pixelate(image, inscale, shape=(7, 7)):
        outscale = image.shape[0] * inscale / shape[0]

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
def _(fishify, np, pixelate, psfker):
    def sim(l=0.51, NA=0.9, side=0.7, center=(0.0, 0.0), Nphoton=500, Nfine=280, bgavg=10, shape=(7, 7)):
        point, scale = psfker(l, NA=NA, side=side, N=Nfine, center=center)
        pxpt, scale = pixelate(point, scale, shape=shape)
        fg = fishify(pxpt, N=Nphoton)
        bg = fishify(np.ones(shape), N=bgavg * np.prod(shape))
        return fg + bg, scale

    return (sim,)


@app.cell
def _(np):
    def centroid(im, scale=None):
        ys, xs = np.indices(im.shape)
        c = np.hstack([np.sum(xs * im), np.sum(ys * im)]) / np.sum(im)
        c = (im * np.mgrid[0:im.shape[0], 0:im.shape[1]]).sum(1).sum(1)/im.sum()
        return c if scale is None else scale * (c - np.array(im.shape) // 2)

    return (centroid,)


@app.cell
def _(np):
    def rms(cs, center=(0.0, 0.0)):
        return float(np.sqrt(np.mean(np.square(cs[:,0] - center[0]) + np.square(cs[:,1] - center[1]))))

    return (rms,)


@app.cell
def _(centroid, np, sim):
    sims1 = [sim(center=(0.0, 0.0)) for m in range(100)]
    cs1 = np.array([centroid(s, scale=scale) for (s, scale) in sims1])
    return cs1, sims1


@app.cell
def _(centroid, cs1, plt, sims1):
    fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(8, 4))
    ax1a.imshow(sims1[0][0], cmap="gray")
    cx, cy = centroid(sims1[0][0])
    ax1a.vlines(cx, 0, 6, color="red")
    ax1a.hlines(cy, 0, 6, color="red")
    ax1b.hist(cs1[:,0], bins="auto")
    fig1.tight_layout()
    fig1
    return


@app.cell
def _(cs1, rms):
    rms(cs1)
    return


@app.cell
def _(centroid, np, rms, sim):
    rmss = []
    for n in np.logspace(0, 5, 15):
        sims = [sim(Nphoton=n) for m in range(100)]
        cs = np.array([centroid(s, scale=sc) for (s, sc) in sims])
        rmss.append(rms(cs))
    return (rmss,)


@app.cell
def _(np, plt, rmss):
    fig2, ax2 = plt.subplots()
    ax2.scatter(np.logspace(0, 5, 15), rmss)
    ax2.loglog(np.logspace(0, 5, 10), 1 / np.sqrt(np.logspace(0, 5, 10)), color="orange")
    ax2.set_aspect('equal', 'box')
    fig2.tight_layout()
    fig2
    return


@app.cell
def _(centroid, np, sim):
    sims3a = [sim(Nphoton=1000) for m in range(100)]
    cs3a = np.array([centroid(s, scale=sc) for (s, sc) in sims3a])
    sims3b = [sim(Nphoton=1000, center=(0.3, 0.0)) for m in range(100)]
    cs3b = np.array([centroid(s, scale=sc) for (s, sc) in sims3b])
    sims3c = [sim(Nphoton=1000, center=(-0.3, 0.0)) for m in range(100)]
    cs3c = np.array([centroid(s, scale=sc) for (s, sc) in sims3c])
    return cs3a, cs3b, cs3c


@app.cell
def _(cs3a, cs3b, cs3c, plt):
    fig3, (ax3a, ax3b, ax3c) = plt.subplots(1, 3, figsize=(9, 3))
    ax3a.hist(cs3a[:, 0] - 0.0, bins="auto")
    ax3b.hist(cs3b[:, 0] - 0.3, bins="auto")
    ax3c.hist(cs3c[:, 0] - (-0.3), bins="auto")
    fig3.tight_layout()
    fig3
    return


@app.cell
def _(centroid, np, sim):
    Dxs = []
    for p in np.linspace(-7, 7, 10):
       sms = [sim(Nphoton=1000) for m in range(100)]
       Dxs.append(np.mean([centroid(s, scale=sc)[0] - p for (s, sc) in sms]))
    return (Dxs,)


@app.cell
def _(Dxs, np, plt):
    fig4, ax4 = plt.subplots()
    ax4.scatter(np.linspace(-0.5, 0.5, 10), Dxs)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
