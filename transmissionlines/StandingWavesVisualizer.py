""" Standing Waves Visualizer Python 3.11 , matplotlib , numpy 
Ramel E. Recentes La Salle University 
Blue = incident waves Green = reflected waves Red = standing waves 
Note: Update the values of Vi and Vr inside the function 'animate' See lines 33 and 35 """ 

""" run:  %matplotlib qt or %matplotlib qt5""" 

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

#Initialize 
pi=np.pi 
fig = plt.figure() 
ax = plt.axes(xlim=(0, 2*pi), ylim=(-2, 2)) 
t = np.linspace(0, 2*pi, 1000)

line1, = ax.plot(t, np.sin(6*t),color='b') 
line2, = ax.plot(t, np.sin(6*t),color='g') 
line, = ax.plot(t, np.sin(6*t),color='r') 

# Init only required for blitting to give a clean slate. 

def init(): 
    line1.set_ydata(np.ma.array(t, mask=True)) 
    line2.set_ydata(np.ma.array(t, mask=True)) 
    line.set_ydata(np.ma.array(t, mask=True)) 
    return line1,line2,line 

def animate(phi): 
    #incident voltage 
    Vi=1
    #reflected voltage
    Vr=1 
    y1=Vi*np.sin(6*t - phi/10.0) 
    y2=Vr*np.sin(6*t + phi/10.0) 
    y=y1+y2 
    line1.set_ydata(y1) 
    line2.set_ydata(y2) 
    line.set_ydata(y) 
    return line1,line2,line 

ani = animation.FuncAnimation(fig, animate,init_func=init,frames=500,interval=50, blit=True) 
plt.show()
