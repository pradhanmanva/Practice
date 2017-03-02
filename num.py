import math

#* Variable Description:
#* f			:	Given function
#* f_		:	Derivative of f
#* [a, b]	:	End point values
#* TOL		:	Tolerance
#* NMAX		:	Max number of iterations

def bisection(f, a, b, TOL=0.001, NMAX=100):
#Takes a function f, start values [a,b], tolerance value(optional) TOL and max number of iterations(optional) NMAX
# and returns the root of the equation using the bisection method.
    n = 1
    while n <= NMAX:
        c = (a + b) / 2.0
        if f(c) == 0 or (b - a) / 2.0 < TOL:
            return c
        else:
            n = n + 1
            if f(c) * f(a) > 0:
                a = c
            else:
                b = c
    return False

def newtonraphson(f, f_, x0, TOL=0.001, NMAX=100):
#Takes a function f, its derivative f_, initial value x0, tolerance value(optional) TOL and max number of iterations(optional) NMAX
#and returns the root of the equation using the newton-raphson method.
    n = 1
    while n <= NMAX:
        x1 = x0 - (f(x0) / f_(x0))
        if x1 - x0 < TOL:
            return x1
        else:
            x0 = x1
    return False

if __name__ == "__main__":
    def func(x):
        return math.pow(x, 3) - x - 2
    def func_(x):
        return 3 * math.pow(x, 2) - 1

    # Invoking Bisection Method
    res = bisection(func, 1, 2)
    print(res)
    # Invoking Newton Raphson Method
    res = newtonraphson(func, func_, 1)
    print(res)

print("Hey now!")
