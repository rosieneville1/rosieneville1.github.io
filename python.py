import pandas as pd

# Load the data from the CSV file
url = "https://raw.githubusercontent.com/rosieneville1/rosieneville1.github.io/main/simpleETS2.csv"
df = pd.read_csv(url)

# Replace non-numeric emissions with 0 and convert columns to numeric
df['2021'] = pd.to_numeric(df['2021'].str.replace(',', '').str.strip(), errors='coerce').fillna(0)
df['2022'] = pd.to_numeric(df['2022'].str.replace(',', '').str.strip(), errors='coerce').fillna(0)
df['2023'] = pd.to_numeric(df['2023'].str.replace(',', '').str.strip(), errors='coerce').fillna(0)

# Group by 'Broad sector' and sum the emissions for each year
summed_df = df.groupby('Broad sector').agg({
    '2021': 'sum',
    '2022': 'sum',
    '2023': 'sum'
}).reset_index()

# Display the transformed DataFrame
print(summed_df)
