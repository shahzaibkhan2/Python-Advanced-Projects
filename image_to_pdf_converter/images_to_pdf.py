from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_images_to_pdf(image_list, output_filename):
    # Create a new PDF
    c = canvas.Canvas(output_filename, pagesize=letter)

    # Set page dimensions
    width, height = letter

    # Loop through each image and add it to the PDF
    for image_path in image_list:
        try:
            # Open the image using Pillow
            img = Image.open(image_path)

            # Resize the image to fit the PDF page
            img_width, img_height = img.size
            aspect_ratio = img_width / img_height
            if aspect_ratio >= 1:
                new_width = width - 50
                new_height = new_width / aspect_ratio
            else:
                new_height = height - 50
                new_width = new_height * aspect_ratio

            # Center the image on the page
            x_offset = (width - new_width) / 2
            y_offset = (height - new_height) / 2

            # Draw the image on the page
            c.drawImage(image_path, x_offset, y_offset, new_width, new_height)

            # Add a new page for the next image
            c.showPage()
        except IOError:
            print(f"Error: Unable to open image {image_path}")

    # Save the PDF
    c.save()

if __name__ == "__main__":
    # Provide a list of image file paths
    image_files = ["img1.jpg", "img2.jpg", "img3.jpg"]

    # Specify the output PDF file name
    output_file = "form.pdf"

    # Convert images to PDF
    convert_images_to_pdf(image_files, output_file)