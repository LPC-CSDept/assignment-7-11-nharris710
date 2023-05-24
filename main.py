import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.2
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
# Make your code
# ******************************
ax.bar(x-width*1.5,Math,width)
ax.bar(x-width*1.5,English,width)
ax.bar(x-width*1.5,Physics,width)
ax.bar(x-width*1.5,Computer,width)
ax.legend()
ax.set_title('Grouped graph for scores')
ax.bar_label(ax.continers[0])
ax.set_xticks(x - width)

fig.savefig('A11.png')
