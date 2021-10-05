a = 1
b = 1
c = 0
fibonacci_sequence = [a,b]
while c <= 1000000:
    c = a + b
    fibonacci_sequence.append(c)
    a = b
    b = c
    continue

def fibonacci_iterative(x):
    return fibonacci_sequence[(x-1)]

fibonacci_iterative(3)