import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load data from the Excel file
excel_file = pd.ExcelFile('RVMP Financials Sep 14 2023.xlsx')  # Replace with your file name
sheet_name = 'Sheet1'  # Replace with your sheet name

# Load the specific cell range (B10:AT10) from the Excel sheet
df = excel_file.parse(sheet_name, header=None, usecols="B10:AT10")

# Transpose the DataFrame to have months as rows and sales as columns
df = df.T
df.columns = ['Sales']

# Create a month column from 1 to the number of data points
df['Month'] = np.arange(1, len(df) + 1)

# Split the data into features (X) and target variable (y)
X = df[['Month']]
y = df['Sales']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions for the next month
next_month = np.array([[len(df) + 1]])  # Predict for the next month
next_month_sales = model.predict(next_month)

print(f"Predicted sales for the next month: {next_month_sales[0]:.2f}")

# Evaluate the model (optional)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Plot the results (optional)
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Prediction')
plt.show()
