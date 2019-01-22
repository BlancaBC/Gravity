import numpy as np
import math
import matplotlib.pyplot as mlp

def Runge_Kutta_2_orden(n,F,U):

    paso_temporal = 1/n
    
    U = U + paso_temporal*0.5*(F + F*(U + paso_temporal*0.5))
        
    return U

def Euler(n,F,U):
    
    paso_temporal = 1/n
    
    U = U + paso_temporal*F
    return U


