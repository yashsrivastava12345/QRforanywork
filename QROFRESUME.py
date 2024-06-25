import qrcode
# Data to be encoded
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("Yash_Resume.png")
"""from fpdf import FPDF

class PDF(FPDF):
    pass  # Add other methods if necessary

# Create instance of FPDF class
pdf = PDF()
pdf.add_page()

# Assuming 'img' is the QR code image generated earlier
img.save("qr_code.png")
pdf.image("qr_code.png", x=10, y=8, w=100)
pdf.output("your_pdf_with_qr.pdf")
"""
