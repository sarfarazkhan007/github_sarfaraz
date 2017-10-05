#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)
#print(x)

y1 = np.sin(x)
y2 = np.cos(x)
print(y2)

# Plot the sin and cos functions
plt.plot(x , y1, "-g", label="sine")
plt.plot(x , y2, "-b", label="cos")

# The legend should be in the top right corner
#plt.legend(loc="lower left")
plt.legend(loc="upper right")

# Limit the y axis to -1.5 to 1.5
plt.ylim(-2.5, 2.5)
plt.show()