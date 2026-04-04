import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,30,35,40]

subjects = ['math','english','chemistry','PE']
marks = [90,76,32,100]

figure, axis = plt.subplots(2,2,figsize=(12,12)) 

#Line Plot
axis[0,0].plot(x,y, marker='o')
axis[0,0].legend()
axis[0,0].set_title('Line Plot')

#Bar Graph
axis[0,1].bar(subjects, marks)
axis[0,1].legend()
axis[0,1].set_title('Bar Graph')

#Pie Chart
axis[1,0].pie(marks,labels=subjects)
axis[1,0].legend()
axis[1,0].set_title('Pie Chart')

#Scatter Plot
axis[1,1].scatter(x,y, marker='*')
axis[1,1].legend()
axis[1,1].set_title('Scatter Plot')

plt.show()
