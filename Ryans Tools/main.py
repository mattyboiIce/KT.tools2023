import os
import openpyxl
from PyPDF2 import PdfFileReader

# Define the folder containing PDF files and the Excel file
pdf_folder = "path/to/pdf_folder"
excel_file = "output.xlsx"

# Initialize an Excel workbook
if not os.path.exists(excel_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Customer Data"
    # Add headers
    sheet.append(["Name", "Email", "Phone"])
else:
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

# Function to extract customer data from a PDF file
def extract_customer_data(pdf_file):
    customer_data = {}
    try:
        pdf_reader = PdfFileReader(open(pdf_file, "rb"))
        page = pdf_reader.getPage(0)  # Assuming customer data is on the first page
        text = page.extract_text()
        # Modify this part to extract customer data from the text as needed
        customer_data["Name"] = "John Doe"
        customer_data["Email"] = "john.doe@example.com"
        customer_data["Phone"] = "123-456-7890"
    except Exception as e:
        print(f"Error extracting data from {pdf_file}: {str(e)}")
    return customer_data

# Iterate through PDF files in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        customer_info = extract_customer_data(pdf_path)
        if customer_info:
            # Append customer data to the Excel sheet
            sheet.append([customer_info["Name"], customer_info["Email"], customer_info["Phone"]])

# Save the updated Excel file
workbook.save(excel_file)
