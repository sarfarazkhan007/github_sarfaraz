#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile("salaries.txt", dtype=int, sep=",")

names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

#You can’t really plot the names on the x axis
x = np.arange(len(names))

#print(x)

plt.bar(x, salary)

#All it does it is replace the numbers in x with names. 
plt.xticks(x, names)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")
plt.show()

print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))



