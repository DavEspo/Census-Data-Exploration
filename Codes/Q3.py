# your code goes here
# AAGE
# IQR
Q1=df["AAGE"].quantile(.25)
Q3=df["AAGE"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["AAGE"]<LowerBound)|(df["AAGE"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["AAGE"])
plt.boxplot(data)
plt.title("BoxPlot for AAGE")
plt.ylabel("Age")
plt.show()


# AHRSPAY
# IQR
Q1=df["AHRSPAY"].quantile(.25)
Q3=df["AHRSPAY"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["AHRSPAY"]<LowerBound)|(df["AHRSPAY"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["AHRSPAY"])
plt.boxplot(data)
plt.title("BoxPlot for AHRSPAY")
plt.ylabel("Wage per hour")
plt.show()


# CAPGAIN
# IQR
Q1=df["CAPGAIN"].quantile(.25)
Q3=df["CAPGAIN"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["CAPGAIN"]<LowerBound)|(df["CAPGAIN"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["CAPGAIN"])
plt.boxplot(data)
plt.title("BoxPlot for CAPGAIN")
plt.ylabel("Capital Gains")
plt.show()


# CAPLOSS
# IQR
Q1=df["CAPLOSS"].quantile(.25)
Q3=df["CAPLOSS"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["CAPLOSS"]<LowerBound)|(df["CAPLOSS"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["CAPLOSS"])
plt.boxplot(data)
plt.title("BoxPlot for CAPLOSS")
plt.ylabel("Capital Losses")
plt.show()


# DIVVAL
# IQR
Q1=df["DIVVAL"].quantile(.25)
Q3=df["DIVVAL"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["DIVVAL"]<LowerBound)|(df["DIVVAL"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["DIVVAL"])
plt.boxplot(data)
plt.title("BoxPlot for DIVVAL")
plt.ylabel("Dividends from Stocks")
plt.show()


# MARSUPWT
# IQR
Q1=df["MARSUPWT"].quantile(.25)
Q3=df["MARSUPWT"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["MARSUPWT"]<LowerBound)|(df["MARSUPWT"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["MARSUPWT"])
plt.boxplot(data)
plt.title("BoxPlot for MARSUPWT")
plt.ylabel("Instance Weight")
plt.show()


# NOEMP
# IQR
Q1=df["NOEMP"].quantile(.25)
Q3=df["NOEMP"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["NOEMP"]<LowerBound)|(df["NOEMP"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["NOEMP"])
plt.boxplot(data)
plt.title("BoxPlot for NOEMP")
plt.ylabel("Num persons worked for employer")
plt.show()


# WKSWORK
# IQR
Q1=df["WKSWORK"].quantile(.25)
Q3=df["WKSWORK"].quantile(.75)
IQR=Q3-Q1

# Lower and Upper Bounds
LowerBound=Q1-1.5*IQR
print("Lower Bound:",format(LowerBound,".2f"))
UpperBound=Q3+1.5*IQR
print("Upper Bound:",format(UpperBound,".2f"))

# Outliers
Outliers=df[(df["WKSWORK"]<LowerBound)|(df["WKSWORK"]>UpperBound)].count()
NumOfOutliers=Outliers.iloc[0]
print("There are",NumOfOutliers,"Outliers")

# BoxPlot
data=(df["WKSWORK"])
plt.boxplot(data)
plt.title("BoxPlot for WKSWORK")
plt.ylabel("Weeks worked in year")
plt.show()

# My outlier analysis from the box plots displayed above make sense for the data from my continuous features because there are relatively few outliers compared to all 199523 values for each feature. 
# Also, the box plots displayed all the outliers for each feature using the IQR method. I would use the IQR method because it uses a very wise range of values and for normal distributions, it considers 
# less than 1% of the data as outliers so it encompases all the data in a very neat way.

# your code goes here
# AAGE
Clamped_DF=df["AAGE"].clip(-37.50,102.50)
print("AAGE:\nClamped Data Frame:\n",pd.DataFrame(Clamped_DF))
Updated_Cells=((Clamped_DF<df["AAGE"])|(Clamped_DF<df["AAGE"])).sum()
print("\nNum of Updated Cells:",Updated_Cells)

# MARSUPWT
Clamped_DF=df["MARSUPWT"].clip(-628.88,3879.10)
print("\n\nMARSUPWT:\nClamped Data Frame:\n",pd.DataFrame(Clamped_DF))
Updated_Cells=((Clamped_DF<df["MARSUPWT"])|(Clamped_DF>df["MARSUPWT"])).sum()
print("\nNum of Updated Cells:",Updated_Cells)

# WKSWORK
Clamped_DF=df["WKSWORK"].clip(-78.00,130.00)
print("\n\nWKSWORK:\nClamped Data Frame:\n",pd.DataFrame(Clamped_DF))
Updated_Cells=((Clamped_DF<df["WKSWORK"])|(Clamped_DF>df["WKSWORK"])).sum()
print("\nNum of Updated Cells:",Updated_Cells)
