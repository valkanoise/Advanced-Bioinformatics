import time
import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

def find_primes_unoptimized():
    start_range = int(input("Enter the start of the range (default=2): ") or "2")
    end_range = int(input("Enter the end of the range: "))
    prime_numbers = find_primes_in_range(start_range, end_range)
    return prime_numbers 

def sieve_of_eratosthenes(limit):
    prime_flags = [True] * (limit + 1)
    prime_flags[0] = prime_flags[1] = False
    
    for num in range(2, int(limit**0.5) + 1):
        if prime_flags[num]:
            for multiple in range(num*num, limit + 1, num):
                prime_flags[multiple] = False
                
    primes = [num for num, is_prime in enumerate(prime_flags) if is_prime]
    return primes


print("--- PRIME NUMBERS APP ---")
print("What do you want to do?")
print("1- Find prime numbers from a range of values")
print("2- Visualize a Graph comparing two algorythms")
option = int(input("Your choice: "))

if option == 1:
    print(find_primes_unoptimized())
elif option == 2:
    print()
    print("Unoptimized and optimized algorythms will be show using 5 ranges from 2-100000\nplease wait...")
    ranges = [round(x) for x in np.linspace(2,100000,5)]
    times_unopt = []
    times_opt = []
    for r in ranges:
        start_unopt = time.time()
        find_primes_in_range(2, r)
        end_unopto = time.time()
        times_unopt.append(end_unopto-start_unopt)
        start_opt = time.time()
        sieve_of_eratosthenes(r)
        end_opto = time.time()
        times_opt.append(end_opto-start_opt)
        

    plt.figure()
    plt.plot(ranges, times_unopt, marker='o', label='Unoptimized')
    plt.plot(ranges, times_opt, marker='x', label='Sieve of Erastosthenes')
    plt.title('PRIME NUMBERS ALGORYTHMS\n Range size vs Time')
    plt.xlabel('Range size')
    plt.ylabel('Computing time (s)')
    plt.legend()
    plt.show()

else:
    print("Wrong choice!")



