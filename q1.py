
def iterative_approximation_exponential(a, b, epsilon=0.001, delta=0.0001, max_iterations=100000):
    # Don't change this line
    assert a > 0 and a != 1 and b > 0, "Invalid input: a must be > 0 and not equal to 1, b must be > 0"

    x = 0.0
    
    for i in range(max_iterations):
        current_value = a ** x
        
        if abs(current_value - b) < epsilon:
            return x
        
        x += delta
        
        
    print("Solution not found within max iterations")
    return None