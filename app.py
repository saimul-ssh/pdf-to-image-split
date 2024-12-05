import fitz  # PyMuPDF
from PIL import Image
import os

def pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through pages
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Render the page to a pixmap
        pix = page.get_pixmap()
        
        # Convert pixmap to Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save image as PNG
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        img.save(image_path)
        print(f"Saved: {image_path}")
    
    pdf_document.close()
    print("All pages converted to images.")

# Usage Example
pdf_to_images(r"yourfile_name.pdf", "output_images")
