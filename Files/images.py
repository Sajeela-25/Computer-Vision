import cv2

# Load images
image1 = cv2.imread("Images/image1.jpg")
image2 = cv2.imread("Images/image2.jpg")

# Check if images loaded successfully
if image1 is None or image2 is None:
    print("Error: Could not load the images.")
else:
    print("Images loaded successfully!")

    # Display the images
    cv2.imshow("Image 1", image1)
    cv2.imshow("Image 2", image2)

    # Wait for a key press
    cv2.waitKey(0)

    # Close the windows
    cv2.destroyAllWindows()
