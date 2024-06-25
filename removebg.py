import cv2
import numpy as np

def remove_background(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a mask
    mask = np.zeros_like(gray)

    # Define background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Define the rectangle that includes the foreground object
    rect = (50, 50, image.shape[1] - 50, image.shape[0] - 50)

    # Apply GrabCut algorithm
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create mask where the background is 0 and the foreground is 1 or 3
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Multiply the image with the mask to remove the background
    result = image * mask2[:, :, np.newaxis]

    # Save the result
    cv2.imwrite(output_path, result)

    print("Background removed successfully. Saved as", output_path)

# Example usage
image_path = "C:/Users/yashs/Desktop/RESUMEQR/Yash_Resume1.png"
output_path = "output_image.png"
remove_background(image_path, output_path)
