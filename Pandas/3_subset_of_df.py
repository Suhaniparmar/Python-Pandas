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

no_NaN = file3[file3["Interaction"].notna()]
print("\n Not NaN interactions are here\n")
print(no_NaN)
print(no_NaN.shape)

high_reach = file3.loc[file3["Reach"]>5000,"Date"]
print(high_reach)
print(high_reach.shape)

print(file3.iloc[5:10, 2:5])

# REMEMBER :
# When selecting subsets of data, square brackets [] are used.

# Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.

# Select specific rows and/or columns using loc when using the row and column names.

# Select specific rows and/or columns using iloc when using the positions in the table.

# You can assign new values to a selection based on loc/iloc.