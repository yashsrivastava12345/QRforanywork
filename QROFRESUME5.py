import fitz  # PyMuPDF
import qrcode
from PIL import Image

def generate_qr_code(pdf_path, qr_data, output_pdf):
    # Open the PDF and extract the first page
    pdf_document = fitz.open(pdf_path)
    first_page = pdf_document.load_page(0)
    pix = first_page.get_pixmap(alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

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
    qr_img = qr_img.resize((int(img.width * 0.2), int(img.height * 0.2)))

    # Overlay QR code onto the image
    img.paste(qr_img, (int(img.width * 0.8), int(img.height * 0.8)))

    # Save the image with QR code as PDF
    img.save(output_pdf)

# Example usage
generate_qr_code("C:/Users/yashs/Downloads/DSC_8226 (1).jpg", "C:/Users/yashs/Desktop/RESUMEQR/Yash_Srivastava_resume.pdf", "output_pdf_with_qr.png")
