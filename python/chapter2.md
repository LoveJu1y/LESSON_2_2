# 第二章
## 2.1
### 2.1.1 布尔类型
Boolean 类型，他只有两个内置对象，False和True
- bool() 函数，用于映射真假
- 测试结果为False:
   - **说明对象为None，0，False，或者空序列，控偶映射**...说明，万物都可以进行<font color=plum>真值测试</font>。
   - 对于用户自定义对象，类型定义了返回整数0或者布尔值False的方法_bool_(),或者_len_();需要有这两个函数，自己定义的数据类型才能用bool。

（此处老师插播了四种特殊类型，ppt）
### 2.1.2 逻辑运算
- 逻辑与 
  格式：x and y
- 逻辑或
  格式：x or y
- 逻辑非
  格式 not x

### 2.1.3 关系运算
- 大小比较
  注意可以连写就可以了
- is 与 not is
  这两判断的是本征值，类似于id，判断是否引用同一对象
  而==只判断值。
- in 与 not in
  只适用于序列

## 2.2
### 2.2.1 单路分支
 ```if condition :
     suite  #一些操作，suite中可以yo空语句**<font color=chocolate>pass</font>**不能什么都没有。
 ```
### 2.2.2 双路分支
```
if condition ：
    suite1
else 
    suite2
```
现在有一种简写形式
```python
expression1 if condition else expression2
#不过很明显的，它是类似于一个三目表达式的，expression并不需要像suite一样，例如
VALUE =1
VALUE = VALUE * 3 + 1 if VALUE %2 else VALUE //2
# express并不是一个完整的句子。
```
### 2.2.3 多路分支
```python
if condition1:
    suite1
elif continude2:
    suite2
else 
    pass
```
## 2.3 循环结构
### 2.3.1
- for循环
```python
for target_list in expression_list :
    suite
for char in "bat" :
    print(char,"666")
for idx in range(1,11) :#,半开半闭区间[1,11)

#range()函数的使用，也是经常使用的
```
- range（）函数
  ```python
  range(1,1):#[]
  range(1,6,2):#[1,3,5]
  range(-1,-3,-1):#[-1,-2]
  ```

### 2.3.4
  for 循环扩展
  ```python
  for target in expression:
    suitefor
  else:
    suite

  while expression:
    suite
  else:
    suite

  ```
  加了一个else，当出现了中止异常迭代或者正常结束是，就执行一遍else。他最大的目的是为了在正常循环后加一个额外操作，其实本质上是为了好看。

  ### 2.3.5循环嵌套
  理论上可以无限嵌套。
  ```python
  for idx in range(3,16):
    print(idx,end=': ')
    value = idx
    while value != 1:
        value =value*3 +1 if value % 2 else value // 2
        print(value,end=' ')
    else:
        print(6)
  ```
  则可以再记一下if的简单写法；

  ### 2.3.6循环终止
break语句：
终止最内层循环，外层循环照常执行，**<font color=plum>如果执行break循环终止了，那么后边的else不执行。</font>**

continue语句：跳过当前迭代，到下一步迭代，循环并不退出。**<font color=plum>continue语句不影响else语句的执行</font>**。

使用break可以用于无限循环的终止。

## 2.4 **异常处理****（重点）**

- 异常(exception) 定义：
  程序中的例外、不正常的情况。并不一定是错误（很大概率是），将异常当做意外情况、小概率情况更好。而错误，
- 异常处理逻辑
  - 存在异常处理程序
  - 异常能够被引发
    这一异常按照约定（出现了这个情况）引发，**<font color=plum>python自动构造该类异常的一个对象，填充必要信息，在引发异常是抛出。</font>**
  - 异常能够被捕获
- 异常处理语句
``` python
try:
  suite_try
finally:
  suite_fin
```
无论出现何种情况，最后都执行fianlly
**说明** ：finally主要是为了防止程序崩溃开辟空间没有释放，资源被占。比如打开的文件即使崩溃都得正确关闭。
```python
try:
    print(1/0)
finally:
    print("oops")
    #触发zerodivisionerror，无论该异常有没有被处理，确保输出oops。
```
**也就是说，上面并没有捕获异常并处理**
- 异常的捕获：异常处理语句2
```python
try:
  suite_try
except exception_type_1 as exception_object_1:#exception_type_1表示异常类型，可以不写，则认为是所有异常，而as相当于赋值命名，可以后语句块中简单写操作。
  suite_exc_1
...#可以有很多这样的except，相当于匹配异常；
else:
  suite_els
finally:
  suite_fin
```
**总结：try-except是最重要的！finally和else可以不需要。**

- 具体？
python中的异常是有一个库的，全部异常的根类是BaseException，而类Exception是我们需要使用的类，（比如我们需要写一个异常类，需要从这个Exception来继承，然后再往下构造）
```python
try:
    print(1/0)
except ZeroDivisionError as e:
    print(type(e))
    print(str(e))
finally:
    print("666")
```
```python
try:
    print(1/0)
except (eroDivisionError,NameError) as e:
    print("not good")
    
finally:
    print("666")
```
下面这个例子是用的类


### 2.4.4 异常的引发
```python
raise[except[from exception_object]]
raise RuntimeError("something no-good happend")
```
抛出异常对象except或者构造并抛出异常类except的异常对象。
这是抛出了异常，我们没有自己写接受的，所以是python自己的traceback收到。
```python
try:
    raise RuntimeError("999")
except RuntimeError as e:
    print(str(e))
    raise
#最后再引发上边的异常，相当于给上级报告，（虽然自己的except已经处理过了）
```

### 输出一点补充
```python
 for num1 in range(1,10):
    for num in range(1,num1+1):
        num2 = num * num1
        print('{0:2} * {1:<2} = {2:<2}' .format(num1, num, num2),end='  ')
    print('\n',end='')
 ```
 这种输出可以控制输出的位宽等


