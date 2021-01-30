m=int(input())
d=int(input())

if m==2 and d==28:
    print(m+1)
    print(1)
elif d==31:
    print(m+1)
    print(1)
elif m==12 and (d==31):
    print(1)
    print(1)
elif m==4 or 6 or 9 or 11 and (d==30):
    print(m+1)
    print(1)
else:
    print(m)
    print(d+1)

undone 

# Given a month (an integer from 1 to 12) and a day in it (an integer from 1 to 31) in the year 2017, print the month and the day of the next day to it.