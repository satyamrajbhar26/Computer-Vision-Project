import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read grayscale image
image = cv2.imread("Input.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Input.jpg not found.")
    exit()

# Calculate histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
histogram = histogram.ravel()

# Find intensity value with highest frequency
highest_intensity = np.argmax(histogram)
highest_frequency = int(histogram[highest_intensity])

print("Intensity value with highest frequency:", highest_intensity)
print("Highest frequency:", highest_frequency)

# Plot histogram
plt.figure()
plt.plot(histogram)
plt.title("Grayscale Intensity Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.xlim([0, 256])

# Save histogram
plt.savefig("output.png")

# Display histogram
plt.show()

print("Histogram analysis completed.")
print("Histogram saved as output.png")