n=int(input())
a=1
# print(1,end=' ')
b=1
# print(1,end=' ')
i=3
while i <= n:
    a,b=b,a+b
    i += 1
print(b, end=' ')


# Fibonacci numbers are the numbers in the integer sequence starting with 1, 1 where every number after the first two is the sum of the two preceding ones:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Given a positive integer n, print the nth Fibonacci number.
