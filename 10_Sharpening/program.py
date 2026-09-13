import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

# Check if image was loaded successfully
if image is None:
    print("Error: input.jpg not found.")
    exit()

# Custom 3x3 sharpening kernel
kernel = np.array([
    [0, -1,  0],
    [-1, 5, -1],
    [0, -1,  0]
], dtype=np.float32)

# Apply the custom sharpening kernel
sharpened_image = cv2.filter2D(image, -1, kernel)

# Save the sharpened image
cv2.imwrite("Output.jpg", sharpened_image)

print("Sharpening completed successfully.")
print("Output saved as Output.jpg")