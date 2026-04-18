import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


data = {
"Age": [25, 30, None, 35, 40],
"Gender": [" Male ", "Female", "Female", " Male", None],
"Salary": [5000, 60000, 55000, None, 650000],
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

#Step 3 - Encoding assigning text-based data a no. 
#Categorical Encoding
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
print(df.head())

df['Purchased'] = le.fit_transform(df['Purchased'])
print(df.head())

#One Hot Encoding
df = pd.get_dummies(df, columns=['Department'])
print(df)

#Step 4 - Feature Scaling bringing all values to the same scale
st = StandardScaler()
df[['Age','Salary']] = st.fit_transform(df[['Age','Salary']])
print(df)

#Step 5 - Removing Outliers Quantile
q1 = df['Salary'].quantile(0.25)
q3 = df['Salary'].quantile(0.75)
qr = q3-q1
df = df[(df['Salary']>= q1-1.5*qr)&(df['Salary']<=q3+1.5*qr)]
print(df)

#Step 6 - Feature Selection

df.drop()


