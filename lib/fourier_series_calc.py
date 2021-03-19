"""
    This function calculats the coefficients ai and bi of the non-complex
    Fourier series
    f(x)= a0/2 + sum(from i=0 to M of ai[i]*cos(2*pi*i*x/T) + bi[i]*sin(2*pi*i*x/T))
    with ai = <f(x),cos(2*pi*i*x/T)> and bi = <f(x),sin(2*pi*i*x/T)>.
    In a discret interval t the values of the above sum are calculated and
    returned as a result.
    Inputs:
        - f: function for Fourier series.
          syntax: f = lambda t: f(t)
        - T: float - period duration
        - M: int - maximal order of the Fourier series
        - dt: float - time-step of the calculation
    Used functions:
        - moca_int(f, N, a, b)
          Numerical integration using the monte carlo method
          (See 'lib/monte_carlo_integration.py')
"""

#imports
import numpy as np
from lib.monte_carlo_integration import *

#functions
def real_fourier(f, T, M, dt):
    """
        Relle Fourier Reihe
        f: Funktion, lambda x: f(x)
        T: Periode [0,T]
        M: Ordnung
    """

    nu = 1/T #frequency
    a0 = (2/T) * moca_int(f=f, N=1000, a=0, b=T) #coefficient a0
    an = [] #list of ai coefficients
    bn = [] #list of bi coefficients
    for i in range(1, M+1): #append the coefficients in the above lists
        ai_func = lambda x: f(x)*np.cos(2*np.pi*i*nu*x)
        bi_func = lambda x: f(x)*np.sin(2*np.pi*i*nu*x)
        an.append( (2/T) * moca_int(f=ai_func, N=1000, a=0, b=T) )
        bn.append( (2/T) * moca_int(f=bi_func, N=1000, a=0, b=T) )

    result = []

    t = np.arange(0, T, dt) #discret values for which the Fourier series is calculated

    for x in t:
        func = a0/2
        for i in range(1, M+1):
            func += an[i-1]*np.cos(2*np.pi*i*nu*x)+bn[i-1]*np.sin(2*np.pi*i*nu*x)
        result.append(func)

    return result
