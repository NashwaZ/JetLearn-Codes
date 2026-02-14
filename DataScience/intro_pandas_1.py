import pandas as pd
'''
#Creating a data frame
df = pd.DataFrame({
    "ID": [11,34,98,4,21],
    "Name": ['jack','john','jeff','jale','jen'],
    "Designation": ['admin','admin','PR','manager','admin'],
    "Department":['customer service','','IT','HR','Internal'],
})

print(df)
#Printing a selected no. of rows
print(df.head())
#Accessing a specific column
print(df["Name"])
print(df['ID'].max())
#How to find no. of rows & columns
print(df.shape)
#Find column details : numerical details - count, mean, standard deviation, min, 25%, 50%, 75%, max
print(df.describe())
#Summary of a data frame
print(df.info())
'''
#Loading titanic.csv file
titanic_df = pd.read_csv('titanic.csv')
print(titanic_df.head())
print(titanic_df.shape)
print(titanic_df.info())
print(titanic_df['Name'])
#Accesssing more than 1 column
print(titanic_df[['Name','Pclass']])
print(titanic_df.describe())

#Printing details of people of age greater than 35 - row filtering
greater_35 = titanic_df[titanic_df['Age'] >= 35]
print(greater_35)