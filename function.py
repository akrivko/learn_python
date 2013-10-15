#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

x = [1,2,3]
y = 2
print (x == y) # Prints out True
print (x is y)

primes = [2,3,5,7]
for prime in primes:
    print (prime)

    # Prints out the numbers 0,1,2,3,4
for x in range(5):
    print (x)

# Prints out 3,4,5
for x in range(3,6):
    print (x)

numb=[1,2,3]
print(len(numb))


def my_function():
    print ("Hello From My Function!")

my_function()


def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(2, 4))

import urllib
print(dir(urllib))

for n in range(10):
	print(n)
	