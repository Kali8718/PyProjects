import matplotlib.pyplot as plt
from fill_walk_class import RandomWalk

rw = RandomWalk(5_000)
rw.fill_walk()

plt.style.use('classic')
fix, ax = plt.subplots(figsize = (15, 9))

ax.plot(rw.x_values, rw.y_values, linewidth=3)





plt.show()


