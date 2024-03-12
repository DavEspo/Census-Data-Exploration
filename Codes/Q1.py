# your code goes here
df = pd.read_csv('census-income.zip', compression='zip', names=columns_abbr, sep=r',', skipinitialspace=True)
df.sort_values("AAGE", ascending=False).head(20)

# your code goes here
rows=df.shape[0]
top=int(rows*.07)
format(df.sort_values("AAGE", ascending=False).head(top).AAGE.mean(),".2f")

df.groupby("ARACE").AAGE.median()
