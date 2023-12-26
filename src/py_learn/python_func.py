a = 123
id = id(a)
print(id)

# 1. all

res = all([14, False, 6])
print(res)

# 2. callable 是Python内置函数之一，用于检查对象是否可调用。可调用对象是指可以像函数一样调用的对象，例如函数、方法、类等。如果对象是可调用的，则callable()函数返回True，否则返回False。
# function_name = "my_function"
# if callable(globals()[function_name]):
#     globals()[function_name]()


class MyClass:
    pass


my_object = MyClass()
if callable(getattr(my_object, "my_method", None)):
    my_object.my_method()


res = eval("1 + 3")
print(res)

a = '678888'.strip('67878')
print(a)
