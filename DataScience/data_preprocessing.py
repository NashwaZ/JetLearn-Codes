import pandas as pd

data = {
"Age": [25, 30, None, 35, 40],
"Gender": [" Male ", "Female", "Female", " Male", None],
"Salary": [50000, 60000, 55000, None, 65000],
"Department": ["IT", "HR", "IT", "Finance", "HR"],
"Purchased": ["Yes", "No", "Yes", "No", "Yes"]
}


df = pd.DataFrame(data)
print(df)

#Data Cleaning

#Step 1 - Removing spaces ' '
for column in df.columns:
    #print(column)
    #print("*********")

    #Checking every column data type for string
    if df[column].dtype == "object":
        df[column] = df[column].str.strip() #strip() removes any space before or after in a string 
    
print(df)
        
#Step 2 - handling None (missing) values
df["Age"].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(0,inplace=True)
df['Gender'].fillna(df["Gender"].mode()[0],inplace=True)
print(df)
