import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 31)
steps = np.random.randint(0,20000,30)

figure, axis = plt.subplots(1,2,figsize=(10,5))

#Line Plot
axis[0].plot(days,steps, label='Daily Steps')
axis[0].legend()
axis[0].set_title('Daily Steps')
print('The average number of steps this month was: ',np.average(steps))

#Scatter Graph
axis[1].scatter(days, steps, color=['limegreen' if steps > 10000 else 'gray' for steps in steps], label='Above 10k')
axis[1].legend()
axis[1].set_title('Days over 10k steps')

plt.show()
