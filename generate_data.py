import pandas as pd
import numpy as np
import random
import sys

# Check if a file name argument is passed
if len(sys.argv) < 2:
    print("Usage: python generate_data.py <output_file_name.csv> [num_of_rows]")
    sys.exit(1)

# Function to parse command line arguments
def parse_arguments():
    output_file = "generated_data.csv"  # Default file name
    num_rows = 1000  # Default number of rows
    
    # Check if any arguments are passed
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    if len(sys.argv) > 2:
        try:
            num_rows = int(sys.argv[2])
        except ValueError:
            print("Error: The number of rows must be an integer.")
            sys.exit(1)

    return output_file, num_rows

# Get the output file name and number of rows from command-line arguments
output_file, num_rows = parse_arguments()

# Set a random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate random feature1 and feature2
feature1 = np.random.rand(num_rows) * 100  # Random floats between 0 and 100
feature2 = np.random.rand(num_rows) * 100  # Random floats between 0 and 100

# Generate labels based on some logic
# For simplicity, let's say if feature1 + feature2 > 100, label is 1, otherwise 0
labels = [1 if f1 + f2 > 100 else 0 for f1, f2 in zip(feature1, feature2)]

# Create a DataFrame
data = pd.DataFrame({
    'feature1': feature1,
    'feature2': feature2,
    'label': labels
})

# Save to the specified CSV file
data.to_csv(output_file, index=False)

print(f"Dataset with {num_rows} rows generated and saved as '{output_file}'")
