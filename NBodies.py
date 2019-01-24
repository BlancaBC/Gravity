#Problema N cuerpos

import math
import numpy as np
import matplotlib.pyplot as mlp

#definición de constantes
G=6.67*10**(-11) 
N=3  #número de cuerpos

class Body:
    def __init__(self,Mass, Position, Velocity):
        self.m=Mass
        self.r=Position
        self.v=Velocity

Earth=Body(10**20,[0,0,0],[10,10,10])
Moon=Body(10**20,[1000, 1000, 1000],[10,10,10])
Satellite=Body(10**20,[5000, 5000, 5000],[10,10,10])
m=[Earth.m,Moon.m,Satellite.m]

r0=np.matrix([Earth.r,Moon.r,Satellite.r])
V0=np.matrix([Earth.v,Moon.v,Satellite.v])

def Nbodies (N,r,V,drdt,dvdt):
    a=np.array([0,0,0])
    for i in range(N):
        for j in range(N):
            if j!=i:
                d=r[j,:]-r[i,:]
                a[:]=a[:]+G*m[j]*d/(abs(d))**3
        drdt[i,:]=V[i,:]
        dvdt[i,:]=a[:]

U=np.zeros((2*N,3))
U[0:3,0:3]=r0
U[3:6,0:3]=V0
F=np.zeros((2*N,3))
Nbodies (N,U[0:3,0:3],U[3:6,0:3],F[0:3,0:3],F[3:6,0:3])