import cv2
import numpy as np

# Read input image
image = cv2.imread("Input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Smoothing using Gaussian Blur
smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

# Sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)

# Apply sharpening
sharpened_image = cv2.filter2D(image, -1, kernel)

# Save output images
cv2.imwrite("output_smooth.png", smoothed_image)
cv2.imwrite("output_sharp.png", sharpened_image)

print("Smoothing and sharpening completed successfully.")
print("Output saved as output_smooth.png")
print("Output saved as output_sharp.png")