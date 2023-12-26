import functools
from functools import lru_cache

from cachetools import TTLCache, cached, time

cache = TTLCache(maxsize=100, ttl=300)
cache_category = TTLCache(maxsize=100, ttl=300)


# @functools.cache 缓存函数结果
# @functools.cached_property 缓存只读函数，作为只读属性
class MyClass:
    def __init__(self, a):
        self._x = a

    @functools.cached_property
    def x(self):
        # 计算属性的值ØØØ
        self._x = self._x * 2
        return self._x

    def set_x(self, input):
        self._x = input

    @functools.cache
    def get_x(self):
        return self._x


# myclass = MyClass(10)
# out = myclass.x
# print(out)
# for i in range(10):
#     myclass.set_x(i)
#     print(myclass.x)
#     print("-----")
#     print(myclass.get_x())

# ------------------------


lst = ["aaa", "bb", "c"]

# 使用 sorted 函数进行排序，key 参数指定排序规则
lst_sorted = sorted(lst, key=functools.cmp_to_key(lambda a, b: len(a) - len(b)))
# 获取lst长度最长的的一个元素
longest_element = max(lst, key=len)
print(longest_element)  # 'aaa'


print(lst_sorted)  # ['c', 'bb', 'aaa']


@cached(cache)
def get_shop_category(shop_code):
    if shop_code == "fasbee":
        time.sleep(5)
        return {"a": 1, "b": (2, 4)}

    if shop_code == "pal":
        time.sleep(5)
        return {"c": 2, "d": 4}

    return {"e": 2, "f": 8}


@cached(cache_category)
def get_category(shop_code):
    if shop_code == "fasbee":
        return 1234

    if shop_code == "pal":
        time.sleep(5)
        return 434554

    return 4656


print(get_category("fasbee"))

numbers = [1, 2, 43, 5, 6]
squared = map(lambda x: x**2, numbers)
print(list(numbers))


def greet(name: str) -> str:
    return "Hello, " + name


def my_generator(numbers):
    for ele in numbers:
        yield ele


# 第一种，用生成器方式
for ele in my_generator(numbers):
    print(ele)


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n

    print("11111")
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


@lru_cache(maxsize=1)
def lru_test():
    print("dsds")
    return 124


lru_test()
