import pandas as pd

data = {
    'City': ['Tokyo', 'Dubai', 'London', 'New York', 'Sydney'],
    'Temperature': [22, 42, 15, 28, 33],
    'Humidity': [55, 20, 75, 60, 85],
    'Rainfall': [120, 5, 60, 100, 210]
}

df = pd.DataFrame(data)

print(df["Temperature"].max())
print(df["Rainfall"].describe())
print(df[df["Temperature"] > 30])