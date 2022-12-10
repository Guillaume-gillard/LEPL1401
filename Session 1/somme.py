# Guillaume Gillard
# 05/10/2022

x = ... #the number
result = ... #store in this variable the sum of the x first positive integers

### Code to complete [START] ###

result = 0
for i in range(x+1):
    result = result + i

print(result)