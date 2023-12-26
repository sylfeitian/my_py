import logging
import os
import time
from functools import wraps


# 1. 最基础的装饰器用法
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something before the original function is called
        print(111)
        result = func(*args, **kwargs)
        print(222)
        # do something after the original function is called
        return result

    return wrapper


@my_decorator
def my_function():
    """This is the docstring for my_function."""
    print(12344)


print(my_function.__name__)  # Output: 'my_function'
print(my_function.__doc__)  # Output: 'This is the docstring for my_function.'
my_function()


def timer(
    log_level=logging.INFO,
    message_format="{func_name}: Time elapsed: {elapsed:.4f} seconds",
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            log_message = message_format.format(
                func_name=func.__name__, elapsed=elapsed
            )
            # logging.log(log_level, log_message)
            print(log_message)
            return result

        print("aaaaa")

        return wrapper

    return decorator


@timer(
    log_level=logging.INFO,
    message_format="{func_name}: Time elapsed: {elapsed:.4f} seconds",
)
def my_expensive_function():
    time.sleep(1)


@timer(log_level=logging.DEBUG)
def my_debug_function():
    time.sleep(1)


my_expensive_function()
my_debug_function()


def sayName(func):
    print("name")

    def inner():
        print("I'm Yu")
        return func()

    return inner


def sayAge(func):
    print("age")

    def inner():
        print("i'm 30")
        return func()

    return inner


@sayName
@sayAge
def sayHi():
    print("Hello, World")


sayHi()


# 装饰器工厂函数，可以
def exit_on_exception(sleep=60, receivers=None):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                logging.error("exit_on_exception")
                logging.exception(e)

                time.sleep(sleep)
                # noinspection PyProtectedMember
                os._exit(1)

        return wrapper

        print("14343")

    return decorator
