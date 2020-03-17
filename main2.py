'''
Alternative solution by using Sieve of Eratosthenes.
To read more about Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

import numpy as np

# Prepare array F for factorization
def arrayF(n):
    i = 2
    F = [0] * (n+1)
    while (i * i <= n):
        if F[i] == 0:
            k = i * i
            while (k <= n):
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F

# perform factorization on given integer
def factorization(x):
    F = arrayF(x)
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x //= F[x]
    primeFactors += [x]
    return primeFactors

def countingElements(A,n):
    count = [0] * (n+1)
    for e in A:
        count[e] += 1
    return count

# merge two lists of prime factor count
def filtering(A,B,k):
    PFC = [0] * (k+1)
    for i, e in enumerate(A):
        if B[i] > e:
            PFC[i] = B[i]
        else:
            PFC[i] = e
    return PFC

# finalize prime factors list 
def supersetlist(A):
    output = []
    for i, e in enumerate(A):
        if e:
            output += [i] * (e)
    return output

def solution(LCM,a,b):
    pf_a = factorization(a)
    pf_b = factorization(b)
    k = max(max(pf_a), max(pf_b)) # find the greatest value in the range of two prime factor lists
    pfc_a = countingElements(pf_a,k)
    pfc_b = countingElements(pf_b,k)
    pfc = filtering(pfc_a, pfc_b, k)
    superset = supersetlist(pfc)
    superset += [LCM // np.prod(superset)] # add the missing integer
    superset.sort()
    result = []
    n = len(superset)
    for i in range(n):
        j = i + 1
        while (j < n):
            value1 = np.prod(superset[i:j+1]) # product of slice 
            value2 = superset[i] * superset[j] # product of element i and element j
            if (value1 not in result) and (value1 != a) and (value1 != b):
                result += [value1]
            if (value2 not in result) and (value1 != a) and (value1 != b):
                result += [value2]
            j += 1
    result.sort()
    return result

def get_input(valid=True):
    while valid:
        num_1 = int(input("Enter number 1: "))
        num_2 = int(input("Enter number 2: "))
        num_lcm = int(input("Enter LCM: "))
        if (num_lcm % num_1 != 0) or (num_lcm % num_2 != 0):
            print ("The input value is invalid.")
        elif (type(num_1) is not int) or (type(num_2) is not int):
            print("Please enter an integer number.")
        else:
            break
    return num_lcm, num_1, num_2

while True:
    LCM, a, b = get_input()
    result = solution(LCM, a, b)
    print(f"Possible values of Num 3 are: {result}")