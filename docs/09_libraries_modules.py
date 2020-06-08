# Import og Sinus kurve plot
import math as math
import matplotlib.pyplot as plt

# Data for plot
x_axis = range(0, 2000)
x_axis = [x / 100 for x in x_axis]
y_axis = [math.sin(x) for x in x_axis]

plot, ax = plt.subplots()
ax.plot(x_axis, y_axis)
ax.set(xlabel='x (radians)', ylabel='sin(x)',
       title='Sinus kurve')
ax.grid()

plot.savefig("sinus_kurve.png")
plt.show()

