import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
df = pd.read_excel('/Users/admin/Desktop/Masters/Trial 2 Oral Exams/feedback id.xlsx')

# Prepare data for visualization
# Sum correct and incorrect identifications for human and GPT-generated feedback
correct_human = df['Feedback generated by human'].sum()
incorrect_human = len(df['Feedback generated by human']) - correct_human
correct_gpt = df['Feedback generated by GPT'].sum()
incorrect_gpt = len(df['Feedback generated by GPT']) - correct_gpt

# Create DataFrame for plotting
data = {
    'Correct ID': [correct_human, correct_gpt],
    'Incorrect ID': [incorrect_human, incorrect_gpt]
}
plot_df = pd.DataFrame(data, index=['Human', 'GPT'])

# Set the seaborn style for better aesthetics
sns.set(style="whitegrid")

# Create a figure with specified size to adjust bulkiness and maintain consistency with the histogram
plt.figure(figsize=(8, 6))

# Plotting the stacked bar chart with matching colors
plot_df.plot(kind='bar', stacked=True, color=['#3498db', '#e74c3c'], width=0.6)  # Adjusted width for bars
plt.title('Correct vs Incorrect Feedback Generator ID')
plt.xlabel('Feedback Generator')
plt.ylabel('Number of IDs')
plt.xticks(rotation=0)  # Keep the labels horizontal for better readability

# Adjust the legend to prevent overlap with the graph
plt.legend(title='ID Accuracy', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to fit everything nicely
plt.tight_layout()

# Show the plot
plt.show()