# 函数
通过接口，与外界通信，传递信息。
- ```function_name([paramter_list])```他的参数传递形式是怎么样的？
它实际上是 **“对象共享”**
- 函数返回值：如果没有返回值，就会自动返回 **none**
- 基本调用逻辑
  他只能调用解释器已经知道的函数；

### 3.13 内置函数
- ```all(iterable)```
  如果iterable全部元素为ture，则为true
- ```any(iterable)```
  iterable某个true，则为true。
- ``` callable(object)```
  若 **object** 可以被调用，则返回true。
- ```chr(i)```
  返回整数i表示的unicode字符对用的字符串
  - ord函数时它的逆运算
- ```eval()函数似乎没有什么印象```（指表达式求值）
- ```map(function,iterable)```
  类似于c++中的，将function作用到iterable的每个元素上。
- ```repr(object)```
  返回object的可打印字符串表示。

## 3.2
### 3.2.1
- 函数调用实例
```python
def fib(n):
    a,b = 0,1
    while a < n:
        print(a, end = ' ')
        a , b =b ,a + b
        print()
fib(6)
```
- 函数定义时允许互相使用，因为定义不是调用.但是在实际调用f时，g得先定义过。
```python
def f():
  print("f")
  g()
def g():
  print(g)
  f()
```
- 嵌套函数（不是c意义上的互相调用）
  ``` python
  def f():
    print("f")
    def g():
      print("g")
    g()
  
  f()#合理调用
  f.g()#不合法，g是外界无法看到的，只能在f函数里面使用，类似于私有成员
  ```
  但是，在下面的情况可以：
  ```
- 嵌套函数（不是c意义上的互相调用）
  ``` python
  def f():
    print("f")
    def g():
      print("g")
    return g

   h = f() #现在h是g（）函数
   h()  #==g()
   #甚至下面的这个也合法
   f()()
  
  f()#合理调用
  f.g()#不合法，g是外界无法看到的，只能在f函数里面使用，类似于私有成员
  ```
- 函数对象类型
  ```python
  f = fib
  f(1000)
  fib(1000)
  ```
  现在相当于函数也是数据，赋值给f，f就可以直接当做函数来用了
  值得注意的是，一般的return是直接终止的，但是在```try-finally-```限制性finally，再return。

### 3.2.3 Lambda表达式
```python
def function(para_list):
  return expression
#等价于
lambda[para_list]:expression
```
相当于创建了一个匿名函数，返回函数对象，适用于需要简单函数的部分，需要注意的是 **它本身不是表达式，虽然感觉上很像表达式的作用
```python
f = lambda a,b : a + b  #取个别名
print(type(f)) #class function
```

### 3.2.4 函数标注
提供用户自定义函数所使用的的类型原信息
- 函数标注格式
  参数使用“ ：”来标注，返回值用“ ->”来标注
  ```python 
  def Add(x:int,y:int = 0) ->int:#还可以看到缺省值。
  return x + y
  ```

  