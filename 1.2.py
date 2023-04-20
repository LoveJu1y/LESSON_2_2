#现实生活中，储户在填定期存单时有“到期自动转存”选项，它表示在存单期满后自动转存为同样存期的新定期存单，结存的本金与利息总额将作为新本金。计算自动转存一次和两次后的期满金额。

while 1:
    try:
        ini = float(input('please put in ben_jin:'))#本金
        li_lv = float(input('please put in li_lv:'))/100#利率
        count = 2 
        while count > 0:#用来计算两次到期自动存储最终的钱
            ini *=pow((1+li_lv),count)
            count -= 1
            print(2 - count,' ，finialy you will get ',ini,'yuan')#打印两次，分别是第一第二次自存的收入
        break
    except:
        print("are you sure these are int numbers?please re_input these two numbers")



