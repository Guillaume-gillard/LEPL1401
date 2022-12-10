# Guillaume Gillard
# 07/10/2022

a = ... #variable to evaluate
b = ... #variable to evaluate
rest = ... #store in this variable the remainder of the division a/b

### Code to complete [START] ###

div = 0
rest = None

while rest == None and b != 0:   
    div = int(a/b)
    print(div)
    if div * b != a :
        rest = a - div * b
    else :
        rest = 0

print(rest)