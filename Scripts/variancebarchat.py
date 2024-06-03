import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame with the provided data
data = {
    "Participant": list(range(1, 18)),
    "Human Variance": [25.750, 1.583, 11.083, 14.083, 11.083, 2.583, 18.750,
                       3.250, 4.333, 18.583, 1.083, 2.583, 11.083, 10.750,
                       7.750, 0.583, 4.333],
    "GPT Variance": [0.000, 0.333, 0.583, 0.250, 0.083, 0.750, 3.000,
                     0.000, 0.583, 1.000, 0.333, 0.333, 0.250, 0.083,
                     0.333, 0.000, 1.333]
}

df = pd.DataFrame(data)

# Set global font size to 18
plt.rcParams.update({'font.size': 18})

# Plotting the variances
plt.figure(figsize=(12, 6))
x = range(len(df['Participant']))
plt.bar(x, df['Human Variance'], width=0.4, label='Human', color='#3498db', align='center')
plt.bar(x, df['GPT Variance'], width=0.4, label='GPT', color='#e74c3c', align='edge')
plt.xlabel('Participant No')
plt.ylabel('Variance (s^2)')
plt.title('Variance in Examiners (Average)')
plt.xticks(x, df['Participant'])
plt.legend()
plt.tight_layout()
plt.show()