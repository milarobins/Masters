import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_mila = pd.read_excel('/Users/admin/Downloads/Mila Trial 4.xlsx')
data_felix = pd.read_excel('/Users/admin/Downloads/Felix Trial 4.xlsx')
data_theo = pd.read_excel('/Users/admin/Downloads/Theo Trial 4.xlsx')
data_arturo = pd.read_excel('/Users/admin/Downloads/Arturo Trial 4.xlsx')

# Determine the y-axis limits based on the data range across all datasets
all_data = pd.concat([data_mila, data_felix, data_theo, data_arturo])
y_min, y_max = all_data.min().min(), all_data.max().max()

# Set the font size globally
plt.rcParams.update({'font.size': 14})

# Plotting for Participant 1 (Mila)
plt.figure(figsize=(12, 8))
data_mila.boxplot()
plt.title('Participant 1', fontsize=20)
plt.xlabel('Transcript Modification', fontsize=16)
plt.ylabel('Marks', fontsize=16)
plt.ylim(y_min, y_max)
plt.grid(False)  # Remove grid lines
plt.savefig('Participant_1_Boxplot.png')
plt.show()

# Plotting for Participant 2 (Felix)
plt.figure(figsize=(12, 8))
data_felix.boxplot()
plt.title('Participant 2', fontsize=20)
plt.xlabel('Transcript Modification', fontsize=16)
plt.ylabel('Marks', fontsize=16)
plt.ylim(y_min, y_max)
plt.grid(False)  # Remove grid lines
plt.savefig('Participant_2_Boxplot.png')
plt.show()

# Plotting for Participant 3 (Theo)
plt.figure(figsize=(12, 8))
data_theo.boxplot()
plt.title('Participant 3', fontsize=20)
plt.xlabel('Transcript Modification', fontsize=16)
plt.ylabel('Marks', fontsize=16)
plt.ylim(y_min, y_max)
plt.grid(False)  # Remove grid lines
plt.savefig('Participant_3_Boxplot.png')
plt.show()

# Plotting for Participant 4 (Arturo)
plt.figure(figsize=(12, 8))
data_arturo.boxplot()
plt.title('Participant 4', fontsize=20)
plt.xlabel('Transcript Modification', fontsize=16)
plt.ylabel('Marks', fontsize=16)
plt.ylim(y_min, y_max)
plt.grid(False)  # Remove grid lines
plt.savefig('Participant_4_Boxplot.png')
plt.show()
