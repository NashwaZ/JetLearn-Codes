import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
titanic_df = pd.read_csv('titanic.csv')
'''
x = np.arange(1,20,2)

#Line Plot
y = 2*x + 5
y1 = x^3 + 21

# Line types: g^ r-- b-- b- p- 
plt.plot(x,y,'ro',label = 'y = 2*x + 5')
plt.plot(x,y1,'g^',label = 'y = x^3 + 21')

plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()

#Bar Plot
x = ['p1','p2','p3','p4']
x = np.arange(len(x))
#x = np.arange(1,5)
y = [12,24,12,36]
y1 = [25,13,21,15]
width = 0.35

plt.bar(x-width/2 ,y, width, color='chocolate', label = 'group A')
plt.bar(x+width/2 ,y1, width, color='b', label = 'group B')

plt.title('Bar Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.show()'''

x = ['Male','Female']
y = titanic_df['Sex'].value_counts()
print(y.values)

