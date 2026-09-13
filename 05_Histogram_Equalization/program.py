import cv2

img = cv2.imread("Input.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Input.jpg not found.")
else:
    equalized = cv2.equalizeHist(img)

    cv2.imwrite("output_original.jpg", img)
    cv2.imwrite("output_equalized.jpg", equalized)

    print("Histogram Equalization completed.")
    print("Original image saved as output_original.jpg")
    print("Equalized image saved as output_equalized.jpg")

    cv2.imshow("Original", img)
    cv2.imshow("Equalized", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
