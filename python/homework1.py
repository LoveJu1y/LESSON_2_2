import math

ini = float(input('please put in benjin:'))#本金
li_lv = float(input('please put in li lv:'))/100#利率
i = 0
now = ini
while i<12 :#默认12个月
    ini += li_lv*ini
    i += 1
print('finialy you will get ',ini,'yuan')


