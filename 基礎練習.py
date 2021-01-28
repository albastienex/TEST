print('Hello, World!')
num1=int(input('number 1:'))
num2=int(input('number 2:'))
num3=int(input('number 3:'))
print("the biggest number is:", max(num1, num2, num3))

account=str(input('type your account:'))
password=str(input('type your password'))
success=(account=="1234" and password=='4567')
print('登入成功', success)

a=int(input('a='))
b=int(input('b='))
print(a-b)

age=int(input("年齡:"))
heart_rate=(220-age)*0.7
print("有效運動心跳率為:"+str(heart_rate))
print('Have a nice day!')

n=input('say sorry')
while'sorry' not in n :
    n=input("say sorry")
print("It's OK")     