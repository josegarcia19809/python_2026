import pandas as pd

# This challenge includes a s&p500.csv with 6 columns:
# Symbol, Security, Sector, Industry, HQ, Founded
# Import the s&p500.csv DataFrame and assign it to
# a companies variable.

companies = pd.read_csv("s&p500.csv")

# Sort the DataFrame by the values in the "Industry" column in ascending order
# Assign the new DataFrame to a "by_industry" variable.
by_industry = companies.sort_values("Industry")
print(by_industry["Industry"])
print()
# Sort the DataFrame by the values in the "HQ" column in descending order
# Assign the new DataFrame to a "by_headquarters_descending" variable.
by_headquarters_descending = companies.sort_values("HQ", ascending=False)
print(by_headquarters_descending["HQ"])
print()
# Sort the DataFrame by two conditions:
#  - by the values in the "Sector" column in descending order
#  - THEN by the values in the "Security" column in ascending order
# Assign the new DataFrame to a 'by_sector_and_security' variable
by_sector_and_security = companies.sort_values(["Sector", "Security"],
                                               ascending=[False, True])
print(by_sector_and_security[["Sector", "Security"]])
