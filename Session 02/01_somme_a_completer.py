some_value = ...

### code to complete [START] ###

n = some_value
sum = 0
count = 0
for numb in range(1, 20000):
    if count == n :
        break
    elif numb % 2 == 0:
        sum += numb
        count += 1