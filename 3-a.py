a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)


#Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) or 0 (if all numbers are different).