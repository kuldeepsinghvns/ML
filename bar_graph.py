import matplotlib.pyplot as plt
import numpy as np

x = [32, 33, 34, 36, 35, 26, 32, 27]
y = [9, 10, 11, 12, 13, 14, 15, 16]
# y = [x*x for x in x][::-1]
plt.title("Last week temprature")
plt.ylabel("Temprature")
plt.xlabel("DATE")
# plt.grid(True)
plt.bar(y,x, color='green', alpha=0.5, edgecolor='black')
plt.scatter(y,x)
plt.legend(['Temp', 'Date'])
plt.errorbar(y,x, color='blue', alpha=0.5)
plt.savefig("bar_graph.png")
plt.show()