import pandas as pd

#defining a dataframe obj as df
df = pd.read_csv("dataset.csv")
print(df)
# print(df.head(5))
# print(df.tail(5))
df.info() 

print(df.describe()) #describes the dataset

print(df["Opposition"].describe())

# print(df)
# print(df["Runs"].value_counts())#frequency of each value => i.e from the col, finding all the unique values and finding their count of how many times those unique values occur

new_df = df[["Runs", "4s", "6s", "Opposition"]] #inside 3rd bracket put all those cols which u want to extract from the org data Frame => to create a new dataFrame
print(new_df)
# print(new_df.describe())
print(new_df.iloc[2])
print(new_df.iloc[2:4]["Runs"])#printing the "Runs" col from index 2 to 4
# print(df["Opposition"] == "v Australia")  
vs_aussies = df[df["Opposition"] == "v Australia"] #is returning a DataFrame
print(vs_aussies.head())

print(vs_aussies["Runs"].sum())
print(vs_aussies["6s"].sum())  #nos of 6s against aus 
centuries = vs_aussies[vs_aussies["Runs"] >= 100]
print(centuries)
