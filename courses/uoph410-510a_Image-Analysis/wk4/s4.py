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
    from skimage import io, filters

    return filters, io


@app.cell
def _():
    import scipy as si
    import scipy.ndimage as nd

    return nd, si


@app.cell
def _():
    import matplotlib
    import matplotlib.pyplot as plt
    plt.ion();
    return (plt,)


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework4.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Frequency Modulation
    """)
    return


@app.cell
def _(io):
    buster_keaton_general_train_512_png = io.imread("Buster_Keaton_General_Train_512.png", as_gray=True)
    buster_keaton_general_train_512_sinmod_png = io.imread("Buster_Keaton_General_Train_512_sineMod.png", as_gray=True)
    return (
        buster_keaton_general_train_512_png,
        buster_keaton_general_train_512_sinmod_png,
    )


@app.cell
def _(
    buster_keaton_general_train_512_png,
    buster_keaton_general_train_512_sinmod_png,
    plt,
):
    fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(8, 4))
    ax1a.imshow(buster_keaton_general_train_512_png, cmap="gray")
    ax1b.imshow(buster_keaton_general_train_512_sinmod_png, cmap="gray")
    return


@app.cell
def _(
    buster_keaton_general_train_512_png,
    buster_keaton_general_train_512_sinmod_png,
    np,
):
    buster_keaton_general_train_512_fft = np.abs(np.fft.fftshift(np.fft.fft2(buster_keaton_general_train_512_png)))
    buster_keaton_general_train_512_sinmod_fft = np.abs(np.fft.fftshift(np.fft.fft2(buster_keaton_general_train_512_sinmod_png)))
    return (
        buster_keaton_general_train_512_fft,
        buster_keaton_general_train_512_sinmod_fft,
    )


@app.cell
def _(
    buster_keaton_general_train_512_fft,
    buster_keaton_general_train_512_sinmod_fft,
    np,
    plt,
):
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(8, 4))
    ax2a.imshow(np.log(buster_keaton_general_train_512_fft), cmap="gray")
    ax2b.imshow(np.log(buster_keaton_general_train_512_sinmod_fft), cmap="gray")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quantized Aggregates
    """)
    return


@app.cell
def _(io):
    emitters_33px_100ph_png = io.imread("emitters_33px_100ph.png")
    return (emitters_33px_100ph_png,)


@app.cell
def _(emitters_33px_100ph_png, plt):
    fig3, ax3 = plt.subplots()
    ax3.imshow(emitters_33px_100ph_png, cmap="gray")
    return


@app.cell
def _(emitters_33px_100ph_png, plt):
    fig4, ax4 = plt.subplots()
    ax4.hist(emitters_33px_100ph_png.ravel(), bins="auto")
    fig4
    return


@app.cell
def _(emitters_33px_100ph_png, filters):
    emitters_33px_100ph_hflt = emitters_33px_100ph_png - 255 * filters.gaussian(emitters_33px_100ph_png, 8, mode="nearest")
    return (emitters_33px_100ph_hflt,)


@app.cell
def _(emitters_33px_100ph_hflt, plt):
    fig6, (ax6a, ax6b) = plt.subplots(1, 2, figsize=(8, 4))
    ax6a.imshow(emitters_33px_100ph_hflt, cmap="gray")
    ax6b.hist(emitters_33px_100ph_hflt.ravel(), bins=20)
    fig6
    return


@app.cell
def _(emitters_33px_100ph_hflt, np):
    ones = np.ones_like(emitters_33px_100ph_hflt, dtype=bool)
    zeros = np.zeros_like(ones, dtype=bool)
    x, y = np.arange(ones.shape[0]), np.arange(ones.shape[1])
    xs, ys = np.meshgrid(x, y)
    masks = [np.where((np.abs(xs - 33 * i) <= 2) & (np.abs(ys - 33 * j) <= 2), ones, zeros) 
             for i in range(1, 11) for j in range(1, 11)]
    # mask = np.where((xs % (33 + 4) > (33 - 4)) & (ys % (33 + 4) > (33 - 4)), ones, zeros)
    mask = sum(masks)
    return mask, masks


@app.cell
def _(emitters_33px_100ph_hflt, masks, np):
    intensities = [np.sum(emitters_33px_100ph_hflt, where=m) for m in masks]
    return (intensities,)


@app.cell
def _(intensities, mask, plt):
    fig7, (ax7a, ax7b) = plt.subplots(1, 2, figsize=(8, 4))
    ax7a.imshow(mask, cmap="gray")
    counts, edges, _ = ax7b.hist(intensities, bins=25)
    fig7
    return counts, edges


@app.cell
def _(counts, edges, np):
    irange = (np.max(edges) - np.min(edges))
    imin = np.min(edges)
    (sum(counts[edges[1:] <= (irange/3) + imin]),
     sum(counts[((irange/3) + imin < edges[1:]) & (edges[1:] <= (2*irange/3) + imin)]),
     sum(counts[((2*irange/3) + imin < edges[1:])])
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A High-Resolution PSF
    """)
    return


@app.cell
def _(np, si):
    def psfker(l, NA=0.9, side=1.0, N=101, center=(0.0, 0.0)):
        xs, ys = np.meshgrid(np.linspace(0.0, side, N), np.linspace(0.0, side, N))
        r2s = np.square(xs - side / 2 - center[0]) + np.square(ys - side / 2 - center[1])
        v = 2 * np.pi * NA * np.sqrt(r2s) / l
        psf = 4 * np.square(si.special.j1(v) / v)
        nans = np.isnan(psf)
        psf[nans] = 1
        return psf / np.sum(psf)

    return (psfker,)


@app.cell
def _(plt, psfker):
    fig8, (ax8a, ax8b, ax8c) = plt.subplots(1, 3, figsize=(8, 2))
    ax8a.imshow(psfker(0.5), cmap="gray")
    ax8b.imshow(psfker(0.4), cmap="gray")
    ax8c.imshow(psfker(0.4, NA=0.5), cmap="gray")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A Worse Worm Image
    """)
    return


@app.cell
def _(io):
    fetter_celegans_cellfig10_png = io.imread("fetter_Celegans_cellfig10.jpg", as_gray=True)
    return (fetter_celegans_cellfig10_png,)


@app.cell
def _(fetter_celegans_cellfig10_png, plt):
    fig9, ax9 = plt.subplots()
    ax9.imshow(fetter_celegans_cellfig10_png, cmap="gray")
    return


@app.cell
def _(fetter_celegans_cellfig10_png, nd, psfker):
    fetter_celegans_cellfig10_psf = nd.convolve(fetter_celegans_cellfig10_png, psfker(0.53, NA=0.7))
    return (fetter_celegans_cellfig10_psf,)


@app.cell
def _(fetter_celegans_cellfig10_psf, plt):
    fig10, ax10 = plt.subplots()
    ax10.imshow(fetter_celegans_cellfig10_psf, cmap="gray")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## SNR and Poisson Noise
    $$ N_\text{photon} \sim SNR^2 $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simulated Point Sources
    """)
    return


@app.cell
def _(np):
    def pixelate(image, inscale, shape=(15, 15)):
        outscale = image.shape[0] * inscale / shape[0] 
        assert outscale == image.shape[1] * inscale / shape[1]
        assert outscale.is_integer()

        ii, jj = np.indices(image.shape)

        ones = np.ones_like(image, dtype=bool)
        zeros = np.zeros_like(image, dtype=bool)

        masks = [np.where((i * outscale <= ii * inscale) & 
                          (ii * inscale < (i + 1) * outscale)
                          & (j * outscale <= jj * inscale) & 
                          (jj * inscale < (j + 1) * outscale),
                          ones, zeros) 
                 for i in range(shape[0]) for j in range(shape[1])]

        outage = np.array([np.sum(image, where=m) for m in masks]).reshape(shape)

        return outage, outscale

    return (pixelate,)


@app.cell
def _(pixelate, psfker):
    simpoint, _ = pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150), 0.1)
    return (simpoint,)


@app.cell
def _(plt, simpoint):
    fig11, ax11 = plt.subplots()
    ax11.imshow(simpoint, cmap="gray")
    return


@app.cell
def _(np):
    def fishify(image, N=1, rng=np.random.default_rng()):
        return rng.poisson(lam=N * (image / np.sum(image)))

    return (fishify,)


@app.cell
def _(fishify, pixelate, psfker):
    simpoint50 = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150), 0.1)[0], N=50)
    simpoint500 = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150), 0.1)[0], N=500)
    return simpoint50, simpoint500


@app.cell
def _(plt, simpoint50, simpoint500):
    fig12, (ax12a, ax12b) = plt.subplots(1, 2, figsize=(8, 4))
    ax12a.imshow(simpoint50, cmap="gray")
    ax12b.imshow(simpoint500, cmap="gray")
    return


@app.cell
def _(fishify, pixelate, psfker):
    simpoint50_shifted = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150, center=(0.3, 0.3)), 0.1)[0], N=50)
    simpoint500_shifted = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150, center=(0.3, 0.3)), 0.1)[0], N=500)
    return simpoint500_shifted, simpoint50_shifted


@app.cell
def _(plt, simpoint500_shifted, simpoint50_shifted):
    fig13, (ax13a, ax13b) = plt.subplots(1, 2, figsize=(8, 4))
    ax13a.imshow(simpoint50_shifted, cmap="gray")
    ax13b.imshow(simpoint500_shifted, cmap="gray")
    return


@app.cell
def _(fishify, np, pixelate, psfker):
    uniform = np.ones((15, 15)) / np.sum(np.ones((15, 15)))
    simpoint_i = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150), 0.1)[0], N=50) + fishify(np.ones((15, 15)), N=2 * 15**2)
    simpoint_ii = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150, center=(0.03, 0.03)), 0.1)[0], N=50) + fishify(np.ones((15, 15)), N=2 * 15**2)
    simpoint_iii = fishify(pixelate(psfker(0.5, NA=0.9, side=15 * 0.1, N = 150, center=(0.03, 0.03)), 0.1)[0], N=500) + fishify(np.ones((15, 15)), N=2 * 15**2)
    return simpoint_i, simpoint_ii, simpoint_iii


@app.cell
def _(plt, simpoint_i, simpoint_ii, simpoint_iii):
    fig14, (ax14a, ax14b, ax14c) = plt.subplots(1, 3, figsize=(8, 2))
    ax14a.imshow(simpoint_i, cmap="gray")
    ax14b.imshow(simpoint_ii, cmap="gray")
    ax14c.imshow(simpoint_iii, cmap="gray")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Simulating a Ring
    """)
    return


@app.cell
def _(np):
    def ring(inner, outer, center=(0, 0), scale=1, shape=(150, 150), rtol=1e-02, atol=1e-02):
        ii, jj = np.indices(shape)
        r2s = np.square((ii - shape[0] / 2) * scale - center[0]) + np.square((jj - shape[1] / 2) * scale - center[1])
        return ((r2s < np.square(outer)) & (r2s >= np.square(inner))).astype(np.float32)

    return (ring,)


@app.cell
def _(fishify, nd, plt, psfker, ring):
    fig15, (ax15a, ax15b, ax15c) = plt.subplots(1, 3, figsize=(8, 4))
    ax15a.imshow(ring(0.5, 0.6, scale=0.01), cmap="gray")
    ax15b.imshow(nd.convolve(ring(0.5, 0.6, scale=0.01), psfker(0.1), mode="nearest"), cmap="gray")
    ax15c.imshow(fishify(nd.convolve(ring(0.5, 0.6, scale=0.01), psfker(0.1), mode="nearest"), N=10_000), cmap="gray")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
