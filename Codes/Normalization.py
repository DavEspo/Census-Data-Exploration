# Imports the Base file to access the csv file and the imports
import Base_to_DataFrame
df=Base_to_DataFrame.df
pd=Base_to_DataFrame.pd

# Different Normalization techniques applied on a few features
# Range Normalization for MARSUPWT
from sklearn.preprocessing import MaxAbsScaler
List=df["MARSUPWT"]
DF_Converted=pd.DataFrame(List)
NormalizedDF=MaxAbsScaler().fit(DF_Converted)
print("Range Normalization:\nDataFrame for MARSUPWT:\n",pd.DataFrame(NormalizedDF.transform(DF_Converted),columns=DF_Converted.columns))

# Robust Scaling for NOEMP
from sklearn.preprocessing import RobustScaler
List=df["NOEMP"]
DF_Converted=pd.DataFrame(List)
DF_Robust=pd.DataFrame(RobustScaler().fit_transform(DF_Converted),columns=DF_Converted.columns)
print("\n\nRobust Scaling:\nDataFrame for NOEMP:\n",DF_Robust)

# Z-score normalization for AAGE
from sklearn.preprocessing import StandardScaler
List=df["AAGE"]
DF_Converted=pd.DataFrame(List)
DF_std=pd.DataFrame(StandardScaler().fit_transform(DF_Converted),columns=DF_Converted.columns)
print("\n\nZ-score normalization:\nDataFrame for AAGE:\n",DF_std)

# Log Scaling for CAPGAIN
import math
Max=df["CAPGAIN"].max()
Denominator=round(math.log10(math.ceil(Max)))
Log_NormDF=pd.DataFrame(df["CAPGAIN"].values/10**Denominator)
print("\n\nLog Scaling:\nDataFrame for CAPGAIN:\n",Log_NormDF)

# Log Scaling for CAPLOSS
Max=df["CAPLOSS"].max()
Denominator=round(math.log10(math.ceil(Max)))
Log_NormDF=pd.DataFrame(df["CAPLOSS"].values/10**Denominator)
print("\nDataFrame for CAPLOSS:\n",Log_NormDF)