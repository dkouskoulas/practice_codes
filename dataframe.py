import pandas as pd
from datetime import datetime, timedelta

# Sample dictionary with dates for DataFrame
data = {
    'date': [
        '2024-01-01',
        '2024-01-02',
        '2024-01-03',
        '2024-01-04',
        '2024-01-05',
        '2024-01-06',
        '2024-01-07'
    ],
    'sales': [100, 150, 200, 175, 225, 300, 250],
    'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
    'quantity': [10, 15, 20, 12, 18, 25, 22]
}



df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])



# Create DataFrame
df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Examples of datetime operations:
print("DataFrame:")
print(df)
print("\n")

# Filter by date
print("Sales after 2024-01-03:")
print(df[df['date'] > '2024-01-03'])
print("\n")

# Extract date components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.day_name()

print("DataFrame with date components:")
print(df)
print("\n")

# Group by date
print("Total sales by date:")
print(df.groupby('date')['sales'].sum())