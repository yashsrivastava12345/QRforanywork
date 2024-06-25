import qrcode
from PIL import Image
# Data to be encoded in the QR code
data = "https://drive.google.com/file/d/1_fWoSFmtNaAvbpnYk1NzidRPg9FMCNKk/view?usp=sharing"
# Generate QR code
background = Image.open('C:/Users/yashs/Desktop/RESUMEQR/_DSC9305_.JPG')
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill='white', back_color=background)

# Open the background image

# Calculate the position to place the QR code on the background
pos = ((background.size[0] - qr_img.size[0]) // 2, (background.size[1] - qr_img.size[1]) // 2)
# Paste the QR code onto the background
background.paste(qr_img, pos)
# Calculate the position to place the QR code on the background
pos = ((background.size[0] - qr_img.size[0]) // 2, (background.size[1] - qr_img.size[1]) // 2)
# Paste the QR code onto the background
background.paste(qr_img, pos)
background.save('qr_with_background.png')
