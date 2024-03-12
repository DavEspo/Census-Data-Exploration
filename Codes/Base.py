import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

columns_abbr = ['AAGE', 'ACLSWKR', 'ADTIND', 'ADTOCC', 'AHGA', 'AHRSPAY', 'AHSCOL', 'AMARITL', 'AMJIND', 'AMJOCC',
                'ARACE', 'AREORGN', 'ASEX', 'AUNMEM', 'AUNTYPE', 'AWKSTAT', 'CAPGAIN', 'CAPLOSS', 'DIVVAL', 
                'FILESTAT', 'GRINREG', 'GRINST', 'HHDFMX', 'HHDREL', 'MARSUPWT', 'MIGMTR1', 'MIGMTR3', 'MIGMTR4', 
                'MIGSAME', 'MIGSUN', 'NOEMP', 'PARENT', 'PEFNTVTY', 'PEMNTVTY', 'PENATVTY', 'PRCITSHP', 'SEOTR', 
                'VETQVA', 'VETYN', 'WKSWORK', 'YEAR', 'PTOTVALB']

# you can read from the compressed file
df = pd.read_csv('census-income.zip', compression='zip', names=columns_abbr, sep=r',', skipinitialspace=True)
df.head()

# you can also unzip census-income.zip and read using the following
# df = pd.read_csv('census-income.csv', names=columns_abbr, sep=r',', skipinitialspace=True)
# df.head()

# you can see the DataFrame's info panel here
df.info()
