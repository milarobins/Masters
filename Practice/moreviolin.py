import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('/Users/admin/Downloads/Trial II.xlsx')

# Assuming 'df' is your DataFrame with the proper data
# Set up the figure
plt.figure(figsize=(12, 10))

# List of examiners and GPTs for plotting
score_columns = ['Human 1', 'Human 2', 'Human 3', 'GPT 1', 'GPT 2', 'GPT 3']

# Plotting
for i, question in enumerate([1, 2, 3, 5], 1):
    plt.subplot(2, 2, i)
    sns.violinplot(data=df[df['Question'] == question][score_columns])
    plt.title(f'Mark Distribution for Question {question}', fontsize=11)
    plt.ylabel('Marks', fontsize=10)
    plt.xlabel('Examiner', fontsize=10)

plt.tight_layout()
plt.show()
