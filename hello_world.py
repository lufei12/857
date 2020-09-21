#
#
# #print("hello world")
#
#
#
#
# #a 变量值 ，= 赋值符 ，变量值
# #a="hello world"
#
#
# #print(a)
#
#
#
# #字符串 '' "" '''
# #number 整数 小数 111 3.2
# #布尔值 True False
# #空值 None
#
# #列表list[1,2,3,4,5] 可修改 有序
# #元祖 tuple(1,2,3,4,5) 不可修改 有序
# #集合 set{1,2,3,4,5} 不可重复 无序
#
#
# #字典 dict {"name":"...","age":18}
#
#
#
# y=[1,2,3,4,]
# y[0]=10
# print(y)
#
# k=(1,2,3,4,)
# #k[0]=10
# print(k)
#
# c={1,2,5,6,7,5}
# print(c)
#
#
#
# l=20
# p="50"
# print(l + int(p))
# print(str(l) + p)
#
# e=True
# r=99
# print(e + r)
#
# f={"name":"sj","age":20}
# print(f["name"])
#
#
#
# l = [1,2,3,4,5,6]
# print(tuple(l))
# print(set(l))
#
#
#
# t = [1,2,3,4,5]
# print(list(t))
# print(set(t))
#
#
# q = [1,2,3,4]
# print(list(q))
# print(tuple(q))
#
#
# z = "123456578"
#
#
#
#
# a = "thadjs"
# t = ["a","4","g"]
# o =("a","4","g")
# w = {"a","4","g"}
# d = {"name":"往返","sex":"女"}
#
# print("a" in a)



# money = 500000
# if(money >= 500000):
#         print("买六瓶SK11")
#         print("用一瓶扔一瓶")
# else:
#         print("白日做梦")





# money = 5000
# if(money < 5000):
#     print("回家种田吧")
#
# elif(money < 100000):
#     print("买五箱华子")
#     print("一天抽一条")
#
# elif(money < 500000):`
#     print("都买了" )
#
# else:
#     print("都是我的")




# for i in range(500):
#     print(i)
#     print("天天开心")

# print(list(range(90,0,-1)))
# print(list(range(100)))
#
#
# i = 2
# while(i<100):
#     print("发财")
# i =+1


# for i in range(2,20):
#     if(i ==5 or i ==15):
#
#         continue
#     print(i)
#
#
#
#
# 函数(方法)
# der 关键字, div: 方法名:a,b 接收外界参数，参数变量必须写在()： ：表示下方包含一个代码块(方法体)
# def div(a,b):
#     if b == 0:
#        print("被除数不能为0")
#     else:
#         print(a/b)
# div(50,20)
# div(60,30)
# div(10,100)

# def select_data(s):
#     res = "查询结果"
#     return res
# result = select_data("1")
# print(result)
#
# 位置参数 调用时，参数有一个传一个
# def s(a,b):
#     return a+b
# print(s(3,5))

# 关键字参数 给参数设置默认值
# 如果调用时没有传参测用默认值
# 关键字、位置同时存在，位置参数在后边，关键字参数在前边
# def s(a=1,b=5):
#     return a+b
# print(s(1,9))
#
# print(s(1,2))
# print(s(b=20))


# def ar(*args,**kwargs):
#     print(args)
#     print(kwargs)
# ar(5,6,7,8,a=4,b=9)


# f = open("s.txt",'w')
# res =f.write("fggfg")
# print(res)
# f.close()

# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,'=',i*j,end='\t')
#     print()
#

# c =20
# def aaa():
#     global c
#     c = 30
# aaa()
# print(c)

# 字符串
# a = "1234567890"
# b = "564"
# print(a[1:-2])
# print(a[-3:])
# print(a[5:])
# print(a[1])
#
# a = " dskjfajh " #字符串对象
# a = a.strip()
# print(a.strip()) #去除前后空格
# print(a.lstrip()) #去除左空格
# print(a.rstrip()) #去除右空格
#
# line = "用例名，账户名，充值金额，预期结果"
# line = line.replace(",",",")
# print(line)
# print(line.split(',')) #切片

# 乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         #1 X 2 =2
#         print("{} X {}".format(j,i,i*j),end='\t')
#     print()
#
#
#
 # 遍历列表
# l = [1,2,3,4,5,6,7,8]
# for i in l :
#     print(i)
#
#
# l[0]=20  #根据下标修改列表元素的值
#
#
# 类和对象
# 创建一个类
# class str_demo():
#
#     s = None
#
#     def replace(self):
#         print("字符串替换")
#
#     def split(self):
#         print("字符串切割")
#
# sd = str_demo()  #实例化 sd就是一个对象
# sd.s = "hello"
# sd.replace()
# sd.split()
#
# class str_demo():
#
#     #不需要显示调用，程序自动调用的
#     def __init__(self):
#         print("魔法方法")
#
#     #实例方法
#     def


#
# class PrivateDemo():
#     _a = None
#
#     def set_a(self,value):
#         self._a = value
#     def get_a(self):
#         return self._a
#
# p = PrivateDemo()
# p.set_a("shuf")
# print(p.get_a())
#

#多态-子类中，对父类方法的重写



# import requests





# '''
# 1、编写一个返回随机手机号的方法
# 2、编写一个返回指定长度和内容的随机字符串方法
# 3、编写一个返回随机姓名的方法
# '''



#
# import  random
# def iphone():
#     l = random.choices("0123456789",k=9)
#     s = random.choice("358")
#     str = "1" + s + "".join(l)
#     print(str)
# iphone()
#
#
#
# def kkkk55(n,b):
#     l = random.choices(b,k=n)
#     print("".join(l))
# kkkk55(5,"fdagjkhdfjh")
#
#
#
# def name(a,s):
#     a1 = random.choice(a)
#     s1 = random.choice(s)
#     print(a1+s1)
# a = "赵钱孙李王"
# s = "一二三四五六"
# name(a,s)
#
#

print("asdf")
try:
    r = open("b.txt","r")
except:
    print("程序执行遇到了问题")
    print("重新打开文件")

print("文件以及打开")



print("hello")

#print(1/0)# ZeroDinisionError 运行时错误 异常：报错，结束代码的运行
print("hello")
try:
    r = open("b.txt","r") #报错 FileNotFoundError

except(FileNotFoundError,ZeroDivisionError) as e:
    print(e)
    print("程序执行遇到了问题")
    print("重新打开文件")

print("文件以及打开")




print("hello")

#print(1/0)# ZeroDinisionError 运行时错误 异常：报错，结束代码的运行
print("hello")
try:
    r = open("b.txt","r") #报错 FileNotFoundError

except(FileNotFoundError,ZeroDivisionError) as e:
    print(e)
    print("程序执行遇到了问题")
    print("重新打开文件")
except ZeroDivisionError as e:
    print("除数不能为0")
else:
    print()

print("文件以及打开")




