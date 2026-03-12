def polynomial(x):
    # Don't change this!
    return 3 * x ** 2 - 4 * x - 5






def bisection_root(a, b, epsilon=0.0001):
    assert b > a, 'Invalid range'
    assert polynomial(a) * polynomial(b) < 0, 'The bisection method cannot be applied'
    
    
    
    
    
    
    
    
def polynomial(x):
    return 3 * x ** 2 - 4 * x - 5

def bisection_root(a, b, epsilon=0.0001):
    assert b > a, 'Invalid range'
    assert polynomial(a) * polynomial(b) < 0, 'The bisection method cannot be applied'
    for i in range(1000):
        m = (a + b) / 2
        
        if abs(polynomial(m)) < epsilon:
            return m

        if polynomial(a) * polynomial(m) < 0:
            b = m
        else:
            a = m
            
    return (a + b) / 2 


