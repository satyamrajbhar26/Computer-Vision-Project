import cv2
import numpy as np

# Input image
image = cv2.imread("Input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Input.jpg not found.")
    print("Make sure Input.jpg is inside the same folder as program.py")
    exit()

# 2D Fourier Transform
dft = np.fft.fft2(image)

# Shift zero frequency component to the center
dft_shift = np.fft.fftshift(dft)

# Calculate magnitude spectrum
magnitude_spectrum = 20 * np.log(np.abs(dft_shift) + 1)

# Normalize for saving as an image
magnitude_spectrum = cv2.normalize(
    magnitude_spectrum,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

magnitude_spectrum = np.uint8(magnitude_spectrum)

# Save output
cv2.imwrite("Output.jpg", magnitude_spectrum)

print("Magnitude Spectrum computed successfully.")
print("Output saved as Output.jpg")