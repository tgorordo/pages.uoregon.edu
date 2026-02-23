# -*- coding: utf-8 -*-
# frequency_modulation_hw.py

"""
Author:   Raghuveer Parthasarathy
Created on Oct. 17, 2024
Last modified on Oct. 18, 2024

Description
-----------

For a homework problem on frequency modulation

"""


import numpy as np
import matplotlib.pyplot as plt
import os
from skimage import io # input output sub-package 

#%% Load the image

parentDir = r'C:\Users\Raghu\Documents\Teaching\Image Analysis Course\Images for Class'
fileName = r'Buster_Keaton_General_Train_512.png'

im = io.imread(os.path.join(parentDir, fileName))

print('Image shape: ', im.shape)
N = im.shape[0]

plt.figure()
plt.imshow(im, 'gray')
plt.title('Original Image')


#%% Multiply by sine waves

xc = np.linspace(-N/2, N/2, N)
x, y = np.meshgrid(xc, xc)
Px = 8
Py = 15
sineWave = np.sin(2.0*np.pi*x/Px) # + np.sin(2.0*np.pi*y/Py) 
im_mod = im*sineWave
# Rescale to [0, 255]
im_mod = 255.0*(im_mod - np.min(im_mod)) / (np.max(im_mod) - np.min(im_mod))
im_mod = np.clip(im_mod, 0, 255).astype('uint8')
plt.figure()
plt.imshow(im_mod, 'gray')
plt.title('Modified Image')

# Output
outputFileName = r'Buster_Keaton_General_Train_512_sineMod.png'

io.imsave(os.path.join(parentDir, outputFileName), im_mod)

#%% Fourier Transforms

# Perform 2D Fourier transform of the original
F = np.fft.fft2(im)  # Fast Fourier Transform
F_shifted = np.fft.fftshift(F)  # Shift so zero frequency is in the center

# Calculate the amplitude and phase
amplitude = np.abs(F_shifted)
phase = np.angle(F_shifted)

# Display amplitude as an image
plt.figure()
plt.title("Fourier Transform Amplitude (log scale)")
plt.imshow(np.log(amplitude), cmap='gray') 
plt.colorbar()
plt.show()

# Perform 2D Fourier transform of the modified image
F_mod = np.fft.fft2(im_mod)  # Fast Fourier Transform
F_shifted_mod = np.fft.fftshift(F_mod)  # Shift so zero frequency is in the center

# Calculate the amplitude and phase
amplitude_mod = np.abs(F_shifted_mod)
phase_mod = np.angle(F_shifted_mod)

# Display amplitude as an image
plt.figure()
plt.title("Fourier Transform Amplitude (log scale): modified image")
plt.imshow(np.log(amplitude_mod), cmap='gray') 
plt.colorbar()
plt.show()