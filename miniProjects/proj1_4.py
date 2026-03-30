import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

fix, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.ocean, s=10)

ax.set_title("cube numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("cube value", fontsize=14)

plt.show()