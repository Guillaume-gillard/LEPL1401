# Guillaume Gillard
# 14/10/2022 


### Code to complete [START] ###


def fibonacci(n):
    f0 = 0
    f1 = 1
    if n == 0 :
        return(0)
    elif n == 1 :
        return(1)
    else :
        fn_1 = 0
        fn_2 = 1
        for i in range(n):
            fn = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn
            
        return(fn)