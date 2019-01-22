import numpy as np
import math
import matplotlib.pyplot as mlp
from scipy.integrate import odeint

#Paso temporal
numPasos=10000
step=20*math.pi/numPasos

# Matriz inversa B
A=np.matrix([[0,1],[-1,0]])

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
    Un=A*np.matrix([[U[2*i,0]],[U[2*i+1,0]]])
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


mlp.plot(range(100),X[:100])
mlp.title("Óscilador")
mlp.xlabel("t")
mlp.ylabel("X(t)")
mlp.grid()
mlp.show()