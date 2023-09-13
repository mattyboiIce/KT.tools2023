import os
import fitz  # PyMuPDF
#Naming the new file
fileName = "Craig and Trena Adams Report 9-12-2023"
#input("Enter Combined pdf File Name: ")
def combine_pdfs(input_directory, output_filename):
    # Create a PDF document
    pdf_document = fitz.open()
    
    # Get a list of PDF files in the input directory
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith(".pdf")]
    
    # Create lists to hold PDFs for each section
    cover_pdfs = []
    mo_pdfs = []
    inv_pdfs = []
    disclosures_pdfs = []
    
    # Define indicator words for each section
    indicator_words = {
        "cover": "cover",
        "mo": "mo",
        "inv": "inv",
        "disclosures": "disclosures"
    }
    
    # Iterate through the PDF files and categorize them
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(input_directory, pdf_file)
        try:
            # Check for indicator words in a case-insensitive manner
            for section, indicator in indicator_words.items():
                if indicator.lower() in pdf_file.lower():
                    if section == "cover":
                        cover_pdfs.append(pdf_file_path)
                    elif section == "mo":
                        mo_pdfs.append(pdf_file_path)
                    elif section == "inv":
                        inv_pdfs.append(pdf_file_path)
                    elif section == "disclosures":
                        disclosures_pdfs.append(pdf_file_path)
        except Exception as e:
            print(f"Skipping PDF file due to error: {pdf_file} - {str(e)}")
    
    # Append PDFs in the specified order
    for pdf_file in cover_pdfs:
        pdf_document.insert_pdf(fitz.open(pdf_file), start_at=0)
    
    for pdf_file in mo_pdfs:
        pdf_document.insert_pdf(fitz.open(pdf_file))
    
    for pdf_file in inv_pdfs:
        pdf_document.insert_pdf(fitz.open(pdf_file))
    
    for pdf_file in disclosures_pdfs:
        pdf_document.insert_pdf(fitz.open(pdf_file))
    
    # Save the combined PDF to the output file
    output_pdf_path = os.path.join(input_directory, output_filename)
    pdf_document.save(output_pdf_path)
    
    print(f"{fileName} PDF created at: {output_pdf_path}")

# Input directory where the PDF files are located
input_directory = os.path.expanduser("~/Library/CloudStorage/OneDrive-KeelerThomasManagement/KT Tools/billing report tool")

'''/Users/matthewmarshall/Library/CloudStora
ge/OneDrive-KeelerThomasManagement/KT Tools/billing report tool
#downloads path works
input_directory = os.path.expanduser("~/Downloads/billing report tool")
'''
# Output PDF file name

output_pdf = (f"{fileName}.pdf")
# Call the function to combine PDFs based on file names
combine_pdfs(input_directory, output_pdf)
