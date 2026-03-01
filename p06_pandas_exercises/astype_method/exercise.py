# Import the pandas library and assign it an alias of 'pd'.


# Import the health.csv file and assign it to a 'health' variable.
import pandas as pd

health = pd.read_csv("health.csv")
print(health.head())
# The resulting DataFrame will have 3 columns: Weight, Height, and Blood Type

# Convert the values in the Weight Series to strings and overwrite the original column
health["Weight"] = health["Weight"].astype("str")
print(health.head())

# Convert the values in the Height Series to integers and overwrite the original column
health["Height"] = health["Height"].fillna(0)
health["Height"] = health["Height"].astype("int")

# Convert the values in the Blood Type Series to categories and overwrite the original column
print("*" * 100)
health["Blood Type"] = health["Blood Type"].astype("category")
print(health.dtypes)
