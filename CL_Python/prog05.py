#!/usr/bin/env python

import sys

my_program = sys.argv[0]
my_args = sys.argv[1:]
my_len = len(my_args)

my_output = (f"I ran the program {my_program} with {my_len} arguments {my_args}")

print(my_output)
print('\n')

if (my_len != 2):
    print("Error: two arguments required.")
    exit(0)

my_a = float(sys.argv[1])
my_b = float(sys.argv[2])
my_answer = my_a + my_b

my_sum = (f"The sum of {my_a} and {my_b} is {my_answer}")

print(my_sum)
print('\n')
