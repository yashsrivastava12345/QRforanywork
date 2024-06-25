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

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # Load the logo image
    logo = Image.open(logo_path).convert("RGBA")

    # Resize logo to fit the QR code
    qr_width, qr_height = qr_img.size
    logo_width, logo_height = logo.size
    logo_size = int(qr_width * 0.2), int(qr_height * 0.2)
    logo = logo.resize(logo_size)

    # Calculate the position to place the logo at the center
    position = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)

    # Create a new image with alpha channel to paste the logo onto
    combined_img = Image.new("RGBA", qr_img.size, (255, 255, 255, 0))

    # Paste the QR code onto the new image
    combined_img.paste(qr_img, (0, 0))

    # Paste the logo onto the new image
    combined_img.paste(logo, position, logo)

    # Save the QR code with logo
    combined_img.save(output_path)

# Example usage
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
logo_path = "C:/Users/yashs/Desktop/RESUMEQR/Picture1.png"
output_path = "Yash_Resume.png"
generate_qr_code_with_logo(data, logo_path, output_path)
