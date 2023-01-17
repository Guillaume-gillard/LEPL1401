a = ... #variable to evaluate
b = ... #variable to evaluate
c = ... #variable to evaluate
median = ... #store in this variable the median of the three variables

### Code to complete [START] ###

if a < b < c or c < b < a :
    median = b
elif c < a < b or b < a < c :
    median = a
elif a < c < b or b < c < a :
    median = c