"""
函数在执行时，要带上所有必要的参数进行调用。但是，有时参数可以在函数被调用之前提前获知。这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
偏函数是将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数依次作为partial()函数后续的参数，除非使用关键字参数。

就像足球比赛安排首发一样，主教练可以固定让某位球员一直首发，而剩余10人，则是等到赛前才决定

所以偏函数，又叫偏心函数

这跟scala的函数柯里化相似
def ass(x: Int, y: Int) = x + y
则调用时，必须add(1, 2)

def add(x:Int)(y:Int) = x + y
则调用时，必须add(1)(2)

"""

import functools


def add(x, y):
    print(x, y)
    return x + y


# 固定让10首发
add_10 = functools.partial(add, 10)


class Stu:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    @staticmethod
    def get_default_instance(e):
        # 固定让1，2，3，4首发
        return functools.partial(Stu, 1, 2, 3, 4)(e)


if __name__ == '__main__':
    print(add_10(5))
    s = Stu.get_default_instance(5)
    print(s.a, s.b, s.c, s.d, s.e)
