from logo_qrcode import LogoQRCode

# URL or text to encode in the QR code
data = 'https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing'

# Path to the logo image
logo_path = 'C:/Users/yashs/Desktop/RESUMEQR/DSC_8226 (1).jpg'

# Path to save the generated QR code
output_path = 'My_Resume.png'

# Create a QR code object with the specified data and logo
qr = LogoQRCode(data=data, logo_path=logo_path)

# Save the QR code with the logo
qr.save(output_path)

print(f'QR code with logo saved as {output_path}')
