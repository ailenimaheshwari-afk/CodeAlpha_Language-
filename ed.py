
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [80, 90, 70, 60, 100],
    'Age': [20, 21, 19, 20, 22]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Display information
print("\nData Information:")
print(df.info())

# Calculate statistics
print("\nStatistical Summary:")
print(df.describe())

# Find average marks
print("\nAverage Marks:", df['Marks'].mean())

# Draw a graph
df['Marks'].plot(kind='bar')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
