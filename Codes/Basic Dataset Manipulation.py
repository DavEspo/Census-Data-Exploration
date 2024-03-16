# Imports the Base file to access the csv file
import Base_to_DataFrame
df=Base_to_DataFrame.df

# Displays the top 20 descending sorted instances based on age
print("Top 20 people with the highest age in descending order:")
print(df.sort_values("AAGE", ascending=False).head(20),"\n")

# Displays average age for the top 7% oldest instances
rows=df.shape[0]
top=int(rows*.07)
print("Average Age for top 7% of oldest instances:")
print(format(df.sort_values("AAGE", ascending=False).head(top).AAGE.mean(),".2f"),"\n")

# Displays median age for each race
print("Median Age for each Race:")
print(df.groupby("ARACE").AAGE.median())