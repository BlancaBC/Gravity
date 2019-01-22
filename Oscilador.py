import numpy as np
import math
import matplotlib.pyplot as mlp
from scipy.integrate import odeint

#Oscilador armónico 
#odeint como integrador

#Definición del paso de integración 
numPasos=10000
step=20*math.pi/numPasos

#Condiciones iniciales
X0=1
V0=0

#Integrador odeint
def func(y,t):
    r=y[0]
    v=y[1]
    return [v, -r]

y0=[X0,V0]
t=np.linspace(0.0,1000.0,numPasos)
U=odeint(func,y0,t)

#Gráficas de resultados
mlp.plot(t[:500],U[:500,0])
mlp.title("Óscilador")
mlp.xlabel("t")
mlp.ylabel("X(t)")
mlp.grid()
mlp.show()

mlp.plot(U[:500,0],U[:500,1])
mlp.title("Órbita")
mlp.xlabel("X(t)")
mlp.ylabel("V(t)")
mlp.grid()
mlp.show()
