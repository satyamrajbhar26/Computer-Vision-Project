import cv2

# Read the same noisy input image
image = cv2.imread("Input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Apply Mean, Gaussian and Median filters
mean_filtered = cv2.blur(image, (5, 5))
gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)
median_filtered = cv2.medianBlur(image, 5)

# Save all three results separately
cv2.imwrite("output_mean.png", mean_filtered)
cv2.imwrite("output_gaussian.png", gaussian_filtered)
cv2.imwrite("output_median.png", median_filtered)

print("Filter comparison completed.")
print("Mean result saved as output_mean.png")
print("Gaussian result saved as output_gaussian.png")
print("Median result saved as output_median.png")