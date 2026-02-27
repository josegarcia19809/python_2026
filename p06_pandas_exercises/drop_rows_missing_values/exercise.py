# The data.csv file contains a dataset of random numbers.
# The dataset has 4 columns: A, B, C, and D.
# Import pandas and use it to parse the CSV.
# Assign the imported DataFrame to a variable called 'data'.
import pandas as pd

data = pd.read_csv("data.csv")
print(data.head(30))
print("*"*100)

# Filter the dataset to remove rows where ALL the
# values are missing. Assign the resulting DataFrame
# to a "no_empty_rows" variable.
no_empty_rows = data.dropna(how="all")
print(no_empty_rows.head(30))
print("*"*100)

# Filter the dataset to remove rows that have a missing value
# in either the "B" or "D" columns.
# Assign the resulting DataFrame to a "result" variable.
result = data.dropna(subset=["B", "D"])
print(result.head(30))
