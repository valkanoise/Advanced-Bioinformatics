'''In this exercise we create a list of prime numbers from a selected range of 
numbers. Additionaly we measure the required time for the process to occur.
'''

import time


def is_prime(number):
    ''''
    Function that receives a number and defines if it is a prime or not prime.
    Procedure:       
        - defines 1 as a non prime number
        - defines 2 and 3 as primer numbers
        - checks if the number can be divided by 2 or 3 without any remainder
    return: True if prime or False if not a prime
    '''
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True


def find_primes_in_range(start, end):
    '''
    Function that creates a range of numbers from start to end
    It iterates over every number in the range and calls the is_prime function.
    If is_prime function returns True the number is added to a list.
    Returns: a list with prime numbers
    '''
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start_range = int(input("Enter the start of the range (default=1): ") or "1")
end_range = int(input("Enter the end of the range: "))

# Lets measure the required time and print it
start = time.time()
prime_numbers = find_primes_in_range(start_range, end_range)
end = time.time()

print(f'Prime numbers in the specified range:{prime_numbers}')
print(f'Required time: {end - start}')




