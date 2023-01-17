i = ...    # the number to check (i >= 1)
temp = ... # "fizz", "buzz", "fizzbuzz" or "no" depending on i's value

### Code to complete [START] ###

if i % 3 == 0 and i % 5 == 0:
    temp = "fizzbuzz"
elif i % 3 == 0:
    temp = "fizz"
elif i % 5 == 0:
    temp = "buzz"
else :
    temp = "no"