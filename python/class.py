#_*_coding:<UTF-8>_*_
import math
print(1)
a = 1 + 3
b=4
print(id(a))

print(id(b))
print(1.1 is 1.1)
print(0.1 + 0.1 + 0.1 - 0.3)

c=1.52
d=666

print((1.23+2.33j).imag,int(c))


dd=[1,2,3]
print(math.fsum(dd))


ddd="aaa"
print('he sum is %s'%ddd)


VALUE =1
VALUE = VALUE * 3 + 1 if VALUE %2 else VALUE //2

##clollatz



try:
    print(1/0)
finally:
    print("oops")

for idx in range(3,16):
    print(idx,end=': ')
    value = idx
    while value != 1:
        value =value*3 +1 if value % 2 else value // 2
        print(value,end=' ')
    else:
        print(6)

try:
    print(1/0)
except :
    print(6)
finally:
    print("666")

print(66666)


try:
    raise RuntimeError("999")
except RuntimeError as e:
    print("what?")
    raise
finally:
    print("5555")