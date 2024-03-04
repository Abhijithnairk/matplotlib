import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(4,2, figsize=(10,10))

#plot1
xpoints=np.array([0,6])
ypoints=np.array([0,250])
axs[0,0].plot(xpoints,ypoints)
axs[0,0].set_title("plot1")

#plot2
xpoints=np.array([1,8])
ypoints=np.array([3,10])
axs[3,0].plot(xpoints,ypoints,'o',color='red')
axs[3,0].set_title("plot2")

#plot3
xpoints=np.array([1,8])
ypoints=np.array([3,10])
axs[1,1].plot(xpoints,ypoints,color='red')
axs[1,1].set_title("plot3")

#plot4

ypoints=np.array([3,8,1,10,5,7])
axs[2,0].plot(ypoints,color='red')
axs[2,0].set_title("plot4")