import numpy as np
from sklearn.linear_model import LinearRegression

# Define your input sequence and target values (the next numbers in the sequence).
# You can replace this data with your own sequence and targets.
sequence = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
targets = np.array([6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# Reshape the sequence to be a 2D array (required for scikit-l∏earn).
sequence = sequence.reshape(-1, 1)

# Initialize and train a linear regression model.
model = LinearRegression()
model.fit(sequence, targets)

# Predict the next number in the sequence.
next_number = model.predict(np.array([[11]]))  # Predict for the next number after 10.

print("Predicted next number:", next_number[0])
