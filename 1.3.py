import math
def factorial(a) :
    b=1
    while a > 0 :
        b*=a
        a-=1
    return b

flag = 1
while flag:
    try:
        a = int(input ('please give me a int number:'))
        b = int( input ('please give me another number :'))
      #  print('the sum of these two numbers factoral is :',math.factorial(a) + math.factorial(b))
        print('the sum of these two numbers factoral is :',factorial(a) + factorial(b))#两种方法
        flag = 0
    except :
        print("are you sure these are int numbers?please re_input these two numbers")

