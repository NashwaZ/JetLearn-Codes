import pandas as pd

titanic_df = pd.read_csv('titanic.csv')
print(titanic_df.head())
'''
#selecting specific column out of condition : loc
print(titanic_df.loc[titanic_df['Age'] > 18])
#selecting specific column out of a different column condition
print(titanic_df.loc[titanic_df['Age']>18,['Name']])
#printing specific number of rows and column
print(titanic_df.iloc[10:26,3:7])
#change a value of a specific column
titanic_df.loc[4,['Name']] = 'Billy Bobby Brown'
print(titanic_df.loc[4,'Name'])
#save dataframe as a csv file after modifying 
titanic_df.to_csv('titanic_df2.csv')
'''
'''#Creating a new column and filling it with values
titanic_df['Updated Fare'] = titanic_df['Fare'] * 2
print(titanic_df['Updated Fare'])
'''
#Renaming Column Names
new_df = titanic_df.rename(columns={'Siblings/Spouses Aboard':'Siblings/Spouses','Parents/Children Aboard': 'Parents/Children'})
print(new_df.info())

#Arthmetic operations on one or multiple columns
print(titanic_df['Age'].mean())
print(titanic_df[['Age','Fare']].mean())

#Group data by categories
#Grouping data by sex and calculating mean of age
data_by_sex = titanic_df[['Sex','Age']].groupby('Sex').mean()
print(data_by_sex)

#Mean ticket price for each sex and passenger class combined
data_by_class = titanic_df.groupby(['Sex','Pclass'])['Fare'].mean()
print(data_by_class)

#Counting no. of rows in each passenger category
data_no_class = titanic_df['Pclass'].value_counts()
print(data_no_class)

data_no_class2 = titanic_df.groupby('Pclass')['Pclass'].count()
print(data_no_class2)

print(titanic_df.sort_values(by='Age'))

#Operations on text data in a data frame
#Changing all names to lowercase
titanic_df['Lower'] = titanic_df['Name'].str.lower()
print(titanic_df['Lower'])

#In Lower field splitting the data 

'''splt = titanic_df['Lower'].str.split(",")
print(splt)'''
print(titanic_df['Name'].str.split(" "))
titanic_df['First Name'] = titanic_df['Name'].str.split(" ").str.get(1)
print(titanic_df['First Name'])
titanic_df['Last Name'] = titanic_df['Name'].str.split(" ").str.get(3)
print(titanic_df['Last Name'])