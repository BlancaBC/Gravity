# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:24:27 2019

@author: igna9
"""

import numpy as np
import math
import matplotlib.pyplot as mlp
from scipy.integrate import odeint
import RungeKutta as Rg

#Definición del paso de integración 
numPasos=10000
step=20*math.pi/numPasos

#Condiciones iniciales
X0=1
V0=0

def oscilador(U):
    A = np.matrix([[0,1],[-1,0]])
    F = A * U
    return F

U = np.array([[X0],[V0]])
F = oscilador(U)
Utotal = np.zeros((numPasos*2,1))
X = np.zeros((numPasos,1))
V = np.zeros((numPasos,))
Utotal[0:2] = U

    
for i in range(numPasos):
        
    U = Rg.Runge_Kutta_2_orden(step,oscilador,U)
    Utotal[i*2:i*2+2] = U
    
    X[i] = Utotal[i*2]
    V[i] = Utotal[i*2+1]

mlp.plot(X,V)
mlp.title("Órbita")
mlp.xlabel("X(t)")
mlp.ylabel("V(t)")
mlp.grid()
mlp.show()
