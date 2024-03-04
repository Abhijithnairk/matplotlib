import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels=["apples","bananas","cherries","dates"]
colors = ["red","yellow","magenta","brown"]
plt.pie(y, labels=mylabels, startangle=90, colors=colors)
#plt.legend(title="FRUITS")
plt.show()