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

# scatter plot
# why to use scatter plot
# used to compare two variables or three if we are using three dimensions
# looking for a co-relation and groups we use scatter plot
# a1 and b1 must be of same size
# we are basically to find out how much two or three variables related to each other


a1 = [1, 2, 3, 4, 5, 6, 7, 8, 4, 10]
b1 = [5, 2, 4, 2, 1, 4, 5, 2, 4, 3]
plt.scatter(a1, b1, label='skitskat', color='green', s=25, marker='o')
plt.legend()
plt.title('scatter plot')


# piechart

slices_hours = [8, 2, 4, 6, 4]
activities = ['college', 'eat', 'Sleep', 'code', 'other']
colors = ['b', 'r', 'g', 'y', 'c']
plt.pie(slices_hours, labels=activities,
        colors=colors, startangle=90, autopct='%.1f%%')
plt.show()


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
