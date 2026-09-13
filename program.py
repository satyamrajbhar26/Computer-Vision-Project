import cv2
import numpy as np

# Read the grayscale image
image = cv2.imread("Input.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Find minimum and maximum intensity values
min_intensity = np.min(image)
max_intensity = np.max(image)

print("Minimum intensity value:", min_intensity)
print("Maximum intensity value:", max_intensity)

# Check intensity range
if max_intensity == min_intensity:
    print("Image has no intensity range for contrast stretching.")
    exit()

# Perform contrast stretching
stretched = ((image - min_intensity) * 255.0 /
             (max_intensity - min_intensity))

# Keep values between 0 and 255
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

# Save enhanced image
cv2.imwrite("Output.jpg", stretched)

print("Contrast stretching completed.")
print("Enhanced image saved as Output.jpg")