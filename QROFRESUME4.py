import qrcode
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def generate_qr_code(image_path, qr_data, output_pdf):
    # Load the image
    img = Image.open(image_path)
    width, height = img.size

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Resize QR code to fit the image
    qr_img = qr_img.resize((int(width * 0.2), int(height * 0.2)))

    # Position the QR code on the image
    img.paste(qr_img, (int(width * 0.8), int(height * 0.8)))

    # Save the image with QR code as PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)
    img_temp = "temp.jpg"
    img.save(img_temp)
    c.drawImage(ImageReader(img_temp), 0, 0, width, height)
    c.save()

    # Clean up temporary image
    import os
    os.remove(img_temp)

# Example usage
generate_qr_code("input_image.jpg", "https://example.com", "output_pdf_with_qr.pdf")
