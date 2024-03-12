# your code goes here
# This cell shows how to fill in the table in the features.csv file
# Description is given in the websites provided at the beginning of this homework
# The 2nd line below outputs the data types for each attribute
print("Data types:")
print(df.dtypes)
# Data scale is determined by ourselves depending on what operations can be done on the data for each attribute. It is nominal if we can only find mode, ordinal if we can find median, 
      # interval if we can find arithmetic mean, and ratio if we can find geometric mean. This also helps us for Q2.2 to determine whether each attribute is categorical or continuous 
      # because if it's nominal or ordinal, it's categorical but if it's interval or ratio, it's continuous
# Domain is given by the code below which is applied to every attribute and we choose a few to write down for each
print("\n\nDomain of each attribute:")
print("AAGE:",df["AAGE"].unique(),"\n\nACLSWKR:",df["ACLSWKR"].unique(),"\n\nADTIND:",df["ADTIND"].unique(),"\n\nADTOCC:",df["ADTOCC"].unique(),"\n\nAHGA:",
      df["AHGA"].unique(),"\n\nAHRSPAY:",df["AHRSPAY"].unique(),"\n\nAHSCOL:",df["AHSCOL"].unique(),"\n\nAMARITL:",df["AMARITL"].unique(),"\n\nAMJIND:",
      df["AMJIND"].unique(),"\n\nAMJOCC:",df["AMJOCC"].unique(),"\n\nARACE:",df["ARACE"].unique(),"\n\nAREORGN:",df["AREORGN"].unique(),"\n\nASEX:",
      df["ASEX"].unique(),"\n\nAUNMEM:",df["AUNMEM"].unique(),"\n\nAUNTYPE:",df["AUNTYPE"].unique(),"\n\nAWKSTAT:",df["AWKSTAT"].unique(),"\n\nCAPGAIN:",
      df["CAPGAIN"].unique(),"\n\nCAPLOSS:",df["CAPLOSS"].unique(),"\n\nDIVVAL:",df["DIVVAL"].unique(),"\n\nFILESTAT:",df["FILESTAT"].unique(),"\n\nGRINREG:",
      df["GRINREG"].unique(),"\n\nGRINST:",df["GRINST"].unique(),"\n\nHHDFMX:",df["HHDFMX"].unique(),"\n\nHHDREL:",df["HHDREL"].unique(),"\n\nMARSUPWT:",
      df["MARSUPWT"].unique(),"\n\nMIGMTR1:",df["MIGMTR1"].unique(),"\n\nMIGMTR3:",df["MIGMTR3"].unique(),"\n\nMIGMTR4:",df["MIGMTR4"].unique(),"\n\nMIGSAME:",
      df["MIGSAME"].unique(),"\n\nMIGSUN:",df["MIGSUN"].unique(),"\n\nNOEMP:",df["NOEMP"].unique(),"\n\nPARENT:",df["PARENT"].unique(),"\n\nPEFNTVTY:",
      df["PEFNTVTY"].unique(),"\n\nPEMNTVTY:",df["PEMNTVTY"].unique(),"\n\nPENATVTY:",df["PENATVTY"].unique(),"\n\nPRCITSHP:",df["PRCITSHP"].unique(),"\n\nSEOTR:",
      df["SEOTR"].unique(),"\n\nVETQVA:",df["VETQVA"].unique(),"\n\nVETYN:",df["VETYN"].unique(),"\n\nWKSWORK:",df["WKSWORK"].unique(),"\n\nYEAR:",
      df["YEAR"].unique(),"\n\nPTOTVALB:",df["PTOTVALB"].unique())
# The 2nd line below checks for the existance of some values. The 4th line checks which attributes have a '?'. The last 3 lines show how many '?' there are 
      # in the attributes that contain it.
print("\n\nChecking for missing values:")
print(df.isin(["Na"]).any().any(),"\n",df.isin(["NaN"]).any().any(),"\n",df.isin([None]).any().any(),"\n",df.isin(["?"]).any().any())
print("\nAttributes that have missing values:")
print(df.isin(["?"]).any())
print("\nAmount of missing values of the attributes containing missing values:")
print("GRINST:",df["GRINST"].value_counts()["?"],"\nMIGMTR1:",df["MIGMTR1"].value_counts()["?"],"\nMIGMTR3:",df["MIGMTR3"].value_counts()["?"],"\nMIGMTR4:",
      df["MIGMTR4"].value_counts()["?"],"\nMIGSUN:",df["MIGSUN"].value_counts()["?"],"\nPEFNTVTY:",df["PEFNTVTY"].value_counts()["?"],"\nPEMNTVTY:",
      df["PEMNTVTY"].value_counts()["?"],"\nPENATVTY:",df["PENATVTY"].value_counts()["?"])

# please fill the information for the data characteristics in the given csv file. read it here and display.
features_df = pd.read_csv('./featuresValues.csv', index_col ='col_name')
features_df

# your code goes here
DF={"Feature":["AAGE","AHRSPAY","CAPGAIN","CAPLOSS","DIVVAL","MARSUPWT","NOEMP","WKSWORK"],
    "Desc.":[features_df.iat[0,0],features_df.iat[5,0],features_df.iat[16,0],features_df.iat[17,0],features_df.iat[18,0],features_df.iat[24,0],features_df.iat[30,0],features_df.iat[39,0]],
    "Count":[df["AAGE"].count(),df["AHRSPAY"].count(),df["CAPGAIN"].count(),df["CAPLOSS"].count(),df["DIVVAL"].count(),df["MARSUPWT"].count(),df["NOEMP"].count(),df["WKSWORK"].count()],
    "% of Missing":[format((features_df.iat[0,4]/int(df["AAGE"].count()))*10,".2f"),format((features_df.iat[5,4]/int(df["AHRSPAY"].count()))*10,".2f"),
                    format((features_df.iat[16,4]/int(df["CAPGAIN"].count()))*10,".2f"),format((features_df.iat[17,4]/int(df["CAPLOSS"].count()))*10,".2f"),
                    format((features_df.iat[18,4]/int(df["DIVVAL"].count()))*10,".2f"),format((features_df.iat[24,4]/int(df["MARSUPWT"].count()))*10,".2f"),
                    format((features_df.iat[30,4]/int(df["NOEMP"].count()))*10,".2f"),format((features_df.iat[39,4]/int(df["WKSWORK"].count()))*10,".2f")],
    "Card":[df["AAGE"].unique().size,df["AHRSPAY"].unique().size,df["CAPGAIN"].unique().size,df["CAPLOSS"].unique().size,
            df["DIVVAL"].unique().size,df["MARSUPWT"].unique().size,df["NOEMP"].unique().size,df["WKSWORK"].unique().size],
    "Min":[format(df["AAGE"].min(),".2f"),format(df["AHRSPAY"].min(),".2f"),format(df["CAPGAIN"].min(),".2f"),format(df["CAPLOSS"].min(),".2f"),
           format(df["DIVVAL"].min(),".2f"),format(df["MARSUPWT"].min(),".2f"),format(df["NOEMP"].min(),".2f"),format(df["WKSWORK"].min(),".2f")],
    "Q1":[format(df["AAGE"].quantile(.25),".2f"),format(df["AHRSPAY"].quantile(.25),".2f"),format(df["CAPGAIN"].quantile(.25),".2f"),format(df["CAPLOSS"].quantile(.25),".2f"),
          format(df["DIVVAL"].quantile(.25),".2f"),format(df["MARSUPWT"].quantile(.25),".2f"),format(df["NOEMP"].quantile(.25),".2f"),format(df["WKSWORK"].quantile(.25),".2f")],
    "Med":[format(df["AAGE"].median(),".2f"),format(df["AHRSPAY"].median(),".2f"),format(df["CAPGAIN"].median(),".2f"),format(df["CAPLOSS"].median(),".2f"),
           format(df["DIVVAL"].median(),".2f"),format(df["MARSUPWT"].median(),".2f"),format(df["NOEMP"].median(),".2f"),format(df["WKSWORK"].median(),".2f")],
    "Q3":[format(df["AAGE"].quantile(.75),".2f"),format(df["AHRSPAY"].quantile(.75),".2f"),format(df["CAPGAIN"].quantile(.75),".2f"),format(df["CAPLOSS"].quantile(.75),".2f"),
          format(df["DIVVAL"].quantile(.75),".2f"),format(df["MARSUPWT"].quantile(.75),".2f"),format(df["NOEMP"].quantile(.75),".2f"),format(df["WKSWORK"].quantile(.75),".2f")],
    "Max":[format(df["AAGE"].max(),".2f"),format(df["AHRSPAY"].max(),".2f"),format(df["CAPGAIN"].max(),".2f"),format(df["CAPLOSS"].max(),".2f"),
           format(df["DIVVAL"].max(),".2f"),format(df["MARSUPWT"].max(),".2f"),format(df["NOEMP"].max(),".2f"),format(df["WKSWORK"].max(),".2f")],
    "Mean":[format(df["AAGE"].mean(),".2f"),format(df["AHRSPAY"].mean(),".2f"),format(df["CAPGAIN"].mean(),".2f"),format(df["CAPLOSS"].mean(),".2f"),
            format(df["DIVVAL"].mean(),".2f"),format(df["MARSUPWT"].mean(),".2f"),format(df["NOEMP"].mean(),".2f"),format(df["WKSWORK"].mean(),".2f")],
    "Std. Dev.":[format(df["AAGE"].std(),".2f"),format(df["AHRSPAY"].std(),".2f"),format(df["CAPGAIN"].std(),".2f"),format(df["CAPLOSS"].std(),".2f"),
                 format(df["DIVVAL"].std(),".2f"),format(df["MARSUPWT"].std(),".2f"),format(df["NOEMP"].std(),".2f"),format(df["WKSWORK"].std(),".2f")]}

df_continuous=pd.DataFrame(DF)
df_continuous.style

DF2={"Feature":["ACLSWKR","ADTIND","ADTOCC","AHGA","AHSCOL","AMARITL","AMJIND","AMJOCC","ARACE","AREORGN","ASEX","AUNMEM",
                "AUNTYPE","AWKSTAT","FILESTAT","GRINREG","GRINST","HHDFMX","HHDREL","MIGMTR1","MIGMTR3","MIGMTR4","MIGSAME",
                "MIGSUN","PARENT","PEFNTVTY","PEMNTVTY","PENATVTY","PRCITSHP","SEOTR","VETQVA","VETYN","YEAR","PTOTVALB"],
     "Desc.":[features_df.iat[1,0],features_df.iat[2,0],features_df.iat[3,0],features_df.iat[4,0],features_df.iat[6,0],features_df.iat[7,0],features_df.iat[8,0],
              features_df.iat[9,0],features_df.iat[10,0],features_df.iat[11,0],features_df.iat[12,0],features_df.iat[13,0],features_df.iat[14,0],features_df.iat[15,0],
              features_df.iat[19,0],features_df.iat[20,0],features_df.iat[21,0],features_df.iat[22,0],features_df.iat[23,0],features_df.iat[25,0],features_df.iat[26,0],
              features_df.iat[27,0],features_df.iat[28,0],features_df.iat[29,0],features_df.iat[31,0],features_df.iat[32,0],features_df.iat[33,0],features_df.iat[34,0],
              features_df.iat[35,0],features_df.iat[36,0],features_df.iat[37,0],features_df.iat[38,0],features_df.iat[40,0],features_df.iat[41,0]],
     "Count":[df["ACLSWKR"].count(),df["ADTIND"].count(),df["ADTOCC"].count(),df["AHGA"].count(),df["AHSCOL"].count(),df["AMARITL"].count(),df["AMJIND"].count(),
              df["AMJOCC"].count(),df["ARACE"].count(),df["AREORGN"].count(),df["ASEX"].count(),df["AUNMEM"].count(),df["AUNTYPE"].count(),df["AWKSTAT"].count(),
              df["FILESTAT"].count(),df["GRINREG"].count(),df["GRINST"].count(),df["HHDFMX"].count(),df["HHDREL"].count(),df["MIGMTR1"].count(),df["MIGMTR3"].count(),
              df["MIGMTR4"].count(),df["MIGSAME"].count(),df["MIGSUN"].count(),df["PARENT"].count(),df["PEFNTVTY"].count(),df["PEMNTVTY"].count(),df["PENATVTY"].count(),
              df["PRCITSHP"].count(),df["SEOTR"].count(),df["VETQVA"].count(),df["VETYN"].count(),df["YEAR"].count(),df["PTOTVALB"].count()],
     "% of Missing":[format((features_df.iat[1,4]/int(df["ACLSWKR"].count()))*10,".2f"),format((features_df.iat[2,4]/int(df["ADTIND"].count()))*10,".2f"),
                     format((features_df.iat[3,4]/int(df["ADTOCC"].count()))*10,".2f"),format((features_df.iat[4,4]/int(df["AHGA"].count()))*10,".2f"),
                     format((features_df.iat[6,4]/int(df["AHSCOL"].count()))*10,".2f"),format((features_df.iat[7,4]/int(df["AMARITL"].count()))*10,".2f"),
                     format((features_df.iat[8,4]/int(df["AMJIND"].count()))*10,".2f"),format((features_df.iat[9,4]/int(df["AMJOCC"].count()))*10,".2f"),
                     format((features_df.iat[10,4]/int(df["ARACE"].count()))*10,".2f"),format((features_df.iat[11,4]/int(df["AREORGN"].count()))*10,".2f"),
                     format((features_df.iat[12,4]/int(df["ASEX"].count()))*10,".2f"),format((features_df.iat[13,4]/int(df["AUNMEM"].count()))*10,".2f"),
                     format((features_df.iat[14,4]/int(df["AUNTYPE"].count()))*10,".2f"),format((features_df.iat[15,4]/int(df["AWKSTAT"].count()))*10,".2f"),
                     format((features_df.iat[19,4]/int(df["FILESTAT"].count()))*10,".2f"),format((features_df.iat[20,4]/int(df["GRINREG"].count()))*10,".2f"),
                     format((features_df.iat[21,4]/int(df["GRINST"].count()))*10,".2f"),format((features_df.iat[22,4]/int(df["HHDFMX"].count()))*10,".2f"),
                     format((features_df.iat[23,4]/int(df["HHDREL"].count()))*10,".2f"),format((features_df.iat[25,4]/int(df["MIGMTR1"].count()))*10,".2f"),
                     format((features_df.iat[26,4]/int(df["MIGMTR3"].count()))*10,".2f"),format((features_df.iat[27,4]/int(df["MIGMTR4"].count()))*10,".2f"),
                     format((features_df.iat[28,4]/int(df["MIGSAME"].count()))*10,".2f"),format((features_df.iat[29,4]/int(df["MIGSUN"].count()))*10,".2f"),
                     format((features_df.iat[31,4]/int(df["PARENT"].count()))*10,".2f"),format((features_df.iat[32,4]/int(df["PEFNTVTY"].count()))*10,".2f"),
                     format((features_df.iat[33,4]/int(df["PEMNTVTY"].count()))*10,".2f"),format((features_df.iat[34,4]/int(df["PENATVTY"].count()))*10,".2f"),
                     format((features_df.iat[35,4]/int(df["PRCITSHP"].count()))*10,".2f"),format((features_df.iat[36,4]/int(df["SEOTR"].count()))*10,".2f"),
                     format((features_df.iat[37,4]/int(df["VETQVA"].count()))*10,".2f"),format((features_df.iat[38,4]/int(df["VETYN"].count()))*10,".2f"),
                     format((features_df.iat[40,4]/int(df["YEAR"].count()))*10,".2f"),format((features_df.iat[41,4]/int(df["PTOTVALB"].count()))*10,".2f")],
     "Card.":[df["ACLSWKR"].unique().size,df["ADTIND"].unique().size,df["ADTOCC"].unique().size,df["AHGA"].unique().size,df["AHSCOL"].unique().size,df["AMARITL"].unique().size,
              df["AMJIND"].unique().size,df["AMJOCC"].unique().size,df["ARACE"].unique().size,df["AREORGN"].unique().size,df["ASEX"].unique().size,df["AUNMEM"].unique().size,
              df["AUNTYPE"].unique().size,df["AWKSTAT"].unique().size,df["FILESTAT"].unique().size,df["GRINREG"].unique().size,df["GRINST"].unique().size,df["HHDFMX"].unique().size,
              df["HHDREL"].unique().size,df["MIGMTR1"].unique().size,df["MIGMTR3"].unique().size,df["MIGMTR4"].unique().size,df["MIGSAME"].unique().size,df["MIGSUN"].unique().size,
              df["PARENT"].unique().size,df["PEFNTVTY"].unique().size,df["PEMNTVTY"].unique().size,df["PENATVTY"].unique().size,df["PRCITSHP"].unique().size,df["SEOTR"].unique().size,
              df["VETQVA"].unique().size,df["VETYN"].unique().size,df["YEAR"].unique().size,df["PTOTVALB"].unique().size],
     "Mode":[df["ACLSWKR"].mode().iloc[0],df["ADTIND"].mode().iloc[0],df["ADTOCC"].mode().iloc[0],df["AHGA"].mode().iloc[0],df["AHSCOL"].mode().iloc[0],df["AMARITL"].mode().iloc[0],
             df["AMJIND"].mode().iloc[0],df["AMJOCC"].mode().iloc[0],df["ARACE"].mode().iloc[0],df["AREORGN"].mode().iloc[0],df["ASEX"].mode().iloc[0],df["AUNMEM"].mode().iloc[0],
             df["AUNTYPE"].mode().iloc[0],df["AWKSTAT"].mode().iloc[0],df["FILESTAT"].mode().iloc[0],df["GRINREG"].mode().iloc[0],df["GRINST"].mode().iloc[0],df["HHDFMX"].mode().iloc[0],
             df["HHDREL"].mode().iloc[0],df["MIGMTR1"].mode().iloc[0],df["MIGMTR3"].mode().iloc[0],df["MIGMTR4"].mode().iloc[0],df["MIGSAME"].mode().iloc[0],df["MIGSUN"].mode().iloc[0],
             df["PARENT"].mode().iloc[0],df["PEFNTVTY"].mode().iloc[0],df["PEMNTVTY"].mode().iloc[0],df["PENATVTY"].mode().iloc[0],df["PRCITSHP"].mode().iloc[0],df["SEOTR"].mode().iloc[0],
             df["VETQVA"].mode().iloc[0],df["VETYN"].mode().iloc[0],df["YEAR"].mode().iloc[0],df["PTOTVALB"].mode().iloc[0]],
     "Mode Freq.":[df["ACLSWKR"].value_counts().iat[0],df["ADTIND"].value_counts().iat[0],df["ADTOCC"].value_counts().iat[0],df["AHGA"].value_counts().iat[0],df["AHSCOL"].value_counts().iat[0],
                   df["AMARITL"].value_counts().iat[0],df["AMJIND"].value_counts().iat[0],df["AMJOCC"].value_counts().iat[0],df["ARACE"].value_counts().iat[0],df["AREORGN"].value_counts().iat[0],
                   df["ASEX"].value_counts().iat[0],df["AUNMEM"].value_counts().iat[0],df["AUNTYPE"].value_counts().iat[0],df["AWKSTAT"].value_counts().iat[0],df["FILESTAT"].value_counts().iat[0],
                   df["GRINREG"].value_counts().iat[0],df["GRINST"].value_counts().iat[0],df["HHDFMX"].value_counts().iat[0],df["HHDREL"].value_counts().iat[0],df["MIGMTR1"].value_counts().iat[0],
                   df["MIGMTR3"].value_counts().iat[0],df["MIGMTR4"].value_counts().iat[0],df["MIGSAME"].value_counts().iat[0],df["MIGSUN"].value_counts().iat[0],df["PARENT"].value_counts().iat[0],
                   df["PEFNTVTY"].value_counts().iat[0],df["PEMNTVTY"].value_counts().iat[0],df["PENATVTY"].value_counts().iat[0],df["PRCITSHP"].value_counts().iat[0],df["SEOTR"].value_counts().iat[0],
                   df["VETQVA"].value_counts().iat[0],df["VETYN"].value_counts().iat[0],df["YEAR"].value_counts().iat[0],df["PTOTVALB"].value_counts().iat[0]],
     "Mode %":[format((df["ACLSWKR"].value_counts().iloc[0]/df["ACLSWKR"].count())*100,".2f"),format((df["ADTIND"].value_counts().iloc[0]/df["ADTIND"].count())*100,".2f"),
               format((df["ADTOCC"].value_counts().iloc[0]/df["ADTOCC"].count())*100,".2f"),format((df["AHGA"].value_counts().iloc[0]/df["AHGA"].count())*100,".2f"),
               format((df["AHSCOL"].value_counts().iloc[0]/df["AHSCOL"].count())*100,".2f"),format((df["AMARITL"].value_counts().iloc[0]/df["AMARITL"].count())*100,".2f"),
               format((df["AMJIND"].value_counts().iloc[0]/df["AMJIND"].count())*100,".2f"),format((df["AMJOCC"].value_counts().iloc[0]/df["AMJOCC"].count())*100,".2f"),
               format((df["ARACE"].value_counts().iloc[0]/df["ARACE"].count())*100,".2f"),format((df["AREORGN"].value_counts().iloc[0]/df["AREORGN"].count())*100,".2f"),
               format((df["ASEX"].value_counts().iloc[0]/df["ASEX"].count())*100,".2f"),format((df["AUNMEM"].value_counts().iloc[0]/df["AUNMEM"].count())*100,".2f"),
               format((df["AUNTYPE"].value_counts().iloc[0]/df["AUNTYPE"].count())*100,".2f"),format((df["AWKSTAT"].value_counts().iloc[0]/df["AWKSTAT"].count())*100,".2f"),
               format((df["FILESTAT"].value_counts().iloc[0]/df["FILESTAT"].count())*100,".2f"),format((df["GRINREG"].value_counts().iloc[0]/df["GRINREG"].count())*100,".2f"),
               format((df["GRINST"].value_counts().iloc[0]/df["GRINST"].count())*100,".2f"),format((df["HHDFMX"].value_counts().iloc[0]/df["HHDFMX"].count())*100,".2f"),
               format((df["HHDREL"].value_counts().iloc[0]/df["HHDREL"].count())*100,".2f"),format((df["MIGMTR1"].value_counts().iloc[0]/df["MIGMTR1"].count())*100,".2f"),
               format((df["MIGMTR3"].value_counts().iloc[0]/df["MIGMTR3"].count())*100,".2f"),format((df["MIGMTR4"].value_counts().iloc[0]/df["MIGMTR4"].count())*100,".2f"),
               format((df["MIGSAME"].value_counts().iloc[0]/df["MIGSAME"].count())*100,".2f"),format((df["MIGSUN"].value_counts().iloc[0]/df["MIGSUN"].count())*100,".2f"),
               format((df["PARENT"].value_counts().iloc[0]/df["PARENT"].count())*100,".2f"),format((df["PEFNTVTY"].value_counts().iloc[0]/df["PEFNTVTY"].count())*100,".2f"),
               format((df["PEMNTVTY"].value_counts().iloc[0]/df["PEMNTVTY"].count())*100,".2f"),format((df["PENATVTY"].value_counts().iloc[0]/df["PENATVTY"].count())*100,".2f"),
               format((df["PRCITSHP"].value_counts().iloc[0]/df["PRCITSHP"].count())*100,".2f"),format((df["SEOTR"].value_counts().iloc[0]/df["SEOTR"].count())*100,".2f"),
               format((df["VETQVA"].value_counts().iloc[0]/df["VETQVA"].count())*100,".2f"),format((df["VETYN"].value_counts().iloc[0]/df["VETYN"].count())*100,".2f"),
               format((df["YEAR"].value_counts().iloc[0]/df["YEAR"].count())*100,".2f"),format((df["PTOTVALB"].value_counts().iloc[0]/df["PTOTVALB"].count())*100,".2f")],
     "2nd Mode":[df["ACLSWKR"].value_counts().index[1],df["ADTIND"].value_counts().index[1],df["ADTOCC"].value_counts().index[1],df["AHGA"].value_counts().index[1],
                 df["AHSCOL"].value_counts().index[1],df["AMARITL"].value_counts().index[1],df["AMJIND"].value_counts().index[1],df["AMJOCC"].value_counts().index[1],
                 df["ARACE"].value_counts().index[1],df["AREORGN"].value_counts().index[1],df["ASEX"].value_counts().index[1],df["AUNMEM"].value_counts().index[1],
                 df["AUNTYPE"].value_counts().index[1],df["AWKSTAT"].value_counts().index[1],df["FILESTAT"].value_counts().index[1],df["GRINREG"].value_counts().index[1],
                 df["GRINST"].value_counts().index[1],df["HHDFMX"].value_counts().index[1],df["HHDREL"].value_counts().index[1],df["MIGMTR1"].value_counts().index[1],
                 df["MIGMTR3"].value_counts().index[1],df["MIGMTR4"].value_counts().index[1],df["MIGSAME"].value_counts().index[1],df["MIGSUN"].value_counts().index[1],
                 df["PARENT"].value_counts().index[1],df["PEFNTVTY"].value_counts().index[1],df["PEMNTVTY"].value_counts().index[1],df["PENATVTY"].value_counts().index[1],
                 df["PRCITSHP"].value_counts().index[1],df["SEOTR"].value_counts().index[1],df["VETQVA"].value_counts().index[1],df["VETYN"].value_counts().index[1],
                 df["YEAR"].value_counts().index[1],df["PTOTVALB"].value_counts().index[1]],
     "2nd Mode Freq.":[df["ACLSWKR"].value_counts().iat[1],df["ADTIND"].value_counts().iat[1],df["ADTOCC"].value_counts().iat[1],df["AHGA"].value_counts().iat[1],
                       df["AHSCOL"].value_counts().iat[1],df["AMARITL"].value_counts().iat[1],df["AMJIND"].value_counts().iat[1],df["AMJOCC"].value_counts().iat[1],
                       df["ARACE"].value_counts().iat[1],df["AREORGN"].value_counts().iat[1],df["ASEX"].value_counts().iat[1],df["AUNMEM"].value_counts().iat[1],
                       df["AUNTYPE"].value_counts().iat[1],df["AWKSTAT"].value_counts().iat[1],df["FILESTAT"].value_counts().iat[1],df["GRINREG"].value_counts().iat[1],
                       df["GRINST"].value_counts().iat[1],df["HHDFMX"].value_counts().iat[1],df["HHDREL"].value_counts().iat[1],df["MIGMTR1"].value_counts().iat[1],
                       df["MIGMTR3"].value_counts().iat[1],df["MIGMTR4"].value_counts().iat[1],df["MIGSAME"].value_counts().iat[1],df["MIGSUN"].value_counts().iat[1],
                       df["PARENT"].value_counts().iat[1],df["PEFNTVTY"].value_counts().iat[1],df["PEMNTVTY"].value_counts().iat[1],df["PENATVTY"].value_counts().iat[1],
                       df["PRCITSHP"].value_counts().iat[1],df["SEOTR"].value_counts().iat[1],df["VETQVA"].value_counts().iat[1],df["VETYN"].value_counts().iat[1],
                       df["YEAR"].value_counts().iat[1],df["PTOTVALB"].value_counts().iat[1]],
     "2nd Mode Perc":[format((df["ACLSWKR"].value_counts().iloc[1]/df["ACLSWKR"].count())*100,".2f"),format((df["ADTIND"].value_counts().iloc[1]/df["ADTIND"].count())*100,".2f"),
                      format((df["ADTOCC"].value_counts().iloc[1]/df["ADTOCC"].count())*100,".2f"),format((df["AHGA"].value_counts().iloc[1]/df["AHGA"].count())*100,".2f"),
                      format((df["AHSCOL"].value_counts().iloc[1]/df["AHSCOL"].count())*100,".2f"),format((df["AMARITL"].value_counts().iloc[1]/df["AMARITL"].count())*100,".2f"),
                      format((df["AMJIND"].value_counts().iloc[1]/df["AMJIND"].count())*100,".2f"),format((df["AMJOCC"].value_counts().iloc[1]/df["AMJOCC"].count())*100,".2f"),
                      format((df["ARACE"].value_counts().iloc[1]/df["ARACE"].count())*100,".2f"),format((df["AREORGN"].value_counts().iloc[1]/df["AREORGN"].count())*100,".2f"),
                      format((df["ASEX"].value_counts().iloc[1]/df["ASEX"].count())*100,".2f"),format((df["AUNMEM"].value_counts().iloc[1]/df["AUNMEM"].count())*100,".2f"),
                      format((df["AUNTYPE"].value_counts().iloc[1]/df["AUNTYPE"].count())*100,".2f"),format((df["AWKSTAT"].value_counts().iloc[1]/df["AWKSTAT"].count())*100,".2f"),
                      format((df["FILESTAT"].value_counts().iloc[1]/df["FILESTAT"].count())*100,".2f"),format((df["GRINREG"].value_counts().iloc[1]/df["GRINREG"].count())*100,".2f"),
                      format((df["GRINST"].value_counts().iloc[1]/df["GRINST"].count())*100,".2f"),format((df["HHDFMX"].value_counts().iloc[1]/df["HHDFMX"].count())*100,".2f"),
                      format((df["HHDREL"].value_counts().iloc[1]/df["HHDREL"].count())*100,".2f"),format((df["MIGMTR1"].value_counts().iloc[1]/df["MIGMTR1"].count())*100,".2f"),
                      format((df["MIGMTR3"].value_counts().iloc[1]/df["MIGMTR3"].count())*100,".2f"),format((df["MIGMTR4"].value_counts().iloc[1]/df["MIGMTR4"].count())*100,".2f"),
                      format((df["MIGSAME"].value_counts().iloc[1]/df["MIGSAME"].count())*100,".2f"),format((df["MIGSUN"].value_counts().iloc[1]/df["MIGSUN"].count())*100,".2f"),
                      format((df["PARENT"].value_counts().iloc[1]/df["PARENT"].count())*100,".2f"),format((df["PEFNTVTY"].value_counts().iloc[1]/df["PEFNTVTY"].count())*100,".2f"),
                      format((df["PEMNTVTY"].value_counts().iloc[1]/df["PEMNTVTY"].count())*100,".2f"),format((df["PENATVTY"].value_counts().iloc[1]/df["PENATVTY"].count())*100,".2f"),
                      format((df["PRCITSHP"].value_counts().iloc[1]/df["PRCITSHP"].count())*100,".2f"),format((df["SEOTR"].value_counts().iloc[1]/df["SEOTR"].count())*100,".2f"),
                      format((df["VETQVA"].value_counts().iloc[1]/df["VETQVA"].count())*100,".2f"),format((df["VETYN"].value_counts().iloc[1]/df["VETYN"].count())*100,".2f"),
                      format((df["YEAR"].value_counts().iloc[1]/df["YEAR"].count())*100,".2f"),format((df["PTOTVALB"].value_counts().iloc[1]/df["PTOTVALB"].count())*100,".2f")]}

df_categorical=pd.DataFrame(DF2)
df_categorical.style

# bar plots
# ACLSWKR
values=df["ACLSWKR"].unique()
instances=df["ACLSWKR"].value_counts()
plt.subplots(figsize=(6,4))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Class of Worker")
plt.title("Bar Plot for ACLSWKR")
plt.show()

# ADTIND
values=df["ADTIND"].unique()
instances=df["ADTIND"].value_counts()
plt.subplots(figsize=(9,5))
plt.bar(values,instances)
plt.xlabel("Industry Code")
plt.ylabel("No. of People")
plt.title("Bar Plot for ADTIND")
plt.show()

# ADTOCC
values=df["ADTOCC"].unique()
instances=df["ADTOCC"].value_counts()
plt.subplots(figsize=(9,5))
plt.bar(values,instances)
plt.xlabel("Occupation Code")
plt.ylabel("No. of People")
plt.title("Bar Plot for ADTOCC")
plt.show()

# AHGA
values=df["AHGA"].unique()
instances=df["AHGA"].value_counts()
plt.subplots(figsize=(7,5))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Education")
plt.title("Bar Plot for AHGA")
plt.show()

# AHSCOL
values=df["AHSCOL"].unique()
instances=df["AHSCOL"].value_counts()
plt.subplots(figsize=(5,4))
plt.bar(values,instances)
plt.xlabel("enrolled in edu inst last wk")
plt.ylabel("No. of People")
plt.title("Bar Plot for AHSCOL")
plt.show()

# AMARITL
values=df["AMARITL"].unique()
instances=df["AMARITL"].value_counts()
plt.subplots(figsize=(6,4))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("marital status")
plt.title("Bar Plot for AMARITL")
plt.show()

# AMJIND
values=df["AMJIND"].unique()
instances=df["AMJIND"].value_counts()
plt.subplots(figsize=(9,7))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("major industry code")
plt.title("Bar Plot for AMJIND")
plt.show()

# AMJOCC
values=df["AMJOCC"].unique()
instances=df["AMJOCC"].value_counts()
plt.subplots(figsize=(7,5))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("major occupation code")
plt.title("Bar Plot for AMJOCC")
plt.show()

# ARACE
values=df["ARACE"].unique()
instances=df["ARACE"].value_counts()
plt.subplots(figsize=(6,3))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("mace")
plt.title("Bar Plot for ARACE")
plt.show()

# AREORGN
values=df["AREORGN"].dropna().unique()
instances=df["AREORGN"].value_counts()
plt.subplots(figsize=(6,4))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("hispanic origin")
plt.title("Bar Plot for AREORGN")
plt.show()

# ASEX
values=df["ASEX"].unique()
instances=df["ASEX"].value_counts()
plt.subplots(figsize=(4,3))
plt.bar(values,instances)
plt.xlabel("sex")
plt.ylabel("No. of People")
plt.title("Bar Plot for ASEX")
plt.show()

# AUNMEM
values=df["AUNMEM"].unique()
instances=df["AUNMEM"].value_counts()
plt.subplots(figsize=(5,4))
plt.bar(values,instances)
plt.xlabel("member of a labor union")
plt.ylabel("No. of People")
plt.title("Bar Plot for AUNMEM")
plt.show()

# AUNTYPE
values=df["AUNTYPE"].unique()
instances=df["AUNTYPE"].value_counts()
plt.subplots(figsize=(6,3))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("reason for unemployment")
plt.title("Bar Plot for AUNTYPE")
plt.show()

# AWKSTAT
values=df["AWKSTAT"].unique()
instances=df["AWKSTAT"].value_counts()
plt.subplots(figsize=(6,4))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("full or part time employment stat")
plt.title("Bar Plot for AWKSTAT")
plt.show()

# FILESTAT
values=df["FILESTAT"].unique()
instances=df["FILESTAT"].value_counts()
plt.subplots(figsize=(6,3))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("tax filer status")
plt.title("Bar Plot for FILESTAT")
plt.show()

# GRINREG
values=df["GRINREG"].unique()
instances=df["GRINREG"].value_counts()
plt.subplots(figsize=(6,3))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("region of previous residence")
plt.title("Bar Plot for GRINREG")
plt.show()

# GRINST
values=df["GRINST"].unique()
instances=df["GRINST"].value_counts()
plt.subplots(figsize=(15,12))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("state of previous residence")
plt.title("Bar Plot for GRINST")
plt.show()

# HHDFMX
values=df["HHDFMX"].unique()
instances=df["HHDFMX"].value_counts()
plt.subplots(figsize=(12,10))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Detailed household and family stat")
plt.title("Bar Plot for HHDFMX")
plt.show()

# HHDREL
values=df["HHDREL"].unique()
instances=df["HHDREL"].value_counts()
plt.subplots(figsize=(6,4))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Detailed household summary in household")
plt.title("Bar Plot for HHDREL")
plt.show()

# MIGMTR1
values=df["MIGMTR1"].unique()
instances=df["MIGMTR1"].value_counts()
plt.subplots(figsize=(7,5))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Migration code-change in msa")
plt.title("Bar Plot for MIGMTR1")
plt.show()

# MIGMTR3
values=df["MIGMTR3"].unique()
instances=df["MIGMTR3"].value_counts()
plt.subplots(figsize=(7,5))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Migration code-change in reg")
plt.title("Bar Plot for MIGMTR3")
plt.show()

# MIGMTR4
values=df["MIGMTR4"].unique()
instances=df["MIGMTR4"].value_counts()
plt.subplots(figsize=(7,5))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Migration code-move within reg")
plt.title("Bar Plot for MIGMTR4")
plt.show()

# MIGSAME
values=df["MIGSAME"].unique()
instances=df["MIGSAME"].value_counts()
plt.subplots(figsize=(6,4))
plt.bar(values,instances)
plt.xlabel("Live in this house 1 year ago")
plt.ylabel("No. of People")
plt.title("Bar Plot for MIGSAME")
plt.show()

# MIGSUN
values=df["MIGSUN"].unique()
instances=df["MIGSUN"].value_counts()
plt.subplots(figsize=(6,4))
plt.bar(values,instances)
plt.xlabel("Migration prev res in sunbelt")
plt.ylabel("No. of People")
plt.title("Bar Plot for MIGSUN")
plt.show()

# PARENT
values=df["PARENT"].unique()
instances=df["PARENT"].value_counts()
plt.subplots(figsize=(6,3))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Family members under 18")
plt.title("Bar Plot for PARENT")
plt.show()

# PEFNTVTY
values=df["PEFNTVTY"].unique()
instances=df["PEFNTVTY"].value_counts()
plt.subplots(figsize=(14,11))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Country of birth father")
plt.title("Bar Plot for PEFNTVTY")
plt.show()

# PEMNTVTY
values=df["PEMNTVTY"].unique()
instances=df["PEMNTVTY"].value_counts()
plt.subplots(figsize=(14,11))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Country of birth mother")
plt.title("Bar Plot for PEMNTVTY")
plt.show()

# PENATVTY
values=df["PENATVTY"].unique()
instances=df["PENATVTY"].value_counts()
plt.subplots(figsize=(14,11))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("Country of birth self")
plt.title("Bar Plot for PENATVTY")
plt.show()

# PRCITSHP
values=df["PRCITSHP"].unique()
instances=df["PRCITSHP"].value_counts()
plt.subplots(figsize=(6,3))
plt.barh(values,instances)
plt.xlabel("No. of People")
plt.ylabel("citizenship")
plt.title("Bar Plot for PRCITSHP")
plt.show()

# SEOTR
values=df["SEOTR"].unique()
instances=df["SEOTR"].value_counts()
plt.subplots(figsize=(5,3))
plt.bar(values,instances)
plt.xlabel("Own business or self employment")
plt.ylabel("No. of People")
plt.title("Bar Plot for SEOTR")
plt.show()

# VETQVA
values=df["VETQVA"].unique()
instances=df["VETQVA"].value_counts()
plt.subplots(figsize=(5,3))
plt.bar(values,instances)
plt.xlabel("Fill inc questionnaire for veteran’s admin")
plt.ylabel("No. of People")
plt.title("Bar Plot for VETQVA")
plt.show()

# VETYN
values=df["VETYN"].unique()
instances=df["VETYN"].value_counts()
plt.subplots(figsize=(5,3))
plt.bar(values,instances)
plt.xlabel("Veterans benefits")
plt.ylabel("No. of People")
plt.title("Bar Plot for VETYN")
plt.show()

# YEAR
values=df["YEAR"].unique()
instances=df["YEAR"].value_counts()
plt.subplots(figsize=(4,3))
plt.bar(values,instances)
plt.xlabel("Year survey was done")
plt.ylabel("No. of People")
plt.title("Bar Plot for YEAR")
plt.show()

# PTOTVALB
values=df["PTOTVALB"].unique()
instances=df["PTOTVALB"].value_counts()
plt.subplots(figsize=(4,3))
plt.bar(values,instances)
plt.xlabel("Total person income")
plt.ylabel("No. of People")
plt.title("Bar Plot for PTOTVALB")
plt.show()

# histograms
# AAGE
data=df["AAGE"]
plt.hist(data,bins=range(min(data),max(data)+10,10),color="skyblue",edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram for AAGE")
plt.show()

# AHRSPAY
data=df["AHRSPAY"]
plt.hist(data,bins=range(min(data),max(data)+1000,1000),color="skyblue",edgecolor="black")
plt.xlabel("Wage per Hour")
plt.ylabel("Frequency")
plt.title("Histogram for AHRSPAY")
plt.show()

# CAPGAIN
data=df["CAPGAIN"]
plt.hist(data,bins=range(min(data),max(data)+10000,10000),color="skyblue",edgecolor="black")
plt.xlabel("Capital Gains")
plt.ylabel("Frequency")
plt.title("Histogram for CAPGAIN")
plt.show()

# CAPLOSS
data=df["CAPLOSS"]
plt.hist(data,bins=range(min(data),max(data)+500,500),color="skyblue",edgecolor="black")
plt.xlabel("Capital Losses")
plt.ylabel("Frequency")
plt.title("Histogram for CAPLOSS")
plt.show()

# DIVVAL
data=df["DIVVAL"]
plt.hist(data,bins=range(min(data),max(data)+10000,10000),color="skyblue",edgecolor="black")
plt.xlabel("Dividends from Stocks")
plt.ylabel("Frequency")
plt.title("Histogram for DIVVAL")
plt.show()

# MARSUPWT
data=df["MARSUPWT"]
plt.hist(data,bins=range(0,int(max(data)+1000),1000),color="skyblue",edgecolor="black")
plt.xlabel("Instance weight")
plt.ylabel("Frequency")
plt.title("Histogram for MARSUPWT")
plt.show()

# NOEMP
data=df["NOEMP"]
plt.hist(data,bins=range(min(data),max(data)+1,1),color="skyblue",edgecolor="black")
plt.xlabel("Num persons worked for employer")
plt.ylabel("Frequency")
plt.title("Histogram for NOEMP")
plt.show()

# WKSWORK
data=df["WKSWORK"]
plt.hist(data,bins=range(min(data),max(data)+10,10),color="skyblue",edgecolor="black")
plt.xlabel("Weeks worked in year")
plt.ylabel("Frequency")
plt.title("Histogram for WKSWORK")
plt.show()
