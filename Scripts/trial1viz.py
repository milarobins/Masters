import matplotlib.pyplot as plt

# Raw data
participants = ['1', '2', '3', '4']
runs = {
    '1': [19, 17.5, 15, 16.5, 15, 18, 14.5, 19, 14, 16],
    '2': [16, 16.5, 18, 17.3, 15, 17.5, 17, 17, 19, 17],
    '3': [20, 20, 17.5, 19, 18, 19, 18, 18, 18, 18],
    '4': [17.5, 17, 15.5, 16, 16, 15, 17, 17.5, 17, 17.5]
}

# Calculate the average marks for each participant
averages = {participant: sum(marks) / len(marks) for participant, marks in runs.items()}

# Increase the font size globally
plt.rcParams.update({'font.size': 16})

# Plot scatter plot
plt.figure(figsize=(12, 8))
colors = ['#FF0000'] * 10  # Red color for all runs

for participant in participants:
    plt.scatter([participant] * 10, runs[participant], color=colors, alpha=0.6, label='Individual GPT runs' if participant == '1' else "")

# Plot the averages
for participant, avg in averages.items():
    plt.scatter(participant, avg, color='#0000FF', edgecolor='black', s=100, zorder=5, marker='s', alpha=0.6, label='Average' if participant == '1' else "")

plt.xlabel('Participant')
plt.ylabel('Mark')
plt.legend()
plt.show()