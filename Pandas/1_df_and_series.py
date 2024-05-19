import pandas as pd
df = pd.DataFrame(
    {
        "Name" : [
            "Suhani Parmar",
            "Nirav Parmar",
            "Pragati Tank",
            "Sheel Tank"
        ],
        "Age" : [19,15,16,14],
        "Gender" : ["Female","Male","Female","Male"],
    }
)

print(df)         #print dataframe
print(df["Age"])


new_age = pd.Series([20,16,17,15],name="Age")   #create new series only
print(new_age)

print(df["Age"].max())
print(new_age.sum())
print(df.describe())