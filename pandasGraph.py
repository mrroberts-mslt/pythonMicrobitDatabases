import pandas as pd
import matplotlib.pyplot as plt

# Reading the updated CSV file into a pandas DataFrame
file_path_updated = 'huw.csv'  # Adjust the path to your updated CSV file
df_updated = pd.read_csv(file_path_updated)

# Renaming the columns for clarity
df_updated.columns = ['Seat Pressure', 'Light', 'Temperature']

# Plotting each of the three columns
plt.figure(figsize=(12, 6))

# Plot each column
for column in df_updated.columns:
    plt.plot(df_updated.index, df_updated[column], label=column)

plt.title('Graph of the 3 Columns from microbit data csv')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

