import numpy as np
import math
import matplotlib.pyplot as mlp

def Runge_Kutta_2_orden(paso_temp,F,U):
    
    U2 = U + paso_temp*0.5*F(U)
    U = U + paso_temp*0.5*(F(U) + F(U2))
        
    return U



















def Euler(n,F,U):
    
    paso_temporal = 1/n
    
    U = U + paso_temporal*F
    return U


