# Guillaume Gillard
# 06/10/2022

a = ... #variable to evaluate
b = ... #variable to evaluate
c = ... #variable to evaluate
minima = ... #store in this variable the smallest of the three variables

### Code to complete [START] ###

if a < b < c or a < c < b:
    minima = a
elif b < c < a or b < a < c:
    minima = b 
elif c < b < a or c < a < b :
    minima = c