import matplotlib.pyplot as plt 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values] 

fig, ax= plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#set chart title and label axes
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()