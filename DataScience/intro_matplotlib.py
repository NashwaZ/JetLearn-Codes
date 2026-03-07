import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

titanic_df = pd.read_csv('titanic.csv')

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

'''#Bar Plot
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

subjects = ['math','science','english','history','PE']
marks = [90,87,43,21,46]
width = 0.5
c = plt.cm.viridis(range(len(marks)))
plt.bar(subjects, marks, width, color=c, linewidth=3 ) #alpha=0.5  edgecolor='red'
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title("Grades")
plt.show()


#Pie Chart
activities = ['football','reading','sleeping','writing','walking']
hours = [3,2,15,1,1]
plt.pie(hours,labels=activities,colors=['blue','red','green','yellow','purple'],startangle=90,explode=[0,1,0,0,0],shadow=1)
plt.title('Activities')
plt.show()

#Scatter Plot
width = [21,24,43,51,32,12,15,11,87,34]
height = [150,160,177,190,145,212,45,21,54,32]
plt.scatter(width,height,s=50, edgecolors='pink', alpha=0.75, marker='*')
plt.xlabel('Width (cm)')
plt.ylabel('Height (cm)')
plt.title('Width/Height')
plt.show()

#Using CSV data to plot a bar graph
x = ['Male','Female']
y = titanic_df['Sex'].value_counts()
print(y.values)

plt.bar(x ,y, width, color='slateblue')

plt.title('Bar Plot')
plt.xlabel('Gender')
plt.ylabel('Number')
plt.legend()

plt.show()
