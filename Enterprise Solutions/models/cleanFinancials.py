import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
excel_file = 'Financials.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Extract the relevant data columns
income_data = df[['Income', 'Total']]
expenses_data = df[['Expenses', 'Total']]
net_income_data = df[['Net Income', 'Total']]

# Calculate the total income, total expenses, and net income
total_income = income_data['Total'].sum()
total_expenses = expenses_data['Total'].sum()
net_income = net_income_data['Total'].sum()

# Extract month-wise data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
monthly_income = [income_data['Total'][i] for i in range(len(months))]
monthly_expenses = [expenses_data['Total'][i] for i in range(len(months))]
monthly_net_income = [net_income_data['Total'][i] for i in range(len(months))]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(months, monthly_income, label='Income', color='blue', alpha=0.7)
plt.bar(months, monthly_expenses, label='Expenses', color='red', alpha=0.7)
plt.bar(months, monthly_net_income, label='Net Income', color='green', alpha=0.7)

plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Income, Expenses, and Net Income by Month')
plt.legend()

# Show the graph
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
