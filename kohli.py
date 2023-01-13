import pandas as pd

#defining a dataframe obj as df
df=pd.read_csv("dataset.csv")
print(df)
      
# print(df.head(10))

# print(df.tail(10))

#df.info()   #it is giving all info of dataset

#print(df.shape)
print(df.describe()) #describes the dataset

print(df["Opposition"].describe())   #ye against top teans and nos of freqency dega

print(df)
print(df["Runs"].value_counts())   #ye against us team ka show karega jiske against max time play kiya hai i.e srilanka

#create a new dataset contaains ball faced, runs and opposition
#create a new data fram for runs, ball faced and opposyion
new_df = df[["Runs", "4s", "6s", "Opposition"]]

print(new_df)  #ye new extracted data set show karega
#print(new_df.describe())    #ye pura details dega new dataset

# #i want to extract 2nd row from dataset
# print(new_df.iloc[2])
# print(new_df.iloc[2:5])   #3 row extract kiye
# #---------
# print(new_df.iloc[2:13]["Runs"])

#print(new_df.iloc[2:13]["6s"])

print(df["Opposition"] == "v Australia")
vs_aussies=df[df["Opposition"] == "v Australia"]
print(vs_aussies.head(10))

#find total nos. of runs scored against virat

print(vs_aussies["6s"].sum())  #nos of 6s against aus 

#nos. of century against australia
vs_aussies_century=df[(df["Opposition"] == "v Australia") & (df["Runs"] >= 100)]  
print(vs_aussies_century)
#or
centuries=vs_aussies[vs_aussies["Runs"] >= 100]
print(centuries.head(10))

#function create kar and if century aa gya then "OG" else "NOOB"
def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"

#if century aayega then ek new col add "century" 
df["Centuries"] = df["Runs"].apply(find_centuries)
print(df)