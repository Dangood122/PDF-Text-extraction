import os
import fitz  # PyMuPDF

#PDF text extractor is a free program created by Dan Good. You are free to use this program for whatever NON-COMMERCIAL purpose you wish#
#Never pay for what you can do yourself for free!#
#PDF Text extractor is a simple tool that uses PyMuPDF to extract text from a PDF and outputs it into a text file. It is as simple as it gets, but it works #

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        total_pages = pdf_document.page_count

        for page_number in range(total_pages):
            page = pdf_document[page_number]
            text += page.get_text("text")

    return text

def main(file_path):
    extracted_text = extract_text_from_pdf(file_path)
    
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    directory = os.path.dirname(file_path)
    counter = 0  # Initialize counter for file name checks

    # Generate initial output file name
    output_file = os.path.join(directory, f"{base_name}.txt")
    
    # Check if the file already exists
    while os.path.exists(output_file):
        counter += 1
        new_output_file = os.path.join(directory, f"{base_name}({counter}).txt")
        print(f"Output file {output_file} already exists, saving as {new_output_file}")
        output_file = new_output_file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(extracted_text)
    
    print(f"Conversion successful, please see {output_file} for your raw text.")

print("Welcome to the PDF text extractor tool - v0.1  ------- Created by: Dan Good")
if __name__ == "__main__":
    print("Please provide path to PDF. This can be found by right clicking the document and copying the location and file name.")
    file_path = input("File path: ")
    main(file_path)
