# Fourier_series
fourier_series.py is an animation to visualize the Fourier series approximation of the function using python 3.
## Required packages
1. Numpy:
```bash
python -m pip install numpy
```
2. matplotlib:
```bash
python -m pip install matplotlib
```
## Usage
Markup : - Choose the function for which the fourier series should be performed
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