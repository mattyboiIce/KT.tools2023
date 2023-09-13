import pandas as pd
import openpyxl

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file_path = 'Spendlove Budget 2.xlsx'

# List of sheet names you want to process (add or remove sheet names as needed)
sheet_names_to_process = [
    'Chase June', 'Chase May', 'Chase July', 'Chase Aug'  # Replace with your sheet names
]

# Define a function to classify transactions based on their description
def classify_transaction(transaction):
    keywords = {
        'Entertainment': ['movie', 'concert', 'theater', 'amusement park', 'spotify', 'netflix', 'hulu'],
        'Eating Out': ['restaurant', 'cafe', 'fast food', 'taco bell', 'qdoba'],
        'Groceries': ['grocery', 'supermarket', 'walmart', "lowe's", 'home depot', 'fred meyer', 'safeway', 'yoke\'s fresh market','target'],
        'Gas': ['gas station', 'shell oil', 'conoco'],
        'Travel': ['flight', 'hotel', 'travel agency', 'car rental', 'expedia', 'delta', 'united airlines', 'spirit', 'viator'],
        'Vehicles': ['car repair', 'auto parts', 'blue dolphin car wash', 'autozone'],
        'Rent & Utilities': ['rent', 'utilities', 'waste mgmt'],
        'Mortgage': ['mortgage', 'chase'],
        'Payment': ['payment', 'paypal'],
        'Fees': ['interest'],
        'Online Shopping': ['asos.com', 'etsy.com', 'bestbuycom', 'microsoft*xbox', 'pandora', 'walmart.com', 'costco by instacart'],
        'Health & Fitness': ['peter attia', 'unchained wellness', 'empowered health', 'all american gymnastics', 'pp*seahawks flag football', 'pp*ov hair', 'pp*consumrrpts', 'pp*betterme', 'smile surfers kids dentis'],
        'Tech & Electronics': ['apple.com/bill', 'amzn mktp us', 'prime video', 'nintendo', 'samsung electronics', 'oculus', 'canva* i03841-22773252 httpscanva.co de'],
        'Other': ['spectrum', 'supra re', 'square', 'paramount theatre', 'crush it app leatherhead', 'allianz travel ins', 'talkspace', 'galaxy game room lincoln city or', 'utah valley home builders 801-2258893 ut', 'chevron 0207761 newberg or', 'rite aid 05371 lincoln city or', 'circle k # 06031 kennewick wa', 'k krates llc 727-2646546 fl', 'asos.com asos.com ga'],
        'Amazon': ['amazon','amzn'], }

    for category, category_keywords in keywords.items():
        for keyword in category_keywords:
            if keyword in str(transaction).lower():  # Use str() to handle potential non-string values
                return category
    return 'Other'

# Load the Excel file and create a Pandas Excel writer
with pd.ExcelFile(excel_file_path) as xls:
    # Create an Excel writer
    output_file_path = f'{excel_file_path.split(".")[0]}_CLEAN.xlsx'
    writer = pd.ExcelWriter(output_file_path, engine='openpyxl')

    # Iterate through the sheets you want to process
    for sheet_name in sheet_names_to_process:
        # Read data from the current sheet into a DataFrame
        data = pd.read_excel(xls, sheet_name=sheet_name)

        # Apply the classification function to add a 'DESCRIPTION' column with classification
        data['DESCRIPTION'] = data['TRANSACTION'].apply(classify_transaction)

        # Save the updated DataFrame to the output Excel file
        data.to_excel(writer, sheet_name=sheet_name, index=False)

    # Save the Excel writer to the output file
    writer._save()

print(f"Classification complete. Results saved to {output_file_path}")
