"""Alternative solution by using Sieve of Eratosthenes.
To read more about Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

import numpy as np

# List of smallest prime divisors of all non-primes for factorization
def smallest_prime_divisor(n):
    i = 2
    prime_divisors = [0] * (n + 1)
    while i * i <= n:
        if prime_divisors[i] == 0:
            k = i * i
            while k <= n:
                if prime_divisors[k] == 0:
                    prime_divisors[k] = i
                k += i
        i += 1
    return prime_divisors


def factorization(x):
    prime_divisors = smallest_prime_divisor(x)
    prime_factors = []
    while prime_divisors[x] > 0:
        prime_factors += [prime_divisors[x]]
        x //= prime_divisors[x]
    prime_factors += [x]
    return prime_factors


def counting_elements(A, k):
    elements_count = [0] * (k + 1)
    for e in A:
        elements_count[e] += 1
    return elements_count


# Merge two lists of prime factor count, retain the higher count
def filtering_prime_factor_count(A, B, k):
    prime_factor_count = [0] * (k + 1)
    for i, e in enumerate(A):
        if B[i] > e:
            prime_factor_count[i] = B[i]
        else:
            prime_factor_count[i] = e
    return prime_factor_count


# Finalize prime factors list
def supersetlist(A):
    prime_factors_superset = []
    for i, e in enumerate(A):
        if e is not None:
            prime_factors_superset += [i] * (e)
    return prime_factors_superset


def solution(num_lcm, num_1, num_2):
    prime_factors_1 = factorization(num_1)
    prime_factors_2 = factorization(num_2)
    range_of_prime = max(
        max(prime_factors_1), max(prime_factors_2)
    )  # Find the greatest value among two prime factor lists

    prime_factors_count_1 = counting_elements(prime_factors_1, range_of_prime)
    prime_factors_count_2 = counting_elements(prime_factors_2, range_of_prime)
    filtered_prime_factors_count = filtering_prime_factor_count(
        prime_factors_count_1, prime_factors_count_2, range_of_prime
    )

    superset_prime_factors = supersetlist(filtered_prime_factors_count)
    superset_prime_factors += [
        num_lcm // np.prod(superset_prime_factors)
    ]  # add the missing integer
    
    result = []
    result += [superset_prime_factors[-1]]
    n = len(superset_prime_factors)

    for i in range(n):
        j = i + 1
        while j < n:
            value1 = np.prod(superset_prime_factors[i : j + 1])  # product of slice
            value2 = (
                superset_prime_factors[i] * superset_prime_factors[j]
            )  # product of element i and element j
            if (value1 not in result) and (value1 != num_1) and (value1 != num_2):
                result += [value1]
            if (value2 not in result) and (value1 != num_1) and (value1 != num_2):
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
            print("The input value is invalid.")
        elif (type(num_1) is not int) or (type(num_2) is not int):
            print("Please enter an integer number.")
        else:
            valid = False
    return num_lcm, num_1, num_2


while True:
    num_lcm, num_1, num_2 = get_input()
    possible_values = solution(num_lcm, num_1, num_2)
    print(f"Possible values of Num 3 are: {possible_values}")
