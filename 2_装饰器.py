import functools
import time

"""
1. 普通方法装饰器
2. 装饰之后，仍然保留原方法名字
3. 带参数的装饰器
4. 普通类装饰器
5. 带参数类装饰器
6. 类静态方法装饰器
7. 类和偏函数装饰器
"""


def test1():
    """
    1. 普通方法装饰器: 接收func方法，返回wrapper方法
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Before ' + func.__name__)
            re = func(*args, **kwargs)
            print('After ' + func.__name__)
            return re

        return wrapper

    @decorator
    def func():
        print('hello func')
        return 'func'

    func()
    print(func.__name__)  # 此时func_1.__name__得到的并不是func_1，而是wrapper，因为func已经由wrapper替代了


def test2_1():
    """
    接收func方法，返回wrapper方法，并半wrapper改回func的name
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Before ' + func.__name__)
            re = func(*args, **kwargs)
            print('After ' + func.__name__)
            return re

        wrapper.__name__ = func.__name__
        return wrapper

    @decorator
    def func():
        print('hello func')
        return 'func'

    func()
    print(func.__name__)


def test2_2():
    """
    接收func方法，返回wrapper方法，并半wrapper改回func的name
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Before ' + func.__name__)
            re = func(*args, **kwargs)
            print('After ' + func.__name__)
            return re

        return wrapper

    @decorator
    def func():
        print('hello func')
        return 'func'

    func()
    print(func.__name__)


def test2_3():
    """
    接收func方法，返回wrapper方法，并半wrapper改回func的name
    """

    def my_wrapper(origin_func):
        def decorator(wrapper_func):
            def wrapper(*args, **kwargs):
                return wrapper_func(*args, **kwargs)

            wrapper.__name__ = origin_func.__name__
            return wrapper

        return decorator

    def decorator(func):
        @my_wrapper(func)
        def wrapper(*args, **kwargs):
            print('Before ' + func.__name__)
            re = func(*args, **kwargs)
            print('After ' + func.__name__)
            return re

        return wrapper

    @decorator
    def func():
        print('hello func')
        return 'func'

    func()
    print(func.__name__)


def test3():
    """
    3. 带参数的装饰器
    """

    def log(param):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print('Before ' + func.__name__)
                print(param)
                re = func(*args, **kwargs)
                print('After ' + func.__name__)
                return re

            return wrapper

        return decorator

    @log('xx')
    def func():
        print('hello func')
        return 'func'

    func()


def test4():
    """
    4. 普通类装饰器
    """

    class class_decorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print('Before ' + self.func.__name__)
            re = self.func(*args, **kwargs)
            print('After ' + self.func.__name__)
            return re

    @class_decorator
    def func():
        print('hello func 6')
        return 'func 6'

    func()


def test5():
    """
    5. 带参数类装饰器
    """

    class class_decorator:
        def __init__(self, is_log=True):
            self.is_log = is_log

        def __call__(self, func):
            def wrapper(*args, **kwargs):
                if self.is_log:
                    print('Before ' + func.__name__)
                    re = func(*args, **kwargs)
                    print('After ' + func.__name__)
                else:
                    re = func(*args, **kwargs)
                return re

            return wrapper

    @class_decorator()
    def func():
        print('hello func 6')
        return 'func 6'

    func()


def test6():
    """
    使用偏函数
    :return:
    """

    class DelayFunc:
        def __init__(self, func):
            self.duration = 2
            self.func = func

        def __call__(self, *args, **kwargs):
            print(f'Wait for {self.duration} seconds...')
            time.sleep(self.duration)
            return self.func(*args, **kwargs)

        def eager_call(self, *args, **kwargs):
            print('Call without delay')
            return self.func(*args, **kwargs)

    def delay():
        return functools.partial(DelayFunc)

    @delay()
    def add(x, y):
        return x + y

    print(add(1, 2))


def test7():
    """
    闭包装饰器实现单例
    """

    def singleton(cls):
        instances = {}

        def get_instance(*args, **kwargs):
            cls_name = cls.__name__
            if cls_name not in instances:
                instance = cls(*args, **kwargs)
                instances[cls_name] = instance
            return instances[cls_name]

        return get_instance

    @singleton
    class User:
        def __init__(self, name):
            self.name = name

    u1 = User('hello')
    u2 = User('hello')
    u3 = User('hi')
    print(id(u1))
    print(id(u2))
    print(id(u3))


def test8():
    """
    类静态方法装饰器
    """

    class Singleton:
        _instances = dict()

        @staticmethod
        def singleton(cls):
            def wrapper(*args, **kwargs):
                cls_name = cls.__name__
                if cls_name not in Singleton._instances:
                    instance = cls(*args, **kwargs)
                    Singleton._instances[cls_name] = instance
                return Singleton._instances[cls_name]

            return wrapper

    def singleton():
        return functools.partial(Singleton.singleton)

    @singleton()
    class User2:
        def __init__(self, name):
            self.name = name

    u1 = User2('hello')
    u2 = User2('hello')
    u3 = User2('hi')
    print(id(u1))
    print(id(u2))
    print(id(u3))


def test9():
    class Singleton:
        _instances = dict()

        @staticmethod
        def singleton(cls):
            def wrapper(*args, **kwargs):
                cls_name = cls.__name__
                if cls_name not in Singleton._instances:
                    instance = cls(*args, **kwargs)
                    Singleton._instances[cls_name] = instance
                return Singleton._instances[cls_name]

            return wrapper

    @Singleton.singleton
    class User2:
        def __init__(self, name):
            self.name = name

    u1 = User2('hello')
    u2 = User2('hello')
    u3 = User2('hi')
    print(id(u1))
    print(id(u2))
    print(id(u3))


def test10():
    """
    装饰器的执行顺序
    """

    def log1(func):
        def wrapper(*args, **kwargs):
            print('Before log1')
            re = func(*args, **kwargs)
            print('After log1')
            return re

        return wrapper

    def log2(func):
        def wrapper(*args, **kwargs):
            print('Before log2')
            re = func(*args, **kwargs)
            print('After log2')
            return re

        return wrapper

    @log1
    @log2
    def func1():
        print('func1')

    @log2
    @log1
    def func2():
        print('func2')

    func1()
    func2()


def test11():
    def log1(func):
        def wrapper(*args, **kwargs):
            print('Before log1')
            re = func(*args, **kwargs)
            print('After log1')
            return re

        return wrapper

    # 装饰器的实际调用过程
    re = log1(lambda a, b: a + b)(1, 2)
    print(re)


if __name__ == '__main__':
    # test1()
    # test2_1()
    # test2_2()
    # test2_3()
    # test4()
    # test5()
    # test6()
    test7()
    # test8()
    # test9()
    # test10()
    # test11()
