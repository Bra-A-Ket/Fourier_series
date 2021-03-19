"""
    Little animation which aminates a Fourier series for a given function.
    Inputs:
        - f: function for Fourier series.
          syntax: f = lambda t: f(t)
        - T: float - period duration
        - M: int - maximal order of the Fourier series
        - dt: float - time-step of the calculation
        - tmin: float - start of the time domain for plotting (axis)
        - tmax: float - end of the time domain for plotting (axis)
        - ymin: float - start of the y domain for plotting (axis)
        - ymax: float - end of the y domain for plotting (axis)
    How it works:
        - Calculating the Fourier series for the discret values in t with
          'lib/fourier_series_calc.py'
        - The in 'lib/fourier_series_calc.py' defined function 'real_fourier'
          returns a list of the y-values for the discret values in t
        - via 'matplotlib' the result is plotted and animated
    Used fuctions:
        - real_fourier(f, T, M, dt)
          Calculation of the Fourier series (See 'lib/fourier_series_calc.py')
"""

#imports
from lib.imports import *

#user inputs
f = lambda t: np.exp(-t)
T = 2*np.pi
M = 10
dt = 0.01
tmin = 0 - dt
tmax = T + dt
ymin = 0 - dt
ymax = 1 + dt

#plotting and animation
t = np.arange(0, T, dt) #discret values for which the Fourier series is calculated

fig = plt.figure()
frames = []
m = range(1, M+1) #list of orders

for i in range(M):
    fourier = real_fourier(f=f, T=T, M=m[i], dt=dt) #calculating Fourier points
    plt.plot(t, f(t), '-.', color='r') #plotting the input function f
    frames.append(plt.plot(t, fourier, 'b'))
    plt.grid(True)
    plt.axis([tmin, tmax, ymin, ymax])
    print("image added for M = " + str(m[i]))

ani = animation.ArtistAnimation(fig, frames, interval=80, blit=True, repeat_delay=1000)
plt.title("Animation: Fourier-series")
plt.xlabel("t")
plt.ylabel("y")
ani.save('Fourier.gif')
plt.show()
