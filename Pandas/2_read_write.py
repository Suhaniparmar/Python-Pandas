import pandas as pd
file1 = pd.read_excel("dashboard.xlsx") 
print(file1)


print(file1.head(8))
print(file1.tail(5))
print(file1.dtypes)        # print datatypes of DataFrame/Series

file1.to_csv("file2.csv")
f2 = pd.read_csv("file2.csv")
print(f2.head())         #[5 rows x 12 columns]
print(f2.info())         # provide a technical info about DataFrame


# REMEMBER :
# Getting data in to pandas from many different file formats or data sources is supported by read_* functions.

# Exporting data out of pandas is provided by different to_*methods.

# The head/tail/info methods and the dtypes attribute are convenient for a first check.