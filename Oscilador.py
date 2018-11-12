
# resolución oscilador armónico

import numpy as np
import math
import matplotlib.pyplot as mlp

numPasos=1000
step=20*math.pi/numPasos

#B=inv(I-step·A)
B=(1/(1+step**2))*np.matrix([[1,step],[-step,1]])
U=np.zeros((2*numPasos,1))
X=np.zeros((numPasos,1))
V=np.zeros((numPasos,1))
U[0,0]=1
U[1,0]=0
X[0,0]=1
V[0,0]=0

for i in range(numPasos-1):
    Un=B*np.matrix([[U[2*i,0]],[U[2*i+1,0]]])
    U[2*i+2,0]=Un[0,0]
    X[i+1]=Un[0,0]
    U[2*i+3,0]=Un[1,0]
    V[i+1]=Un[1,0]

Dist=math.sqrt(U[2*numPasos-1,0]**2+U[2*numPasos-2,0]**2)
print(Dist)
mlp.plot(X,V)
mlp.title("Órbita")
mlp.xlabel("X(t)")
mlp.ylabel("V(t)")
mlp.grid()
mlp.show()

