#                          ///////////////////////////////// Practicle -03 //////////////////////////////////


# 1. Print series from 1 to 10
def series(N):
    if N < 11:
        print(N)
        series(N + 1)


# 2. Factorial using recursion
def fact(N):
    if N == 0:
        return 1
    elif N > 0:
        return N * fact(N - 1)
    else:
        return "Invalid input"


# 3. Fibonacci using recursion
def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N > 1:
        return fib(N - 1) + fib(N - 2)
    else:
        return "Invalid input"


# Function calls
print("Series:")
series(1)

print("Factorial:", fact(5))

print("Fibonacci:", fib(7))
