import pandas as pd

file3 = pd.read_csv("C:\\Users\\Suhani\\Desktop\\git\\Python-Pandas\\Pandas\\file2.csv")
print(file3)



f3 = file3[["Reach","Posts"]]
print(type(f3))
print(f3.shape)   # shape & dtype are attribute ( no need to brackate)

high_reach = file3[file3["Reach"]>5000]
print(high_reach)

follower = file3[file3["Interaction"].isin([6,9])]
# or
#follower =  file3[(file3["Followers"]==20) | (file3["Followers"]==21) | (file3["Followers"]==22)]
print(follower)