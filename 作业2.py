# def sum_(n:int)->int:
#     sum=0
#     while 1:
#         sum = 0
#         while 1:
#             tmp = n % 10
#             n = n // 10
#             sum += tmp
#             if(n==0):
#                 break
#         if(sum>9):
#             n = sum
#         else :
#             break
#     return sum





# #第二题
# def sum_1_9():
#     n = [0 for idx in range(9)] 
#     for n0 in range (1,100000):
#         sum = sum_(n0)
#         n[sum-1] += 1
#     print(n)   
#     return n

# ret = sum_1_9()
# for idx in range(9):
#     print (ret[idx]/99999,end=' ')    
# #可以看出实际上比例都是相同的九分之一

#第三题
def C(n:int,k:int)->int:
    if(k==0):
        return 1
    if(k==1):
        return n
    if(n==k):
        return 1
    
    return C(n-1,k-1)+C(n-1,k)

print(C(6,3))


#第四题
import random
i = int(input("please input how many times you want to sycle \n"))
n = 0
count_pi = 0
while n<i:
    random.seed()
    x = random.random()
    y = random.random()
    if(x * x + y * y < 1) :
        count_pi += 1
    n += 1

print(4 * count_pi / n)


