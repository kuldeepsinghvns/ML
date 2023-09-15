import matplotlib.pyplot as plt
import numpy as np

x = [32, 33, 34, 36, 35, 33, 32, 30]
y = [9, 10, 11, 12, 13, 14, 15, 16]
# y = [x*x for x in x][::-1]
plt.title("Last week temprature")
plt.ylabel("Temprature")
plt.xlabel("DATE")
plt.grid(True)
# plt.scatter(x,y)
plt.plot(y, x, color='red', linestyle='-', linewidth=2)
plt.scatter(y,x)
plt.savefig("tem.png")
plt.show()

