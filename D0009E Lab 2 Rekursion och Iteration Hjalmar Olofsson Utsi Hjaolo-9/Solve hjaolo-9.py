import math

def f(x):
    return x**2-1

def derivative(f, x, h):
    return (1.0/(2*h))*(f(x+h)-f(x-h))

def solve(f, x0, h):
    x = 0
    while True:
        x=x0 - (f(x0)/derivative(f , x0, h))
        if abs(x0-x) < h:
            return x
        x0 = x

print(solve(f, -5, 0.0001))
