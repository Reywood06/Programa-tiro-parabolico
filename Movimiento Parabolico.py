import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtl
import matplotlib.animation as animation
from math import sqrt

xf = int(input('ingrese el valor en x en el que desea que caiga la pelota: '))
theta= np.pi/4
x0=0.
y0=0.
g=9.8
time = 5
t=np.linspace(0,time,50)

def velini(xf,g,theta):
    velocidad = sqrt((xf*g)/(np.sin(theta*2)))
    return velocidad

v0 = velini(xf,g,theta)

def x_pos(theta,t,v0,x0):
    x=x0+v0*np.cos(theta)*t
    return x

def y_pos(theta,t,v0,y0):
    y=y0+(v0*np.sin(theta)*t)-((g*t**2)/2)
    return y

x=x_pos(theta,t,v0,0)
y=y_pos(theta,t,v0,0)
N=len(t)

fig, ax=plt.subplots()
ln, = plt.plot(x,y,'ro')
ax.set_xlim(0,100)
ax.xaxis.set_major_locator(mtl.MultipleLocator(10))
ax.set_ylim(0,100)
ax.yaxis.set_major_locator(mtl.MultipleLocator(10))


def actualizar(i):
    ln.set_data(x[i],y[i])
    return ln,
ani = animation.FuncAnimation(fig,actualizar,range(N),interval=1, repeat = True)

plt.grid()
plt.show()