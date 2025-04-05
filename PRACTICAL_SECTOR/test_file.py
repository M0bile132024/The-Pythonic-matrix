import matplotlib.pyplot as plt
import numpy as np

# Generate 500 random x, y points
np.random.seed(42)  # For reproducibility
x_points = np.random.uniform(0, 10, 500)
y_points = np.random.uniform(0, 10, 500)

# Display x, y points
plt.scatter(x_points, y_points, color='blue', label='Random Points')

# Define the line function f(x) = mx + c
def f(x, m=1, c=0):
    return m * x + c

# Generate the line based on the function
line_x = np.linspace(0, 10, 100)
line_y = f(line_x, m=2, c=3)  # Example line with slope 2 and intercept 3

# Display the line
plt.plot(line_x, line_y, color='red', label='Line f(x) = 2x + 3')

# Compute the desired answers (e.g., count of points above the line)
above_line = np.sum(y_points > f(x_points, m=2, c=3))

# Display the desired answers
plt.legend()
plt.title(f'Points Above Line: {above_line}')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

print(f'Number of points above the line: {above_line}')
