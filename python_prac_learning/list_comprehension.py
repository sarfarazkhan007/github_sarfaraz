#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

x = [5,10,15,20,25]

# declare y as an empty list
y = []



for counter in x:
   y.append(counter / 5)

print("\nOld fashioned way: x = {} y = {} \n".format(x, y))


# Easy method
z = [n/5 for n in x]
print("List Comprehensions: x = {} z = {} \n".format(x, z))

# not allowed but allowed in numpy array
try:
    a = x / 5
except:
    print("No, you can't do that with regular Python lists\n")

# easy method NUMPY array
a = np.array(x)
b = a / 5

print("With Numpy: a = {} b = {} \n".format(a, b))

# Create x, evenly spaced between 0 to 20
x = np.linspace(0, 20, 10)
print(x)

y1 = np.sin(x)
y2 = np.cos(x)
	
	
# Plot the sin and cos functions
plt.plot(x , y1, "-g", label="sine")
plt.plot(x , y2, "-b", label="cos")

# The legend should be in the top right corner
plt.legend(loc="upper right")
























