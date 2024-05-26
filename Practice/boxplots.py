import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_mila = pd.read_excel('/Users/admin/Downloads/Mila Trial 4.xlsx')
data_felix = pd.read_excel('/Users/admin/Downloads/Felix Trial 4.xlsx')
data_theo = pd.read_excel('/Users/admin/Downloads/Theo Trial 4.xlsx')

# Plotting for Participant 1 (Mila)
plt.figure(figsize=(12, 8))
data_mila.boxplot()
plt.title('Distribution of Marks for Participant 1')
plt.xlabel('Transcript Version')
plt.ylabel('Scores')
plt.xticks()
plt.savefig('Participant_1_Boxplot.png')
plt.show()

# Plotting for Participant 2 (Felix)
plt.figure(figsize=(12, 8))
data_felix.boxplot()
plt.title('Distribution of Marks for Participant 2')
plt.xlabel('Transcript Version')
plt.ylabel('Scores')
plt.xticks()
plt.savefig('Participant_2_Boxplot.png')
plt.show()

# Plotting for Participant 3 (Theo)
plt.figure(figsize=(12, 8))
data_theo.boxplot()
plt.title('Distribution of Marks for Participant 3')
plt.xlabel('Transcript Version')
plt.ylabel('Scores')
plt.xticks()
plt.savefig('Participant_3_Boxplot.png')
plt.show()
