def poly_term_derivative(c: float, x: float, n: float) -> float:

    if n >= 2:
        return c * (n * x*(n-1))
    elif n == 1:
        return c * n 
    else:
        return c * n * x