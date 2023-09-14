import numpy as np
import matplotlib.pyplot as plt

# Momentum oscillator threshold
threshold = 0.5

# Variables
x = []
y = []
consecutive_below_75 = 0

# Generate random data points
while len(x) < 150:
    random_num = np.random.randint(1, 150)
    
    # Check if the random number is above 75
    if random_num > 75:
        x.append(random_num)
        consecutive_below_75 = 0
    else:
        x.append(random_num)
        consecutive_below_75 += 1
        if consecutive_below_75 >= 5:
            x[-5:] = [75] * 5
            consecutive_below_75 = 0

# Calculate the momentum oscillator value for each data point
for num in x:
    if num > threshold:
        y.append("Trending Up")
    else:
        y.append("Trending Down")

# Create a scatter plot summary
plt.figure(figsize=(8, 6))
plt.scatter(range(len(x)), x, c='b', marker='o', label='Data Points')
plt.axhline(y=75, color='r', linestyle='--', label='Threshold (75)')
plt.xlabel('Data Point Index')
plt.ylabel('Value')
plt.title('Momentum Oscillator Summary')
plt.legend()
plt.grid(True)
plt.show()
