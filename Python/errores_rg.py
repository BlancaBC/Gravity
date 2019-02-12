from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
from Integradores import Runge_Kutta_2_orden, Euler
#Definición de constantes
G = 1.0
m1=1.0
m2=0.001
mu=G*(m1+m2)
N=10000

t=np.linspace(0.0, 1000.0, N)
t2=np.linspace(0.0, 1000.0, 2 * N)

step1 = t[2] - t[1]
step2 = t2[2]-t[1]

#Orden del integrador
orden = 2
#Condiciones iniciales
y0=[1.0, 0.0, 0.0, 1.2]

#devuelve la derivada del vector de estado
def func(y):
    r=y[:2]
    v=y[2:]
    F = np.array([v[0], v[1], -mu*r[0]/norm(r)**3, -mu*r[1]/norm(r)**3])
    return F

#Condiciones uniciales para lo solución1
    
U = (y0)
F = func(y0)

#Matriz con los resultados

Utotal1 = np.zeros((N,4)) #Dimensiones de t
Utotal1[0,0:4] = U

#Itengración con el primer step

for i in range(1,N): #Dimensiones de t
    U = Runge_Kutta_2_orden(step1,func,U)
    Utotal1[i,0:4] = U

sol1 = Utotal1 
#Condiciones iniciales para la solucion1
    
U = (y0)
F = func(y0)
Utotal2 = np.zeros((2*N,4)) #dimensiones de t2
Utotal2[0,0:4] = U

#Itengración con el segundo step

for i in range(1,2*N): #dimensiones de t2
    U = Runge_Kutta_2_orden(step2,func,U)
    Utotal2[i,0:4] = U
    
#Para comparar la sol1 con la sol2, necesito cada 2 elememtos
sol2 = Utotal2[::2,:]

#Error mediante Richardson
E=np.zeros((N,4))
E[:,:]=(sol1-sol2)/(1-0.5**orden)

#Gráficas de resultados
plt.figure()
plt.plot(t,abs(E[:,0]))
plt.show()
