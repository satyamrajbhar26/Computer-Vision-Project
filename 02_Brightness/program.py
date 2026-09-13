import cv2
import numpy as np

# Read the dark image
image = cv2.imread("Input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Constant brightness value
brightness = 50

# Store one pixel value before enhancement
before = image[100, 100].copy()

# Increase brightness and keep pixel values within 0-255
enhanced = np.clip(image.astype(np.int16) + brightness, 0, 255).astype(np.uint8)

# Store the same pixel value after enhancement
after = enhanced[100, 100].copy()

# Save enhanced image
cv2.imwrite("Output.jpg", enhanced)

# Display pixel values in console
print("Pixel value before enhancement:", before)
print("Pixel value after enhancement:", after)

print("Brightness enhancement completed.")
print("Enhanced image saved as Output.jpg")