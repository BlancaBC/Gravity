
#Problema N cuerpos

import math
import numpy as np
import matplotlib.pyplot as mlp

import RungeKutta

#definición de constantes
G=6.67*10**(-11) 
N=3  #número de cuerpos
m=np.array([10**20,2*10**20,3*10**20])
n = 25
#numero de pasos


r0_1=np.array([0, 0, 0])
r0_2=np.array([1000, 1000, 1000])
r0_3=np.array([5000, 5000, 5000])
V0_1=np.array([10,10,10])
V0_2=np.array([10,10,10])
V0_3=np.array([10,10,10])

r=np.matrix([r0_1,r0_2,r0_3])
V=np.matrix([V0_1,V0_2,V0_3])


    
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
U[0:3,0:3]=r
U[3:6,0:3]=V
U_euler = U
F=np.zeros((2*N,3))
F_euler = F
#print(U)

for i in range(n-1):
    Nbodies(N,U[0:3,0:3],U[3:6,0:3],F[0:3,0:3],F[3:6,0:3]) #Esto me permite obtener F

    Un = RungeKutta.Runge_Kutta_2_orden(n,F,U) #Me devuelve U en el siguiente paso
    U = Un
    
    Nbodies(N,U_euler[0:3,0:3],U_euler[3:6,0:3],F_euler[0:3,0:3],F_euler[3:6,0:3])
    
    U_euler = RungeKutta.Euler(n,F_euler,U_euler)
