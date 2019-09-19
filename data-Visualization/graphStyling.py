# styling of graph using ggplot
# ggplot is a library which is used to style the grap using matplotlib

from matplotlib import pyplot as plt
from matplotlib import style


style.available  # style svailable in ggplot


# basic list example to show how ggplot used to style a graph

x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]


plt.title("GGPLOT Styling")
plt.ylabel('y-axis')
plt.xlabel('x-label')
plt.plot(x, y, 'green', label='line one', linewidth='5')
plt.plot(x2, y2, 'red', label='line two', linewidth='5')

plt.legend()
plt.grid(True, color='k')
plt.show()

# bargraph

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], color='red', label="Bargraph 1")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], color='green', label='Bargraph 2')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bargraph example')
# plt.grid(True, color='k')
plt.show()

# histogram


