#接受两个数，一个为用户一年期定期存款本金，一个为一年期定期存款利率。计算一年期满后本金与利息总额。说明：（1）存款金额以人民币元为单位；（2）输入利率时不需要输入百分号，例如一年期定期存款年利率为2.52%，用户输入 2.52 即可。

while 1:
    try:
        ini = float(input('please put in ben_jin:'))#本金
        li_lv = float(input('please put in li_lv:'))/100#利率
        print('finialy you will get ',ini * (1+li_lv),'yuan')#打印两次，分别是第一第二次自存的收入
        break
    except:
        print("are you sure these are int numbers?please re_input these two numbers")