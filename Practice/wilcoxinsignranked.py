from scipy.stats import shapiro
import pandas as pd

# Load the data from the uploaded Excel file
file_path = '/mnt/data/edited vs unedited trial 2.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head(), data.columns

# Prepare data for normality testing
columns = ['GPT Run 1', 'GPT Run 2', 'GPT Run 3', 'Unedited GPT Run 1', 'Unedited GPT Run 2', 'Unedited GPT Run 3']
normality_results = {}

# Conduct Shapiro-Wilk test for normality
for col in columns:
    stat, p_value = shapiro(data[col])
    normality_results[col] = {'Statistic': stat, 'p-value': p_value}

pd.DataFrame(normality_results).T

from scipy.stats import wilcoxon

# Data preparation for comparisons (excluding Question 4)
questions_to_compare = [1, 2, 3, 5]

# Run Wilcoxon signed-rank tests for each question for each of the runs
wilcoxon_results = {}
for q in questions_to_compare:
    q_data = data[data['Question'] == q]
    for i in range(1, 4):
        edited_score = q_data[f'GPT Run {i}']
        unedited_score = q_data[f'Unedited GPT Run {i}']
        stat, p_value = wilcoxon(edited_score, unedited_score)
        wilcoxon_results[f'Question {q} - Run {i}'] = {'Statistic': stat, 'p-value': p_value}

pd.DataFrame(wilcoxon_results).T
