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
    plt.ion();
    return (plt,)


@app.cell
def _():
    import numpy as np

    return (np,)


@app.cell
def _():
    from skimage import io
    from skimage.filters import gaussian, median, threshold_otsu

    return gaussian, io, median, threshold_otsu


@app.cell
def _():
    import scipy.ndimage as ndi

    return (ndi,)


@app.cell
def _(mo):
    from pathlib import Path
    mo.pdf(src=Path("Homework3.pdf"), width="100%", height="50vh")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convolution and Filtering
    """)
    return


@app.cell
def _(io):
    escher_relativity_png = io.imread("escher-relativity.png", as_gray=True)
    return (escher_relativity_png,)


@app.cell
def _(escher_relativity_png, plt):
    fig1, ax1 = plt.subplots()
    p1 = ax1.imshow(escher_relativity_png, cmap="gray")
    cbar1 = fig1.colorbar(p1, ax=ax1)
    fig1
    return


@app.cell
def _(np):
    avgker11 = np.ones((11, 11)) / np.square(11)
    return (avgker11,)


@app.cell
def _(avgker11, escher_relativity_png, ndi):
    escher_relativity_png_avgd_const = ndi.convolve(escher_relativity_png, avgker11, mode="constant")
    escher_relativity_png_avgd_miror = ndi.convolve(escher_relativity_png, avgker11, mode="mirror")
    return escher_relativity_png_avgd_const, escher_relativity_png_avgd_miror


@app.cell
def _(escher_relativity_png_avgd_const, escher_relativity_png_avgd_miror, plt):
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(8, 4))
    p2a = ax2a.imshow(escher_relativity_png_avgd_const, cmap="gray")
    p2b = ax2b.imshow(escher_relativity_png_avgd_miror, cmap="gray")
    fig2.colorbar(p2a, ax=ax2a)
    fig2.colorbar(p2b, ax=ax2b)
    fig2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Gaussian Filtering
    """)
    return


@app.cell
def _(np):
    def gaussker(sgm2, shape=(11, 11)):
        xs, ys = np.meshgrid(np.arange(shape[0]), np.arange(shape[1]))
        r2s = np.square(xs - shape[0] // 2) + np.square(ys - shape[0] // 2)
        e = np.exp(- r2s / (2 * sgm2))
        return e / np.sum(e)  # return normalized kernel

    return (gaussker,)


@app.cell
def _(gaussker, plt):
    fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(8, 4))
    p3a = ax3a.imshow(gaussker(3))
    p3b = ax3b.imshow(gaussker(7))
    fig3.colorbar(p3a, ax=ax3a)
    fig3.colorbar(p3b, ax=ax3b)
    fig3
    return


@app.cell
def _(escher_relativity_png, gaussker, ndi):
    escher_relativity_png_gaussd3 = ndi.convolve(escher_relativity_png, gaussker(3))
    escher_relativity_png_gaussd7 = ndi.convolve(escher_relativity_png, gaussker(7))
    return escher_relativity_png_gaussd3, escher_relativity_png_gaussd7


@app.cell
def _(escher_relativity_png_gaussd3, escher_relativity_png_gaussd7, plt):
    fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(8, 4))
    p4a = ax4a.imshow(escher_relativity_png_gaussd3, cmap="gray")
    p4b = ax4b.imshow(escher_relativity_png_gaussd7, cmap="gray")
    fig4.colorbar(p4a, ax=ax4a)
    fig4.colorbar(p4b, ax=ax4b)
    fig4
    return


@app.cell
def _(escher_relativity_png, gaussian, np):
    escher_relativity_png_gaussdsk7 = gaussian(escher_relativity_png, np.sqrt(7))
    return (escher_relativity_png_gaussdsk7,)


@app.cell
def _(escher_relativity_png_gaussdsk7, plt):
    fig5, ax5 = plt.subplots()
    p5 = ax5.imshow(escher_relativity_png_gaussdsk7, cmap="gray")
    fig5.colorbar(p5, ax=ax5)
    fig5
    return


@app.cell
def _(escher_relativity_png_gaussd7, escher_relativity_png_gaussdsk7, np):
    escher_relativity_png_skdiff = escher_relativity_png_gaussdsk7 - escher_relativity_png_gaussd7
    escher_relativity_png_skdiff = escher_relativity_png_skdiff - np.min(escher_relativity_png_skdiff)
    return (escher_relativity_png_skdiff,)


@app.cell
def _(escher_relativity_png_skdiff, plt):
    fig6, ax6 = plt.subplots()
    p6 = ax6.imshow(escher_relativity_png_skdiff, cmap="gray")
    fig6.colorbar(p6, ax=ax6)
    fig6
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Median Filtering
    """)
    return


@app.cell
def _(escher_relativity_png, median, np):
    escher_relativity_png_median7 = median(escher_relativity_png, np.ones((7, 7)))
    return (escher_relativity_png_median7,)


@app.cell
def _(escher_relativity_png_median7, plt):
    fig7, ax7 = plt.subplots()
    p7 = ax7.imshow(escher_relativity_png_median7, cmap="gray")
    fig7.colorbar(p7, ax=ax7)
    fig7
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filtering and Thresholding
    """)
    return


@app.cell
def _(io):
    makeup_richardprince_1983_gray_png = io.imread("MakeUp_RichardPrince_1983_gray.png", as_gray=True)
    return (makeup_richardprince_1983_gray_png,)


@app.cell
def _(makeup_richardprince_1983_gray_png, plt):
    fig8, ax8 = plt.subplots()
    p8 = ax8.imshow(makeup_richardprince_1983_gray_png, cmap="gray")
    fig8.colorbar(p8, ax=ax8)
    fig8
    return


@app.cell
def _(gaussian, makeup_richardprince_1983_gray_png, np, threshold_otsu):
    makeup_richardprince_1983_gray_png_gaussian = 255 * gaussian(makeup_richardprince_1983_gray_png, np.sqrt(51))
    makeup_richardprince_1983_gray_png_gaussian_gthreshold = threshold_otsu(makeup_richardprince_1983_gray_png_gaussian)
    makeup_richardprince_1983_gray_png_gaussian_threshd = makeup_richardprince_1983_gray_png_gaussian > makeup_richardprince_1983_gray_png_gaussian_gthreshold
    return (makeup_richardprince_1983_gray_png_gaussian_threshd,)


@app.cell
def _(makeup_richardprince_1983_gray_png, median, np, threshold_otsu):
    makeup_richardprince_1983_gray_png_median = median(makeup_richardprince_1983_gray_png, np.ones((51, 51)))
    makeup_richardprince_1983_gray_png_median_gthreshold = threshold_otsu(makeup_richardprince_1983_gray_png_median)
    makeup_richardprince_1983_gray_png_median_threshd = makeup_richardprince_1983_gray_png_median > makeup_richardprince_1983_gray_png_median_gthreshold
    return (makeup_richardprince_1983_gray_png_median_threshd,)


@app.cell
def _(
    makeup_richardprince_1983_gray_png_gaussian_threshd,
    makeup_richardprince_1983_gray_png_median_threshd,
    plt,
):
    fig9, (ax9a, ax9b) = plt.subplots(1, 2, figsize=(8, 4))
    p9a = ax9a.imshow(makeup_richardprince_1983_gray_png_gaussian_threshd, cmap="gray")
    fig9.colorbar(p9a, ax=ax9a)
    p9b = ax9b.imshow(makeup_richardprince_1983_gray_png_median_threshd, cmap="gray")
    fig9.colorbar(p9b, ax=ax9b)
    fig9
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## High-pass Filtering
    """)
    return


@app.cell
def _(io):
    elevator_to_the_gallows_png = io.imread("Elevator_to_the_gallows.png", as_gray=True)
    return (elevator_to_the_gallows_png,)


@app.cell
def _(elevator_to_the_gallows_png, plt):
    fig10, ax10 = plt.subplots()
    ax10.imshow(elevator_to_the_gallows_png, cmap="gray")
    fig10
    return


@app.cell
def _(gaussian, np):
    def gausshighpass(image, sigma=np.sqrt(7)):
        gaussd = (np.max(image) - np.min(image)) * gaussian(image, sigma)
        diff = image - gaussd
        diff = diff - np.min(diff)
        return (255 / np.max(diff)) * diff

    return (gausshighpass,)


@app.cell
def _(elevator_to_the_gallows_png, gausshighpass):
    elevator_to_the_gallows_png_highpass = gausshighpass(elevator_to_the_gallows_png, sigma=21)
    return (elevator_to_the_gallows_png_highpass,)


@app.cell
def _(elevator_to_the_gallows_png_highpass, plt):
    fig11, ax11 = plt.subplots()
    ax11.imshow(elevator_to_the_gallows_png_highpass, cmap="gray")
    fig11
    return


@app.cell
def _(elevator_to_the_gallows_png_highpass, threshold_otsu):
    elevator_to_the_gallows_png_highpass_threshold = threshold_otsu(elevator_to_the_gallows_png_highpass)
    elevator_to_the_gallows_png_highthresh = elevator_to_the_gallows_png_highpass > elevator_to_the_gallows_png_highpass_threshold
    return (elevator_to_the_gallows_png_highthresh,)


@app.cell
def _(elevator_to_the_gallows_png_highthresh, plt):
    fig12, ax12 = plt.subplots()
    ax12.imshow(elevator_to_the_gallows_png_highthresh, cmap="gray")
    fig12
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Band-pass Filtering
    """)
    return


@app.cell
def _(io):
    gaussians_s2_to_s50_px_tif = io.imread("gaussians_s2_to_s50_px.tif", as_gray=True)
    return (gaussians_s2_to_s50_px_tif,)


@app.cell
def _(gaussians_s2_to_s50_px_tif, plt):
    fig13, (ax13a, ax13b) = plt.subplots(1, 2, figsize=(8, 4))
    ax13a.imshow(gaussians_s2_to_s50_px_tif, cmap="gray")
    ax13a.hlines(1240, 0, 3200, color="magenta")
    ax13b.plot(gaussians_s2_to_s50_px_tif[1240, :])
    fig13
    return


@app.cell
def _(gaussian, np):
    def gausslowpass(image, sigma=np.sqrt(7)):
        gaussd = (np.max(image) - np.min(image)) * gaussian(image, sigma)
        return (255 / np.max(gaussd)) * gaussd

    return (gausslowpass,)


@app.cell
def _(gausshighpass, gaussians_s2_to_s50_px_tif, gausslowpass):
    gaussians_s2_to_s50_px_tif_bandpassed = gausslowpass(gausshighpass(
        gaussians_s2_to_s50_px_tif, 
        sigma=20), sigma=10)
    return (gaussians_s2_to_s50_px_tif_bandpassed,)


@app.cell
def _(gaussians_s2_to_s50_px_tif_bandpassed, plt):
    fig14, (ax14a, ax14b) = plt.subplots(1, 2, figsize=(8, 4))
    ax14a.imshow(gaussians_s2_to_s50_px_tif_bandpassed, cmap="gray")
    ax14a.hlines(1240, 0, 3200, color="magenta")
    ax14b.plot(gaussians_s2_to_s50_px_tif_bandpassed[1240, :])
    fig14
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Signal to Noise Ratio
    """)
    return


@app.cell
def _(np):
    rng = np.random.default_rng()
    def sim_image(r, b=2, t=2, size=(27, 27)):
        bg = rng.poisson(lam=b * t, size=size)
        sg = np.zeros_like(bg)
        sg[sg.shape[0] // 2, sg.shape[1] // 2] = rng.poisson(lam=r*t)
        return bg + sg

    return (sim_image,)


@app.cell
def _(plt, sim_image):
    fig15, (ax15a, ax15b, ax15c) = plt.subplots(1, 3, figsize=(10, 4))
    ax15a.imshow(sim_image(2, t=1), cmap="gray")
    ax15b.imshow(sim_image(6, t=1), cmap="gray")
    ax15c.imshow(sim_image(10, t=1), cmap="gray")
    return


@app.cell
def _(np, sim_image):
    exposure_sims = [ sim_image(0.5, t=t) for t in range(0, 300) ]
    sns = [s[27//2, 27//2] / np.std(s) for s in exposure_sims]  
    return (sns,)


@app.cell
def _(plt, sns):
    fig16, ax16 = plt.subplots()
    ax16.scatter(range(0, 300), sns)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A little bit of Fourier Transforming
    """)
    return


@app.cell
def _(io):
    Lincoln_Coleman_png = io.imread("Lincoln_Coleman_40-copyright-havecamerawilltravel-com_crop512_gray.png", as_gray=True)
    return (Lincoln_Coleman_png,)


@app.cell
def _(Lincoln_Coleman_png, plt):
    fig17, ax17 = plt.subplots()
    ax17.imshow(Lincoln_Coleman_png, cmap="grey")
    return


@app.cell
def _():
    # %load fourier_masking_HWproblem.py
    return


@app.cell
def _(io, np, plt):
    # %load fourier_masking_HWproblem.py
    # fourier_masking_HWproblem.py
    """
    Author:   Raghuveer Parthasarathy
    Created on Tue Oct  8 07:25:53 2024
    Last modified on Oct. 12, 2024

    Description
    -----------

    For a homework problem on masking Fourier Transforms

    """

    #import numpy as np
    #import matplotlib.pyplot as plt
    import os
    #from skimage import io  # input output sub-package


    # %% Load the image

    parentDir = r"./"
    fileName = r"Lincoln_Coleman_40-copyright-havecamerawilltravel-com_crop512_gray.png"

    im = io.imread(os.path.join(parentDir, fileName))

    if im.ndim > 2:
        # A bit silly, since I know this is 2D
        im = np.mean(im, axis=2, dtype=im.dtype)

    print("Image shape: ", im.shape)
    # Image size; I'm not checking if it's square!
    # The Lincoln Memorial image is 512x512
    N = im.shape[0]

    plt.figure()
    plt.imshow(im, "gray")
    plt.title("Original Image")

    # %% Fourier Transform

    # Perform 2D Fourier transform
    F = np.fft.fft2(im)  # Fast Fourier Transform
    F_shifted = np.fft.fftshift(F)  # Shift so zero frequency is in the center

    # Calculate the amplitude and phase
    amplitude = np.abs(F_shifted)
    phase = np.angle(F_shifted)

    # Display amplitude as an image
    plt.figure()
    plt.title("Fourier Transform Amplitude (log scale)")
    # Should maybe add an offset to avoid -Inf,
    # but I've tested and there are no zeros.
    plt.imshow(np.log(amplitude), cmap="gray")
    plt.colorbar()
    plt.show()

    # Display phase as an image
    plt.figure()
    plt.title("Fourier Transform Phase (radians)")
    plt.imshow(phase)
    plt.colorbar()
    plt.show()

    # %% Masking

    # "Fundamental frequency" for the mask
    f0 = 15  # I determined this "by hand"
    # Full width of the mask -- should be an even number
    df = 4

    # Create a mask array
    mask = np.ones((N, N))
    for k in range(1, N // (2 * f0)):
        center_f = N / 2 + k * f0
        mask[:, int(center_f - df / 2) : int(center_f + df / 2)] = 0
        center_f = N / 2 - k * f0
        mask[:, int(center_f - df / 2) : int(center_f + df / 2)] = 0

    # Create a new amplitude array that is the original multiplied by this mask
    new_amplitude = amplitude * mask
    # new_amplitude = amplitude * (1.0 - mask) # show just the *difference*!

    # Display the new amplitude as an image
    plt.figure()
    plt.title("Amplitude * Mask")
    plt.imshow(np.log(new_amplitude + 0.1), cmap="gray")  # + 0.1 because of zeros.
    plt.colorbar()
    plt.show()


    # Combine new amplitude with original phase
    new_F_shifted = new_amplitude * np.exp(1j * phase)

    # Perform the inverse Fourier transform
    new_F = np.fft.ifftshift(new_F_shifted)
    new_im = np.fft.ifft2(new_F)
    new_im = np.abs(new_im)

    # Display the resulting image
    plt.figure()
    plt.title("Image based on Inverse FT")
    plt.imshow(new_im, cmap="gray")
    plt.colorbar()
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
