import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20,20)


m = int(input("Enter your m value: "))
c = int(input("Enter your c value: "))
y = m*x + c


m1 = int(input("Enter your second m value: "))
c1= int(input("Enter your second c value: "))
y1 = m1*x + c1


a = int(input("Enter your a value: "))
b = int(input("Enter your b value: "))
c2 = int(input("Enter your c value: "))
y2 = a*x**2 + b*x + c2

plt.style.use('Solarize_Light2')
plt.plot(x,y, color = 'b',label = f'y = {m}x + {c}')
plt.plot(x,y1, color = 'g', label = f'y = {m1}x + {c1}')
plt.plot(x,y2, color = 'brown', label = f'y = {a}x^2 + {b}x + {c2}')


plt.axhline(0)  
plt.axvline(0)  
plt.grid(True)

plt.legend()
plt.show()

