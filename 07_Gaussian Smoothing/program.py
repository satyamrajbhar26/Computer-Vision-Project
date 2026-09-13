import cv2

# Read the noisy image
image = cv2.imread("Input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# 5x5 is an odd kernel size suitable for reducing noise smoothly
smoothed = cv2.GaussianBlur(image, (5, 5), 0)

# Save the Gaussian smoothed image
cv2.imwrite("Output.jpg", smoothed)

print("Gaussian smoothing completed.")
print("Smoothed image saved as Output.jpg")