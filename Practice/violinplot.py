import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Participant': list(range(1, 18)),
    'Human Examiner Avg': [12.500, 18.833, 15.167, 15.333, 17.333, 13.833, 12.000, 14.000, 15.667, 6.833, 5.833, 16.833, 14.333, 8.500, 13.000, 17.667, 16.333],
    'GPT Avg': [15.333, 16.333, 14.333, 14.000, 16.500, 15.167, 15.167, 16.000, 15.833, 11.667, 9.333, 18.500, 15.333, 11.167, 16.667, 19.667, 15.500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Reshape the DataFrame to long format
df_long = pd.melt(df, id_vars=['Participant'], value_vars=['Human Examiner Avg', 'GPT Avg'],
                  var_name='Examiner', value_name='Scores')

# Create a violin plot
sns.violinplot(x='Examiner', y='Scores', data=df_long)
plt.title('Score Distribution Comparison Between Human Examiners and GPT')
plt.show()
