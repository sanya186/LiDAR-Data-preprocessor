import numpy as np
import cv2

def fft_process(img):
    # Apply FFT, shift zero frequency to center, magnitude spectrum
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift) + 1)
    magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    return magnitude_spectrum

def median_filter(img):
    # Median filter with kernel size 5
    filtered = cv2.medianBlur(img, 5)
    return filtered
