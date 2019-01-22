from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

#Definición de constantes
G = 1.0
m1=1.0
m2=0.001
mu=G*(m1+m2)
N=10000
DeltaT=1000/N
t=np.linspace(0.0, 1000.0, N)
t2=np.linspace(0.0, 1000.0, 2 * N)

#Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.2]

#devuelve la derivada del vector de estado
def func(y,t):
    r=y[:2]
    v=y[2:]
    return [v[0], v[1], -mu*r[0]/norm(r)**3, -mu*r[1]/norm(r)**3]

# Integracion con 'odeint'                                                                                                 
solucion1=odeint(func, y0, t)
U1=solucion1[N-1,:]
print(U1)

solucion2=odeint(func,y0,t2)
solucion3=solucion2[::2,:]
U2=solucion2[2*N-1,:]
print(U2)

#Error mediante Richardson
E=np.zeros((N,4))
E[:,:]=(solucion1-solucion3)/(1-0.5**4)

#Gráficas de resultados
plt.figure()
plt.plot(t,abs(E[:,0]))
plt.show()
