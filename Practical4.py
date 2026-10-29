#                                 /////////////////////////// Practical -04 ////////////////////////////////

#                                    //////////////////////// Practical -4.1 ////////////////////////////
# List
def mylist():
    return [1, 2, 3, 4, 5]


# Get Head and Tail
def mylist_ht(L):
    if len(L) == 0:
        return None, []
    return L[0], L[1:]


# Get Tail
def mylist_t(L):
    return L[1:]


# Get Head
def mylist_h(L):
    if len(L) == 0:
        return None
    return L[0]


# Search an element
def search(X):
    L = mylist()
    return X in L


# Find length
def mylength():
    L = mylist()
    return len(L)


# Function calls
L = mylist()

print("List:", L)
print("Head and Tail:", mylist_ht(L))
print("Tail:", mylist_t(L))
print("Head:", mylist_h(L))
print("Search 3:", search(3))
print("Length:", mylength())
 
 
#                                  //////////////////////// Practical -4.2 ////////////////////////////


# Original list
def mylist():
    return [1, 2, 3, 4, 5]


# Append two lists
def myappend(L1, L2):
    return L1 + L2


# Insert an element at the 3rd position
def insert_3rd(X, L):
    if len(L) < 2:
        return "List must contain at least 2 elements"
    return L[:2] + [X] + L[2:]


# Reverse a list using recursion
def rev_list(L):
    if L == []:
        return []
    return rev_list(L[1:]) + [L[0]]


# Function calls
L = mylist()

print("Original List:", L)
print("Append:", myappend(L, [6, 7]))
print("Insert 10 at 3rd position:", insert_3rd(10, L))
print("Reversed List:", rev_list(L))
