import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5)
y1 = 2*x + 1
y2 = x**2 - 5
y3 = 0.5*x**3 - 7*x
plt.plot(x,y1,label="y1")
plt.plot(x,y2,label="y2")
plt.plot(x,y3,label="y3")
plt.legend()
plt.xlabel("x", size=13)
plt.ylabel("y", size=13)
plt.grid()
plt.show()