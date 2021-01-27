n=int(input())
m=int(input())
a =[['.']*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2!=0:  #i+j為奇數
            a[i][j]='*'
for row in a:
    print(*row)
