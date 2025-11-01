def polynomial(x):
    # Don't change this!
    return 3 * x ** 2 - 4 * x - 5

def bisection_root(a, b, epsilon=0.0001):
    assert b > a, 'Invalid range'
    assert polynomial(a) * polynomial(b) < 0, 'The bisection method cannot be applied'
    
    # Implement here