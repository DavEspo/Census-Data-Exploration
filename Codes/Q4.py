# your code goes here
# Range Normalization for MARSUPWT
from sklearn.preprocessing import MaxAbsScaler
List=df["MARSUPWT"]
DF_Converted=pd.DataFrame(List)
NormalizedDF=MaxAbsScaler().fit(DF_Converted)
pd.DataFrame(NormalizedDF.transform(DF_Converted),columns=DF_Converted.columns)

# Robust Scaling for NOEMP
from sklearn.preprocessing import RobustScaler
List=df["NOEMP"]
DF_Converted=pd.DataFrame(List)
DF_Robust=pd.DataFrame(RobustScaler().fit_transform(DF_Converted),columns=DF_Converted.columns)
DF_Robust

# Z-score normalization for AAGE
from sklearn.preprocessing import StandardScaler
List=df["AAGE"]
DF_Converted=pd.DataFrame(List)
DF_std=pd.DataFrame(StandardScaler().fit_transform(DF_Converted),columns=DF_Converted.columns)
DF_std

# Log Scaling for CAPGAIN
import math
Max=df["CAPGAIN"].max()
Denominator=round(math.log10(math.ceil(Max)))
Log_NormDF=pd.DataFrame(df["CAPGAIN"].values/10**Denominator)
Log_NormDF

# Log Scaling for CAPLOSS
Max=df["CAPLOSS"].max()
Denominator=round(math.log10(math.ceil(Max)))
Log_NormDF=pd.DataFrame(df["CAPLOSS"].values/10**Denominator)
Log_NormDF
