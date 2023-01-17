### Code to complete [START] ###

def is_prime(i, prime_number):
    for x in prime_number:
        if i%x == 0:
            return False
    return True


def primes(max):
    prime_number = []
    for i in range(2, max+1):
        if is_prime(i, prime_number):
            prime_number.append(i)
    return prime_number