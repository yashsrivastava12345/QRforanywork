import qrcode
from PIL import Image

def generate_qr_code_with_logo(data, background_image_path, logo_path, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="lightgray", back_color="transparent").convert("RGBA")

    # Load the background image
    bg_img = Image.open(background_image_path)

    # Resize the background image to match the QR code's dimensions
    bg_img = bg_img.resize(qr_img.size)

    # Composite the QR code onto the background image
    combined_img = Image.alpha_composite(bg_img.convert("RGBA"), qr_img)

    # Load the logo image
    logo = Image.open(logo_path).convert("RGBA")

    # Resize logo to fit the QR code
    qr_width, qr_height = qr_img.size
    logo_width, logo_height = logo.size
    logo_size = int(qr_width * 0.2), int(qr_height * 0.2)
    logo = logo.resize(logo_size)

    # Calculate the position to place the logo at the center
    position = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)

    # Paste the logo onto the combined image
    combined_img.paste(logo, position, logo)

    # Save the QR code with logo
    combined_img.save(output_path)

# Example usage
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
logo_path = "C:/Users/yashs/Desktop/RESUMEQR/Picture2.png"
background_image_path = "C:/Users/yashs/Desktop/RESUMEQR/_DSC9305_.JPG"
#logo_path = "logo.png"
output_path = "Yash_resume_with_logo_and_bg.png"

generate_qr_code_with_logo(data, background_image_path, logo_path, output_path)
