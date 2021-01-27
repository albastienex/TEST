drinks=['coffee', 'tea', 'wine']
enumerate_drinks=enumerate(drinks)
lst=list(enumerate_drinks)
print("轉成串列輸出,初始索引值是0 =", lst)
print(type(lst[0]))

numbers1=(1,2,3,4,5)
fruits=('apple', 'orange')
mixed=('James', 50)
val_tuple=(10,)
print(numbers1[0])
print(fruits[1])
print(mixed[0])
print(val_tuple)

keys=('magic','xaab',9099)
for s in keys:
    print(s)

fruits=('apple', 'orange')
print(fruits[1])

fruits=('apple', 'orange')
for a in fruits:
    print(a)
print(*fruits)

f=('alex','bastien','cody','david','frank')
print(f[:3:2])

keys=('magic','xaab',9099)
print(len(keys))
