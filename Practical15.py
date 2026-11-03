#                         //////////////////////////// Practical - 15 ////////////////////////////////
#                             /////////////////////////// Unification //////////////////////////
def unify(x,y):
    if x==y:
        return
    if x.islower():
        return {x,y}
    if y.islower():
        return{y,x}
    
    return None

print(unify('x','Ram'))
print(unify('A','A'))
print(unify('x','y'))