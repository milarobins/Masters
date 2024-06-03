import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data from the image
data = {
    'Dataset1': [11, 10.5, 12.5, 17, 12, 13, 12, 10.5, 12, 11, 13.5, 9],
    'Dataset2': [16, 13.5, 15, 10.5, 11.5, 8, 11, 10, 7, 21.5, 11, 20]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set global font size to 14
plt.rcParams.update({'font.size': 20})

# Set the seaborn style for better aesthetics
sns.set(style="whitegrid")

# Create a figure with specified size
plt.figure(figsize=(10, 6))

# Plotting the distribution of both datasets using KDE
sns.kdeplot(df['Dataset1'], shade=True, label='Original', color='blue')
sns.kdeplot(df['Dataset2'], shade=True, label='Language Consideration', color='green')

# Adding title and labels
plt.xlabel('Value')
plt.ylabel('Density')

# Add a legend to the plot
plt.legend()

# Remove grid lines from the plot
plt.grid(False)

# Show the plot
plt.tight_layout()
plt.show()
