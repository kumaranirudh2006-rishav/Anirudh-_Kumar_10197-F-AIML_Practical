#                                   /////////////////////////// Practical - 01 ///////////////////////
# Arithmetic Functions in Python

def add(A, B):
    R = A + B
    return R

def sub(A, B):
    S = A - B
    return S

def mul(A, B):
    M = A * B
    return M

def div(A, B):
    if B == 0:
        return "Division by zero is not allowed"
    D = A / B
    return D


# Function calls
print("Addition:", add(1, 2))
print("Subtraction:", sub(5, 2))
print("Multiplication:", mul(3, 4))
print("Division:", div(10, 2))
