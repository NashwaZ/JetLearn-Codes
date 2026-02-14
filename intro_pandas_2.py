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