import pandas as pd

data= {
    "apples": [3, 4, 6, 9],
    "oranges": [1, 5, 6, 8]
}
purchases = pd.DataFrame(data)
print(purchases)
print(type(purchases))


#--------------------
index = ['Aaron', 'Lee', 'Steve', 'Shaun']
purchases=pd.DataFrame(
    data, index = index    
)
print(purchases)
print(type(purchases))

#want to extract the row of column

print(purchases["apples"]) #printing the apple column
print(purchases.loc["Aaron"])
