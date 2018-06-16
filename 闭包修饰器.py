# 闭包：函数里面那层函数调用外面那层函数的参数，此参数可以是一个函数
# 例：func(2)(100)
# def func(x):
# 	def fn(arg):
# 		return arg ** x
# 	return fn


# 修饰器：一个可以挂羊头卖狗肉的函数
# 例：
def deco(fn):
    print("装饰器函数被调用")
    print(fn)
    return lambda: print("hello world!")


@deco
def myfunc():
    print("函数myfunc被调用！")


myfunc()
myfunc()
myfunc()
myfunc()
myfunc()
# 只能被修饰一次　　　hello world却重复打印
print("_________________________")


# 闭包和装饰器同时有的例子：
def msg_service(fn):
    def savemoney2(name, x):
        print("装饰器函数被调用")
        print("欢迎", name, "来江苏银行,请取号！！！")
        fn(name, x)
        print(name, "办理了存", x, "元钱的业务，短信发送中")
    return savemoney2


@msg_service
def savemoney(name, x):
    print(name, "存钱", x, "元")


savemoney("小张", 200)
savemoney("小赵", 500)
