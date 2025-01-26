import numpy as np
import matplotlib.pyplot as plt

def get_houses_data():
    # Set the random seed for reproducibility
    np.random.seed(42)

    # Generate a discrete feature for the number of bedrooms (1 to 5)
    bedrooms = np.random.randint(1, 6, size=100)

    # Generate a continuous feature for the area in thousands of square feet (0.6 to 3.0)
    square_feet = 0.6 + 2.4 * np.random.rand(100)

    # Generate the age of the houses (0 to 50 years)
    age = np.random.randint(0, 51, size=100)

    # Create a linear relationship for the labels (house price) in dollars
    # Base price starts at $100,000
    # Bedrooms add $30,000 each
    # Area adds $150 per square foot
    # Age decreases value by $1,000 per year
    price = (
        100000
        + 30000 * bedrooms
        + 150 * square_feet * 1000  # Price in dollars based on area
        - 1000 * age               # Deduct $1,000 per year of age
        + np.random.normal(scale=5000, size=100)  # Reduced random noise for realism
    )

    # Remove outliers by limiting price values
    price = np.clip(price, a_min=None, a_max=800000)  # Clip to avoid extreme values

    return (bedrooms, square_feet, age, price)

def plot_results(df):
  # Plot setup
  plt.figure(figsize=(12, 8))

  # Scatter plot for Expected and Predicted Prices
  plt.scatter(df.index, df["Expected Price"], color='blue', label='Expected Price', alpha=0.7, s=80)
  plt.scatter(df.index, df["Predicted Price"], color='orange', label='Predicted Price', alpha=0.7, s=80)

  # Add lines connecting the points for clarity
  for i in range(len(df)):
    plt.plot(
        [df.index[i], df.index[i]],
        [df["Expected Price"][i], df["Predicted Price"][i]],
        color='gray', linestyle='--', alpha=0.5
    )

  # Add labels, legend, and title
  plt.xlabel('Listings', fontsize=14)
  plt.ylabel('Price (in $)', fontsize=14)
  plt.title('Comparison of Expected vs Predicted Prices', fontsize=16)
  plt.xticks(df.index, [f'House Listing {i + 1}' for i in df.index], rotation=45)
  plt.legend()
  plt.grid(alpha=0.3)

  # Show the plot
  plt.tight_layout()
  plt.show()