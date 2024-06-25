import qrcode
from PIL import Image

def create_qr_with_background(data, background_image_path, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

    # Open the background image
    background_img = Image.open(background_image_path)

    # Resize the QR code to fit onto the background image
    qr_img = qr_img.resize(background_img.size)

    # Paste the QR code onto the background image
    result = Image.alpha_composite(background_img.convert('RGBA'), qr_img)

    # Save the resulting image
    result.save(output_path)

# Example usage
data = "https://example.com"
background_image_path = 'C:/Users/yashs/Desktop/RESUMEQR/_DSC9305_.JPG'
output_path = "qr_with_background.png"
create_qr_with_background(data, background_image_path, output_path)
