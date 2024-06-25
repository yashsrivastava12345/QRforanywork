import qrcode
from PIL import Image

def merge_qr_with_image(data, image_path, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Open the image
    image = Image.open(image_path)

    # Resize the QR code to fit onto the image
    qr_img = qr_img.resize((100, 100))  # Adjust the size as needed

    # Paste the QR code onto the image
    image.paste(qr_img, (50, 50))  # Adjust the position as needed

    # Save the resulting image
    image.save(output_path)

# Example usage
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
image_path = 'C:/Users/yashs/Desktop/RESUMEQR/_DSC9305_.JPG'
output_path = "merged_image.jpg"
merge_qr_with_image(data, image_path, output_path)
