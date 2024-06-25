import qrcode
from PIL import Image

def generate_qr_code_with_logo(data, logo_path, output_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="red", back_color="white")
    qr_img = qr_img.convert("RGBA")

    # Load the logo image
    logo = Image.open(logo_path)

    # Resize logo to fit the QR code
    qr_width, qr_height = qr_img.size
    logo_width, logo_height = logo.size
    logo_size = int(qr_width * 0.2), int(qr_height * 0.2)
    logo = logo.resize(logo_size)

    # Calculate the position to place the logo at the center
    position = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)

    # Paste the logo on the QR code
    qr_img.paste(logo, position, logo)

    # Save the QR code with logo
    qr_img.save(output_path)

# Example usage
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
logo_path = "C:/Users/yashs/Desktop/RESUMEQR/DSC_8226 (1).jpg"
output_path = "qr_code_with_logo.png"

generate_qr_code_with_logo(data, logo_path, output_path)
