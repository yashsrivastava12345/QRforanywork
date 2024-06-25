from PIL import Image
5
def merge_images(image1_path, image2_path, output_path):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Resize image2 to fit image1
    image2 = image2.resize(image1.size)

    # Combine the images
    merged_image = Image.alpha_composite(image1.convert("RGBA"), image2.convert("RGBA"))

    # Save the result
    merged_image.save(output_path)

# Example usage
image2_path = "C:/Users/yashs/Desktop/RESUMEQR/output_image.png"
image1_path = "C:/Users/yashs/Desktop/RESUMEQR/_DSC9305_.JPG"
output_path = "merged_image.png"

merge_images(image1_path, image2_path, output_path)
