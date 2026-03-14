import matplotlib.pyplot as plt
import pandas as pd

titanic_df = pd.read_csv('titanic.csv')

grouped = titanic_df.groupby(['Sex', 'Survived']).size()

male_survived = grouped['male', 1]
male_casualty = grouped['male', 0]

female_survived = grouped['female', 1]
female_casualty = grouped['female', 0]

x = ['Survived', 'Did Not Survive']
y = [male_survived, male_casualty]
width = 0.5

plt.bar(x, y, width, color='teal')

plt.title('Male Survival rate on Titanic')
plt.xlabel('Outcome')
plt.ylabel('Number')

plt.show()

x = ['Survived', 'Did Not Survive']
y = [female_survived, female_casualty]
width = 0.5

plt.bar(x, y, width, color='lightsalmon')

plt.title('Female Survival on Titanic')
plt.xlabel('Outcome')
plt.ylabel('Number')


plt.show()