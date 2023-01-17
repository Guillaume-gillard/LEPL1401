n = ...    #Borne supérieure

### code to complete [START] ###

for i in range(1, n+1):
    count = 0
    for div in range(1, i+1):
        if div != i and i % div == 0:
            count += 1
    print(i, ":", count)
    