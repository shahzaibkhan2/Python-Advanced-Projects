# Import numpy
import numpy as np

# Function to calculate statistics
def calculate_statistics(data):
    # Standard Deviation
    std_dev = np.std(data)

    # Variance
    variance = np.var(data)

    # Maximum
    maximum = np.max(data)

    # Minimum
    minimum = np.min(data)

    # Interquartile Range
    q75, q25 = np.percentile(data, [75 ,25])
    iqr = q75 - q25

    # Percentiles
    percentiles = np.percentile(data, [10, 25, 50, 75, 90])

    return std_dev, variance, maximum, minimum, iqr, percentiles

# Example for usage
dataset = [5, 11, 12, 10, 14, 16, 21, 22, 24, 31]

std_dev, variance, maximum, minimum, iqr, percentiles = calculate_statistics(dataset)

print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Interquartile Range:", iqr)
print("Percentiles:", percentiles)
