import cv2

# Read the image containing salt-and-pepper noise
image = cv2.imread("Input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Apply 5x5 median filter to remove impulse noise
filtered = cv2.medianBlur(image, 5)

# Save the filtered result
cv2.imwrite("Output.jpg", filtered)

print("Median filtering completed.")
print("Filtered image saved as Output.jpg")