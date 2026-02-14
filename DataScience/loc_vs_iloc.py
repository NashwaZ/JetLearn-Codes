import pandas as pd

student_d = {
    'Name':['John','Jack','Jen','Andrew','Joy'],
    'Age' : [10,12,13,21,11],
    'Marks':[80,91,40,32,99]
}

df = pd.DataFrame(student_d)

#loc - label based selection - row index, column - names
#selecting a column
print(df.loc[0:,'Name'])

#selecting a row that has specific data
print(df.loc[2,])

#selecting specific number of rows and columns
print(df.loc[1:2,['Age','Marks']])

#labeling row numbers
df = pd.DataFrame(student_d,index = ['r1','r2','r3','r4','r5'])
print(df)
print(df.loc['r2':'r3',['Age','Name']])

#iloc - index based selection - 
#select a single row
print(df.iloc[2])
#select all rows + second column
print(df.iloc[:,2])
#specific set of rows and columns
print(df.iloc[0:2,1:])
