#!/usr/bin/env python

import sys

my_program = sys.argv[0]
my_args = sys.argv[1:]
my_len = len(my_args)

my_output = (f"I ran the program {my_program} with {my_len} arguments {my_args}")

print (my_output)
