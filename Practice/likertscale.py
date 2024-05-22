import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
df = pd.read_excel('/Users/admin/Desktop/Masters/Trial 2 Oral Exams/Likert only.xlsx')
#print(df.head())

# Initialize lists to store the feedback ratings
human_ratings = []
gpt_ratings = []

# Aggregate ratings for human and GPT from each relevant column
for col in df.columns:
    if "human" in col:
        human_ratings.extend(df[col].dropna().tolist())
    elif "GPT" in col:
        gpt_ratings.extend(df[col].dropna().tolist())

# Prepare DataFrame for plotting
ratings_data = pd.DataFrame({
    'Rating': human_ratings + gpt_ratings,
    'Type': ['Human'] * len(human_ratings) + ['GPT'] * len(gpt_ratings)
})

# Set the style of seaborn for better aesthetics
sns.set(style="whitegrid")

# Create a figure with specified size to adjust bulkiness
plt.figure(figsize=(8, 6))  # Smaller and more proportional

# Create a count plot to show the data side-by-side
ax = sns.countplot(x='Rating', hue='Type', data=ratings_data, palette=['#3498db', '#e74c3c'])

# Adding title and labels
plt.title('Distribution of Usefulness Ratings for Human vs GPT Feedback')
plt.xlabel('Likert Scale Rating')
plt.ylabel('Frequency')
plt.xticks(range(0, 5), labels=['1: Not useful at all', '2', '3', '4', '5: Very useful'])  # Custom labels for Likert scale

# Add a legend to the plot to identify the histograms
plt.legend(title='Feedback Type')

# Show the plot
plt.tight_layout()
plt.show()