# Import the required packages 
import matplotlib.pyplot as plt
import numpy as np

# Generate the data
x = np.arange(0, 500, 0.5)
y = np.arange(0,1000, 1)

# Generate the figure and the axes
fig, axs = plt.subplots(nrows=1, ncols=1)

# On the first axis, plot the sine and label the ordinate 
axs.plot(x,y)
axs.set_ylabel('Test')

# Display the resulting plot 
plt.show()