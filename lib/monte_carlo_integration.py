"""
    Numerical integration using the monte carlo method
    <f> = 1/(b-a) * int(from a to b of f(x) dx)
    where <f> indicates the average of the function in the interval [a,b]
    Inputs:
        - f: function which will be integrated
          syntax: f = lambda x: f(x)
        - N: int - number of support points to approximate the average of the
          function f in the interval [a,b]
        - a: float - lower integration limit
        - b: float - upper integration limit
        - dx: step-size
"""

def moca_int(f, N, a, b, dx=None):
    if dx == None:
        dx = 1/N
    else:
        dx = dx

    f_list = []
    x = a
    while x <= b:
        f_list.append(f(x))
        x += dx

    average = sum(f_list) / (len((f_list)))
    integral = (b-a) * average

    return integral
