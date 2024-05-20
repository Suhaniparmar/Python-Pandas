import pandas as pd

# Reading the Excel file
file3 = pd.read_excel("C:\\Users\\Suhani\\Desktop\\git\\Python-Pandas\\Pandas\\dashboard.xlsx")
print(file3)

# Selecting specific columns
f3 = file3[["Checkout", "Sessions"]]
print(type(f3))
print(f3.shape)  # shape and dtype are attributes (no need for parentheses)

# Filtering rows based on "Sessions" column value
high_reach = file3[file3["Sessions"] > 500]
print(high_reach)

# Filtering rows based on "Checkout" column values
follower = file3[file3["Checkout"].isin([6, 9])]
print(follower)

# Uncomment and use this if you want to filter based on "Followers" column
# follower =  file3[(file3["Followers"]==20) | (file3["Followers"]==21) | (file3["Followers"]==22)]
# print(follower)
