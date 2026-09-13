import cv2

# Read the input image
image = cv2.imread("Input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Apply mean filter with two different kernel sizes
filtered_3x3 = cv2.blur(image, (3, 3))
filtered_5x5 = cv2.blur(image, (5, 5))

# Save both results
cv2.imwrite("Output_3x3.jpg", filtered_3x3)
cv2.imwrite("Output.jpg", filtered_5x5)

print("Mean filtering completed.")
print("3x3 result saved as Output_3x3.jpg")
print("Final 5x5 result saved as Output.jpg")