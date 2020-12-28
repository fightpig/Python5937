from contextlib import contextmanager
import traceback

num = 1

"""
上下文管理器用于：
    1. 执行前做某些动作
    2. 真正执行
    3. 执行后做某些动作
"""


def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            print('Begin t launch ' + func.__name__)
            return func(*args, **kwargs)
        except Exception:
            print('Yes, I catched a exception')
            # print(traceback.format_exc())
    return wrapper


@contextmanager
def try_catch_1(func):
    try:
        print('Begin t launch ' + func.__name__)
        yield
    except Exception:
        print('Yes, I catched a exception')
        # print(traceback.format_exc())


class TryCatch:
    def __init__(self, func):
        self.func = func

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def launch(self):
        try:
            print('Begin t launch ' + self.func.__name__)
            self.func()
        except Exception:
            print('Yes, I catched a exception')


def f1():
    a = 1 / 0
    print(a)


@try_catch
def f2():
    a = 1 / 0
    print(a)


def f3():
    with try_catch_1(f3):
        f1()


def f5():
    with TryCatch(f1) as tc:
       tc.launch()


def f4():
    """
    当执行f3()，会得到一个生成器g，g生成器里面放着10，只有执行next(g)才能得到10
        g = f3()
        next(g)
    """
    yield 10


if __name__ == '__main__':
    try:
        print('Begin t launch ' + f1.__name__)
        f1()
    except Exception:
        print('Yes, I catched a exception')
    f2()
    f3()
    f5()
