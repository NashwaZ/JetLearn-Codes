import pandas as pd

#Creating a data frame
df = pd.DataFrame({
    "ID": [1,2,3,4,5],
    "Name": ['jack','john','jeff','jale','jen'],
    "Designation": ['admin','admin','PR','manager','admin'],
    "Department":['customer service','IT','IT','HR','Internal'],
})

print(df)