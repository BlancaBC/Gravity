
# resolución oscilador armónico
# Usando euler inverso para la integración

import numpy as np
import math
import matplotlib.pyplot as mlp
from scipy.integrate import odeint

#Paso temporal
numPasos=1000
step=20*math.pi/numPasos

#M Matriz inversa B
B=(1/(1+step**2))*np.matrix([[1,step],[-step,1]])

# Definición de vectores y condiciones iniciales
U=np.zeros((2*numPasos,1))
X=np.zeros((numPasos,1))
V=np.zeros((numPasos,1))
U[0,0]=1
U[1,0]=0
X[0,0]=1
V[0,0]=0

# Integrador de Euler inverso
for i in range(numPasos-1):
    Un=B*np.matrix([[U[2*i,0]],[U[2*i+1,0]]])
    U[2*i+2,0]=Un[0,0]
    X[i+1]=Un[0,0]
    U[2*i+3,0]=Un[1,0]
    V[i+1]=Un[1,0]

#Gráficas de resultados
mlp.plot(X,V)
mlp.title("Órbita")
mlp.xlabel("X(t)")
mlp.ylabel("V(t)")
mlp.grid()
mlp.show()


mlp.plot(range(numPasos),X)
mlp.title("Óscilador")
mlp.xlabel("t")
mlp.ylabel("X(t)")
mlp.grid()
mlp.show()


