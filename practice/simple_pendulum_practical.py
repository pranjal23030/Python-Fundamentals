import numpy
import pylab

# Data points in the format (length, time)
data = [
    (0, 0),
    (21, 0.9),
    (31, 1.32),
    (41, 1.69),
    (51, 2.1),
    (61, 2.56),
    (71, 3.06),
    (81, 3.61),
    (91, 4.2),
    (101, 4.85),
    (111, 5.52)
]

# Lists to store x (length) and y (time) data
x_data = []
y_data = []

# Separate length and time data into respective lists
for length, time in data:
    x_data.append(length)
    y_data.append(time)

# Plot the data
pylab.plot(x_data, y_data)

# Set the title and labels for the plot
pylab.title('Graph of Length vs Time')
pylab.xlabel('Length')
pylab.ylabel('Time')

# Display the plot
pylab.show()