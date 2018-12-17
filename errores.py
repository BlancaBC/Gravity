from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

G = 1.0
m1=1.0
m2=0.001
mu=G*(m1+m2)
N=10000
DeltaT=1000/N
y0=[1.0, 0.0, 0.0, 1.2]
t=np.linspace(0.0, 1000.0, N)
t2=np.linspace(0.0, 1000.0, 2 * N)

#devuelve la derivada del vector de estado
def func(y,t):
    r=y[:2]
    v=y[2:]
    return [v[0], v[1], -mu*r[0]/norm(r)**3, -mu*r[1]/norm(r)**3]

# Integracion con 'odeint'                                                                                                 
solucion1=odeint(func, y0, t)
#r=solucion[:, :2]     # vector de posición                                                                      
#v=solucion[:, 2:]     # vector de velocidad   
U1=solucion1[N-1,:]
print(len(t2))

solucion2=odeint(func,y0,t2)
solucion3=solucion2[::2,:]
U2=solucion2[2*N-1,:]
print(U2)

E=np.zeros((N,4))
print(len(E))
E[:,:]=(solucion1-solucion3)/(1-0.5**4)

#plt.figure()
plt.plot(t,abs(E[:,0]))
#plt.show()
#graficos
#plt.figure()
#plt.plot(r[:,0],r[:,1])
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()
#plt.figure()
#plt.plot(r[:,0],v[:,0])
#plt.xlabel('x')
#plt.ylabel('v_x')
#plt.show()