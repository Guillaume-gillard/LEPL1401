# Guillaume Gillard
# 05/10/2022

s0 = ...    #Entier de départ

### Code to complete [START] ###

print(s0)
while True :
    if s0 == 1 :
        break
    elif s0 % 2 == 0 :
        s0 = s0//2
    else :
        s0 = 3*s0 + 1    
    print(s0)