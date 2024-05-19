import pandas as pd

file2 = pd.read_excel("dashboard.xlsx")

print(file2)

f2 = file2[["Reach","Posts"]]
print(type(f2))
print(f2.shape)   # shape & dtype are attribute ( no need to brackate)

high_reach = file2[file2["Reach"]>5000]
print(high_reach)

follower = file2[file2["Followers"].isin([20,21,22])]
# or
#follower =  file2[(file2["Followers"]==20) | (file2["Followers"]==21) | (file2["Followers"]==22)]
print(follower)