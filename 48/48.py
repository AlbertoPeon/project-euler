#! /usr/bin/env python3

# https://projecteuler.net/problem=48

print(str(sum((n ** n for n in range(1, 1001))))[-10:])
