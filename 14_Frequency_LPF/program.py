import cv2
import numpy as np

# Read grayscale input image
image = cv2.imread("Input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Convert image to floating-point type for DFT
image_float = np.float32(image)

# Compute 2D DFT using OpenCV
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low-frequency components to the center
dft_shift = np.fft.fftshift(dft, axes=(0, 1))

rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

# Create a low-pass frequency mask.
# A circular radius of 30 preserves central low frequencies.
mask = np.zeros((rows, cols, 2), np.float32)
cv2.circle(mask, (ccol, crow), 30, (1, 1), -1)

# Apply the low-pass mask
filtered_dft = dft_shift * mask

# Shift frequency representation back
filtered_dft = np.fft.ifftshift(filtered_dft, axes=(0, 1))

# Perform inverse DFT to reconstruct the filtered image
inverse_dft = cv2.idft(filtered_dft)

# Calculate magnitude of the reconstructed image
magnitude = cv2.magnitude(inverse_dft[:, :, 0], inverse_dft[:, :, 1])

# Normalize the result for image saving
output = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

output = np.uint8(output)

# Save reconstructed LPF output
cv2.imwrite("output.png", output)

print("Frequency-Domain Low-Pass Filtering completed successfully.")
print("Reconstructed LPF output saved as output.png")