# Fourier_series
fourier_series.py is an animation to visualize the Fourier series approximation of the function using python 3.
![Example animation](https://github.com/Bra-A-Ket/Fourier_series/blob/main/fourier-exp.gif)
## Required packages
1. Numpy:
```bash
python -m pip install numpy
```
2. matplotlib:
```bash
python -m pip install matplotlib
```
3. tqdm
```bash
python -m pip install tqdm
```
## Usage
- Choose the function for which the fourier series should be performed
- Choose the upper limit of the interval (the lower limit is 0)
- Choose the maximal order of the series
- Choose the time step and axis leghts for the plotting

```python
f = lambda t: np.exp(-t)
T = 2*np.pi
M = 10
dt = 0.01
tmin = 0 - dt
tmax = T + dt
ymin = 0 - dt
ymax = 1 + dt
```
The python script fourier_series.py has to be executed in the main directory like
```bash
python -m fourier_series
```
## How it works
The basic idea is to perform the non-complex fourier series. Therefore the coefficients  
![fourier](https://miro.medium.com/max/875/0*gFnaliohbO3vh3ok)  
are needed and will be calculated numerically by evalutation the integrals with the implementet monte carlo method.
For discret point in the inverval [0,T] (step size dt) the fourier series of the order M will be plotted and finally animated.
