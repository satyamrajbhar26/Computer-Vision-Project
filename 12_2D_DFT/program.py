import cv2
import numpy as np

# Read input image in grayscale
image = cv2.imread("Input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Convert image to float32
image_float = np.float32(image)

# Calculate 2D DFT
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Separate real and imaginary parts
real_part = dft[:, :, 0]
imaginary_part = dft[:, :, 1]

# Shift frequency components to the center
real_shifted = np.fft.fftshift(real_part)
imaginary_shifted = np.fft.fftshift(imaginary_part)

# Logarithmic scaling for clear visualization
real_output = np.log(1 + np.abs(real_shifted))
imaginary_output = np.log(1 + np.abs(imaginary_shifted))

# Normalize to 0-255
real_output = cv2.normalize(
    real_output, None, 0, 255, cv2.NORM_MINMAX
).astype(np.uint8)

imaginary_output = cv2.normalize(
    imaginary_output, None, 0, 255, cv2.NORM_MINMAX
).astype(np.uint8)

# Save DFT outputs
cv2.imwrite("DFT_Real.jpg", real_output)
cv2.imwrite("DFT_Imaginary.jpg", imaginary_output)

print("2D DFT computation completed successfully.")
print("DFT Real part saved as DFT_Real.jpg")
print("DFT Imaginary part saved as DFT_Imaginary.jpg")