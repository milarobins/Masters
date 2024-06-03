import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataframe based on the provided data
data = {
    "Student": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "GPT": [12, 25.33, 16.33, 14.17, 18.08, 21.67, 25, 21.17, 24.75],
    "Human": [16.5, 35, 18.5, 18.5, 20, 25, 32, 32, 35]
}

df = pd.DataFrame(data)

plt.rcParams.update({'font.size': 14}) # set global font size to 14

# Kernel Density Estimation (KDE) Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(df['GPT'], shade=True, label='GPT', color='blue')
sns.kdeplot(df['Human'], shade=True, label='Human', color='green')
plt.title('KDE Plot of GPT and Human Marks')
plt.xlabel('Marks')
plt.ylabel('Density')
plt.legend()
plt.show()