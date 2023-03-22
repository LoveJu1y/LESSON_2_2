#_*_coding:<UTF-8>_*_
# import math
# print(1)
# a = 1 + 3
# b=4
# print(id(a))

# print(id(b))
# print(1.1 is 1.1)
# print(0.1 + 0.1 + 0.1 - 0.3)

# c=1.52
# d=666

# print((1.23+2.33j).imag,int(c))


# dd=[1,2,3]
# print(math.fsum(dd))


# ddd="aaa"
# print('he sum is %s'%ddd)


# VALUE =1
# VALUE = VALUE * 3 + 1 if VALUE %2 else VALUE //2

# ##clollatz



# try:
#     print(1/0)
# finally:
#     print("oops")

# for idx in range(3,16):
#     print(idx,end=': ')
#     value = idx
#     while value != 1:
#         value =value*3 +1 if value % 2 else value // 2
#         print(value,end=' ')
#     else:
#         print(6)

# try:
#     print(1/0)
# except :
#     print(6)
# finally:
#     print("666")

# print(66666)


# try:
#     raise RuntimeError("999")
# except RuntimeError as e:
#     print("what?")
#     raise
# finally:
#     print("5555")

# #第二次作业
# #水仙花数

# for num in range(100,1000):
#     a = num // 100
#     b = num % 100 // 10
#     c = num % 10 
#     if a**3 + b**3+ c**3 == num:
#         print(num,end=',')

#投资

# seed_money = eval(input('please input seed money \n'))
# now = seed_money
# #对题目理解有点误区 理解1：每年利率递增，是1%，2%...
# for year in range(0,30):
#     interest = (year + 1) / 100 + 1 
#     seed_money *= interest 
# print("if the interest rate is inceresing by 1% ,finally you will get ",seed_money,", the total interest reate is ",seed_money / now -1,"\n \n")


# #第二种理解，三十年的利率都一样
# seed_money = now 
# for num in range (0,30):
#     interest = (num + 1) / 100 +1 
#     print("if the interest rate in 30 years = %f " %(interest -1)) #在这种%%转义怎么报错呢..
#     seed_money *= interest **30 
#     print('finally you will get %f'%seed_money,end='\n \n')


# # 乘法表
# for num1 in range(1,10):
#     for num in range(1,num1+1):
#         num2 = num * num1
#         print('{0:2} * {1:<2} = {2:<2}' .format(num1, num, num2),end='  ')
#     print('\n',end='')

#平均值：
sum = 0
idx = 0
while True:
    try :
        a = eval(input("please input a number: \n")) 
        if a == 0:
            print('you have stop this process ')
            break
        sum += a
        idx += 1
    except Exception :
        print("you sure this is a number ? please do rewrite it")
        
if idx == 0:
    print('the average is 0' )
else:
    print('the average is %f' %(sum/idx))
