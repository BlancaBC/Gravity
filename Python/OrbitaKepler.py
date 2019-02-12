from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

#Definición de constantes
G=1.0
m1=1
m2=1
mu=G*(m1+m2)
N=10000
DeltaT=1000/N
t=np.linspace(0.0,1000.0,N)

#Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.2]

#devuelve la derivada del vector de estado
def func(y,t):
    r=y[:2]
    v=y[2:]
    return [v[0], v[1], -mu*r[0]/norm(r)**3, -mu*r[1]/norm(r)**3]

# Integracion con 'odeint'                                                                                                 
solucion=odeint(func,y0,t)
r=solucion[:, :2]     # vector de posición                                                                      
v=solucion[:, 2:]     # vector de velocidad   

#graficos
plt.figure()
plt.plot(r[:,0],r[:,1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Órbita Kepleriana')
plt.show()
plt.figure()
plt.plot(r[:,0],v[:,0])
plt.xlabel('x')
plt.ylabel('v_x')
plt.title('Velocidad orbital')
plt.show()
plt.figure()
plt.plot(r[:,1],v[:,1])
plt.xlabel('y')
plt.ylabel('v_y')
plt.title('Velocidad orbital')
plt.show()
