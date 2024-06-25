import fitz  # PyMuPDF
import qrcode

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def extract_images_from_pdf(pdf_path):
    images = []
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            images.append(base_image)
    return images

def generate_qr_codes(data, output_path_prefix):
    chunk_size = 300  # Adjust the chunk size as needed
    num_chunks = (len(data) + chunk_size - 1) // chunk_size
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size
        chunk_data = data[start_idx:end_idx]
        qr.clear()  # Clear the QR code data
        qr.add_data(chunk_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        output_path = f"{output_path_prefix}_{i + 1}.png"
        qr_img.save(output_path)

# Example usage
#generate_qr_codes(combined_data, "output_qr_code")



def convert_pdf_to_qr(pdf_path, output_qr_path):
    text = extract_text_from_pdf(pdf_path)
    images = extract_images_from_pdf(pdf_path)
    combined_data = text + str(images)  # Combine text and image data
    generate_qr_codes(combined_data, output_qr_path)

# Example usage
convert_pdf_to_qr("C:/Users/yashs/Desktop/RESUMEQR/Yash_Srivastava_resume.pdf", "output_qr_code.png")
