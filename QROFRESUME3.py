import qrcode
import base64

# Function to encode the PDF file into base64
def encode_pdf_to_base64(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        base64_encoded = base64.b64encode(pdf_file.read())
    return base64_encoded

# Path to your PDF file
pdf_path = 'C:/Users/yashs/Desktop/RESUMEQR/Yash_Srivastava_resume.pdf'

# Encode your PDF file
encoded_pdf = encode_pdf_to_base64(pdf_path)

# Generate QR code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encoded_pdf)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill='black', back_color='white')
img.save('pdf_qr_code.png')
