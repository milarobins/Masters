import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel('/Users/admin/Desktop/Masters/Trial 2 Oral Exams/feedback id copy.xlsx')

# Columns for each question and feedback type
questions = ['Q1', 'Q2', 'Q3', 'Q5']
feedback_types = ['Human', 'GPT']

# Prepare data for visualization
data = []

# Collect data for each question and feedback type
for question in questions:
    for feedback_type in feedback_types:
        correct_column = f'{question} {feedback_type}'
        if correct_column in df.columns:
            correct_count = df[correct_column].sum()
            incorrect_count = df[correct_column].count() - correct_count  # Calculate incorrect identifications
            data.append({'Question': question, 'Feedback Type': feedback_type, 'Identification': 'Correct', 'Count': correct_count})
            data.append({'Question': question, 'Feedback Type': feedback_type, 'Identification': 'Incorrect', 'Count': incorrect_count})

# Convert to DataFrame
plot_df = pd.DataFrame(data)

# Summarize data for overall correct vs. incorrect for simplicity
summary_df = plot_df.groupby(['Feedback Type', 'Identification']).sum().reset_index()

# Plotting
plt.figure(figsize=(8, 6))
sns.barplot(x='Feedback Type', y='Count', hue='Identification', data=summary_df, palette=['#3498db', '#e74c3c'])
plt.title('Overall Correct vs Incorrect Feedback Generator Identification')
plt.xlabel('Feedback Type')
plt.ylabel('Total Identifications')
plt.legend(title='Identification Accuracy')
plt.tight_layout()
plt.show()
