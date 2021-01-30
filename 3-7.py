a=int(input())

if a//1000 == a%10 and a%1000//100 == a%100//10:
    print('YES')
else:
    print('NO')


# Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise. 