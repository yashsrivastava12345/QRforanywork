import qrcode
from PIL import Image

def create_custom_qr_code(data, background_image_path, output_path):
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

    # Load the background image
    bg_img = Image.open(background_image_path)

    # Resize the background image to match the QR code's dimensions
    bg_img = bg_img.resize(qr_img.size)

    # Composite the QR code onto the background image
    result = Image.alpha_composite(bg_img.convert('RGBA'), qr_img)

    # Save or display the result
    result.save(output_path)
    result.show()

# Example usage
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
background_image_path = "C:/Users/yashs/Desktop/RESUMEQR/_DSC9305_.JPG"
output_path = "custom_qr_code.png"

create_custom_qr_code(data, background_image_path, output_path)
