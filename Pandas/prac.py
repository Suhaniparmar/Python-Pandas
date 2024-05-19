import pandas as pd

file2 = pd.read_excel("dashboard.xlsx")

print(file2)

f2 = file2[["Reach","Posts"]]
print(type(f2))
print(f2.shape)   # shape & dtype are attribute ( no need to brackate)

high_reach = file2[file2["Reach"]>5000]
print(high_reach)