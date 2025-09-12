import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('social-media.csv')

# Check the first few rows
print(df.head())

# Extract columns (make sure names match your CSV exactly)
ids = df["UserId"]
countries = df["Country"]


# Plot bar chart
plt.bar(countries, ids)
plt.xlabel("Name of the Country")
plt.ylabel("User Id")
plt.title("Users by Country")
plt.show()


# Line Plot
plt.plot(countries, ids)
plt.xlabel("Name of the Country")
plt.ylabel("User Id")
plt.title("Users by Country")
plt.show()


