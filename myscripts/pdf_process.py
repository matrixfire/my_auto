##########################################################################


##########################################################################


import fitz  # PyMuPDF
import os

def images_to_pdf(images_path, output_pdf_path):
    # Create a new PDF document
    pdf_document = fitz.open()

    # List all image files in the directory
    image_files = [f for f in os.listdir(images_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp'))]
    image_files.sort()  # Optional: sort files by name to ensure order

    if not image_files:
        print("No images found in the directory.")
        return

    for image_file in image_files:
        image_path = os.path.join(images_path, image_file)
        # Open the image file
        img_document = fitz.open(image_path)
        # Get the first page of the image document
        img_page = img_document.load_page(0)
        # Create a new PDF page with the same dimensions as the image
        pdf_page = pdf_document.new_page(width=img_page.rect.width, height=img_page.rect.height)
        # Insert the image into the PDF page
        pdf_page.insert_image(pdf_page.rect, filename=image_path)
        img_document.close()

    # Save the PDF
    pdf_document.save(output_pdf_path)
    pdf_document.close()

    print(f"Combined images into PDF and saved to '{output_pdf_path}'.")

if __name__ == "__main__":
    # Get paths from user input
    images_path = input("Enter the path for images: ").strip().strip('"')
    output_pdf_path = input("Enter the path for the output PDF: ").strip().strip('"')

    images_to_pdf(images_path, os.path.join(output_pdf_path, "combined_images.pdf"))




##########################################################################

import fitz  # PyMuPDF
import pyinputplus as pyip
import os

def extract_pages_p(pdf_path, start_page, end_page, output_path=None):
    # Open the original PDF
    pdf_document = fitz.open(pdf_path)

    # Check if the page numbers are within the range
    num_pages = pdf_document.page_count
    if start_page < 1 or end_page > num_pages or start_page > end_page:
        print(f"Invalid page range. The PDF has {num_pages} pages.")
        return

    # Create a new PDF to save the extracted pages
    new_pdf_document = fitz.open()

    # Extract pages from start_page to end_page (inclusive)
    for page_num in range(start_page - 1, end_page):
        page = pdf_document.load_page(page_num)
        new_pdf_document.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    # Determine the output path
    if output_path is None:
        base_name, ext = os.path.splitext(pdf_path)
        output_path = f"{base_name}({start_page}-{end_page}){ext}"

    # Save the new PDF
    new_pdf_document.save(output_path)
    new_pdf_document.close()
    pdf_document.close()

    print(f"Extracted pages {start_page} to {end_page} and saved to '{output_path}'.")

def extract():
    # Prompting for input using pyinputplus
    pdf_path = input(f"Enter the path for PDF: ").strip().strip('"')
    start_page = pyip.inputInt(prompt="Enter the start page number: ", min=1)
    end_page = pyip.inputInt(prompt="Enter the end page number: ", min=start_page)

    # Call the function with default output_path logic
    extract_pages_p(pdf_path, start_page, end_page)


extract()

##########################################################################

import fitz  # PyMuPDF
import os

def combine_pdfs():
    # Step 1: Ask how many PDFs the user wants to combine
    num_pdfs = int(input("How many PDFs do you want to combine? "))
    
    # Step 2: Collect paths for each PDF
    pdf_paths = []
    for i in range(num_pdfs):
        pdf_path = input(f"Enter the path for PDF {i+1}: ").strip().strip('"')  # Remove quotes and spaces
        pdf_paths.append(pdf_path)
    
    # Step 3: Create a new PDF where the combined result will be saved
    output_pdf = fitz.open()

    # Step 4: Loop through each PDF and append its pages to the output PDF
    for pdf_path in pdf_paths:
        pdf_document = fitz.open(pdf_path)  # Open the current PDF
        for page_num in range(pdf_document.page_count):
            output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
        pdf_document.close()
    
    # Step 5: Define and save the combined PDF output path
    output_file_name = "combined_output.pdf"
    output_file_path = os.path.abspath(output_file_name)
    output_pdf.save(output_file_path)
    output_pdf.close()

    # Step 6: Print the absolute path of the combined output PDF
    print(f"PDFs have been successfully combined. The combined file is saved at:\n{output_file_path}")

# Call the function to combine PDFs
combine_pdfs()


##########################################################################



import fitz  # PyMuPDF
import os

def interleaving_combine_pdfs_with_circles():
    # Step 1: Ask how many PDFs the user wants to combine
    num_pdfs = int(input("Enter the number of PDFs to combine: "))
    
    if num_pdfs < 2:
        print("You need at least 2 PDFs to perform interleaving.")
        return
    
    # Step 2: Collect paths for all PDFs
    pdf_paths = []
    for i in range(num_pdfs):
        pdf_path = input(f"Enter the path for PDF {i+1}: ").strip().strip('"')  # Remove quotes and spaces
        pdf_paths.append(pdf_path)
    
    # Step 3: Open all PDFs
    pdfs = [fitz.open(path) for path in pdf_paths]
    
    # Step 4: Create a new PDF for the combined result
    output_pdf = fitz.open()

    # Step 5: Get the maximum page count across all PDFs
    max_pages = max(pdf.page_count for pdf in pdfs)

    # Step 6: Define colors for the circles (more colors can be added here)
    colors = [
        (1, 0, 0),   # Red
        (0, 0, 1),   # Blue
        (0, 1, 0),   # Green
        (1, 1, 0),   # Yellow
        (1, 0, 1),   # Magenta
        (0, 1, 1)    # Cyan
    ]

    # Step 7: Interleave pages from all PDFs with circles
    for page_num in range(max_pages):
        for i, pdf in enumerate(pdfs):
            if page_num < pdf.page_count:
                # Insert the page from the current PDF
                output_pdf.insert_pdf(pdf, from_page=page_num, to_page=page_num)
                # Add a colored circle, alternating based on the PDF number
                page = output_pdf[-1]  # Get the last added page
                draw_colored_circle(page, colors[i % len(colors)])  # Alternate through the colors

    # Step 8: Save the combined PDF output path
    output_file_name = "interleaved_output_with_circles.pdf"
    output_file_path = os.path.abspath(output_file_name)
    output_pdf.save(output_file_path)
    output_pdf.close()
    
    # Close the individual PDFs
    for pdf in pdfs:
        pdf.close()

    # Step 9: Print the absolute path of the combined output PDF
    print(f"PDFs have been successfully interleaved with colored circles. The combined file is saved at:\n{output_file_path}")

# Helper function to draw a small circle at the top-left corner of a PDF page
def draw_colored_circle(page, color):
    # Define circle position and size
    circle_center = (30, 30)  # Coordinates near the top-left corner
    circle_radius = 10        # Radius of the circle
    
    # Create a circle using the draw_circle method
    page.draw_circle(center=circle_center, radius=circle_radius, color=color, fill=color)

# Call the function to combine PDFs with colored circles
interleaving_combine_pdfs_with_circles()

##########################################################################

import fitz  # PyMuPDF
import os

def interleave_pdfs_with_grouped_pages():
    # Step 1: Ask how many PDFs the user wants to combine
    num_pdfs = int(input("Enter the number of PDFs to combine: "))
    
    if num_pdfs < 2:
        print("You need at least 2 PDFs to perform interleaving.")
        return
    
    # Step 2: Collect paths and page group sizes for all PDFs
    pdf_paths = []
    pages_per_pdf = []
    
    for i in range(num_pdfs):
        pdf_path = input(f"Enter the path for PDF {i+1}: ").strip().strip('"')  # Remove quotes and spaces
        pdf_paths.append(pdf_path)
        
        # Ask for the number of pages to treat as a group for the current PDF
        pages_group = input(f"Enter the number of pages to treat as a group for PDF {i+1} (default is 1): ")
        pages_per_pdf.append(int(pages_group) if pages_group.isdigit() else 1)

    # Step 3: Open all PDFs
    pdfs = [fitz.open(path) for path in pdf_paths]
    
    # Step 4: Create a new PDF for the combined result
    output_pdf = fitz.open()

    # Step 5: Interleave pages from all PDFs with circles
    max_pages = max(pdf.page_count for pdf in pdfs)

    # Step 6: Define colors for the circles
    colors = [
        (1, 0, 0),   # Red
        (0, 0, 1),   # Blue
        (0, 1, 0),   # Green
        (1, 1, 0),   # Yellow
        (1, 0, 1),   # Magenta
        (0, 1, 1)    # Cyan
    ]

    # Step 7: Interleave pages from all PDFs with circles
    for page_num in range(max_pages):
        for i, (pdf, group_size) in enumerate(zip(pdfs, pages_per_pdf)):
            for j in range(group_size):
                if page_num * group_size + j < pdf.page_count:
                    # Insert the page from the current PDF
                    output_pdf.insert_pdf(pdf, from_page=page_num * group_size + j, to_page=page_num * group_size + j)
                    # Add a colored circle
                    page = output_pdf[-1]  # Get the last added page
                    draw_colored_circle(page, colors[i % len(colors)])  # Alternate through the colors

    # Step 8: Save the combined PDF output path
    output_file_name = "interleaved_output_with_circles.pdf"
    output_file_path = os.path.abspath(output_file_name)
    output_pdf.save(output_file_path)
    output_pdf.close()
    
    # Close the individual PDFs
    for pdf in pdfs:
        pdf.close()

    # Step 9: Print the absolute path of the combined output PDF
    print(f"PDFs have been successfully interleaved with colored circles. The combined file is saved at:\n{output_file_path}")

# Helper function to draw a small circle at the top-left corner of a PDF page
def draw_colored_circle(page, color):
    # Define circle position and size
    circle_center = (30, 30)  # Coordinates near the top-left corner
    circle_radius = 10        # Radius of the circle
    
    # Create a circle using the draw_circle method
    page.draw_circle(center=circle_center, radius=circle_radius, color=color, fill=color)


interleave_pdfs_with_grouped_pages()

##########################################################################

import fitz
import os

def combine_all_pdfs_in_directory(directory, output_filename):
    """
    Combine all PDF files in a given directory into a single PDF.

    Parameters:
        directory (str): The directory containing the PDF files to combine.
        output_filename (str): The name of the output combined PDF file.

    Returns:
        str: The full path to the combined PDF file.
    """
    # Ensure directory exists
    if not os.path.exists(directory):
        raise ValueError(f"The directory {directory} does not exist.")
    
    # Get a sorted list of all PDF files in the directory
    pdf_list = sorted([os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.pdf')])
    
    if not pdf_list:
        raise ValueError(f"No PDF files found in the directory {directory}.")
    
    # Full path for the output PDF
    output_pdf_path = os.path.join(directory, output_filename)
    
    # Create a new PDF document
    combined_pdf = fitz.open()
    
    # Iterate over each PDF in the list and add its pages to the combined PDF
    for pdf_file in pdf_list:
        with fitz.open(pdf_file) as pdf:
            for page_num in range(pdf.page_count):
                combined_pdf.insert_pdf(pdf, from_page=page_num, to_page=page_num)
    
    # Save the combined PDF
    combined_pdf.save(output_pdf_path)
    combined_pdf.close()
    
    print(f"Combined PDF saved as: {output_pdf_path}")
    return output_pdf_path

# Example usage:
directory_path = r'G:\全部PPT'
output_filename = 'combined_output.pdf'
combined_pdf_path = combine_all_pdfs_in_directory(directory_path, output_filename)





##########################################################################
