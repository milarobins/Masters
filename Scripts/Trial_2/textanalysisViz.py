import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Load the results from the CSV file
results_path = '' # Insert file path to CSV where results have been stored
visualization_df = pd.read_csv(results_path, index_col=0).transpose()
#print(visualization_df.columns)

# Heat Map - Correlation Matrix
plt.figure(figsize=(12, 10))
sns.heatmap(visualization_df.corr(), annot=True, cmap='coolwarm',annot_kws={"size": 10})
plt.title('Correlation Matrix of Metrics')
plt.xticks(fontsize=8)  # Reduce x-axis label font size
plt.yticks(fontsize=8)  # Reduce y-axis label font size
plt.show()