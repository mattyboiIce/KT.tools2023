# Packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import openai  # Import the openai package

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your API key

# Load data from the Excel file
excel_file = pd.ExcelFile('RVMP Financials Sep 14 2023.xlsx')  # Replace with your file name
sheet_name = 'Profit and Loss'  # Replace with your sheet name

# Load the specific cell range (B10:AT10) from the Excel sheet
df = excel_file.parse(sheet_name, header=None, usecols="B:AT", skiprows=9, nrows=1)

# Transpose the DataFrame to have months as rows and sales as columns
df = df.T
df.columns = ['Sales']

# Create a month column from 1 to the number of data points
df['Month'] = np.arange(1, len(df) + 1)

# Split the data into features (X) and target variable (y)
X = df[['Month']]
y = df['Sales']

# Create a list to store sales predictions for multiple trials
trial_predictions = []

# Number of trials
num_trials = 1000

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)  # Use all available data for training

# Simulate sales predictions for the next 12 months for each trial
for _ in range(num_trials):
    trial_sales = []
    for month in range(len(df) + 1, len(df) + 13):
        # Predict sales for the next month
        next_month = np.array([[month]])
        next_month_sales = model.predict(next_month)[0]
        
        # Generate justification text (you may want to limit API requests for large trials)
        justification = "Your justification text here"  # Replace with actual justification
        
        # Append the prediction and justification to the list
        trial_sales.append((next_month_sales, justification))
    
    trial_predictions.append(trial_sales)

# Rest of your code for saving justifications and plotting results (not provided in the snippet)

# Visualize the results using matplotlib (add your code for plotting here)


# Save the justifications to a text file
with open('justification.txt', 'w') as justification_file:
    for trial in trial_predictions:
        for prediction, justification in trial:
            justification_file.write(f"Predicted Sales: {prediction:.2f}\n")
            justification_file.write(f"Justification: {justification}\n\n")

# Rest of the code for plotting the results (same as previous code)

# Load data from the Excel file
excel_file = pd.ExcelFile('RVMP Financials Sep 14 2023.xlsx')  # Replace with your file name
sheet_name = 'Profit and Loss'  # Replace with your sheet name

# Load the specific cell range (B10:AT10) from the Excel sheet
df = excel_file.parse(sheet_name, header=None, usecols="B:AT", skiprows=9, nrows=1)

# Transpose the DataFrame to have months as rows and sales as columns
df = df.T
df.columns = ['Sales']

# Create a month column from 1 to the number of data points
df['Month'] = np.arange(1, len(df) + 1)

# Split the data into features (X) and target variable (y)
X = df[['Month']]
y = df['Sales']

# Create a list to store sales predictions for multiple trials
trial_predictions = []

# Number of trials
num_trials = 1000

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)  # Use all available data for training

# Simulate sales predictions for the next 12 months for each trial
for _ in range(num_trials):
    trial_sales = []
    for month in range(len(df) + 1, len(df) + 13):
        # Predict sales for the next month
        next_month = np.array([[month]])
        next_month_sales = model.predict(next_month)[0]
        
        # Introduce random noise (you can adjust the scale as needed)
        noise = np.random.normal(0, 10)  # Adjust the standard deviation (10 in this case)
        trial_sales.append(next_month_sales + noise)
    
    trial_predictions.append(trial_sales)

# Plot the actual sales and trial predictions
plt.figure(figsize=(12, 6))
plt.plot(df['Month'], y, label='Actual Sales', color='black')

for trial_sales in trial_predictions:
    plt.scatter(range(len(df) + 1, len(df) + 13), trial_sales, marker='.', alpha=0.2, color='blue')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Actual Sales and Predictions for Next 12 Months (1000 Trials)')
plt.legend()
plt.show()
