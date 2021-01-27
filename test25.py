for i in range(1,20):
    if i ==5:      #若i==5則略過不印
        continue
    print(i, end=' ')
    if i ==10:    #若i==10就跳出迴圈
        break
print('end')

s='agkhwe;kgketkh'
for i in s:
    if i == 'k':   #如果找到k
        print("found") 