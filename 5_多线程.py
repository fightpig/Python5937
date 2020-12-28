import threading
import time
from contextlib import contextmanager

"""
多线程共享资源安全问题，同时修改num，
则有时线程1刚执行num + 1操作，还没来得及重新给num赋值，
这时线程2火急燎燎的就执行了num + 1操作且重新给num赋值，
然后线程1才执行重新给num赋值，则线程2此番操作则白干了
"""

num = 0


def auto_lock(func):
    lock = threading.RLock()
    acquire_count = 0

    def wrapper(*args, **kwargs):
        try:
            lock.acquire()
            nonlocal acquire_count
            acquire_count += 1
            re = func(*args, **kwargs)
            return re
        finally:
            lock.release()
            print(acquire_count)

    return wrapper


class MyLock:
    def __init__(self):
        self._rlock = threading.RLock()
        self.acquire_count = 0

    @contextmanager
    def lock(self):
        try:
            self._rlock.acquire()
            self.acquire_count += 1
            yield
        finally:
            self._rlock.release()


def add(times):
    global num
    for i in range(times):
        num += 1
    print(f'{threading.current_thread().name:3} num: {num}')


def add_1(times, lock_func):
    with lock_func():
        add(times)


@auto_lock
def add_2(times):
    add(times)


def operate(func):
    times = 100 * 100 * 100 * 100
    t1 = threading.Thread(target=func, args=(times,))
    t2 = threading.Thread(target=func, args=(times,))
    t3 = threading.Thread(target=func, args=(times,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(num == 3 * times, num, 3 * times)


def operate_1(func, lock_func):
    times = 100 * 100 * 100 * 100
    t1 = threading.Thread(target=func, args=(times, lock_func))
    t2 = threading.Thread(target=func, args=(times, lock_func))
    t3 = threading.Thread(target=func, args=(times, lock_func))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(num == 3 * times, num, 3 * times)


def test1():
    """没加锁，多个线程瞎搞资源"""
    operate(add)


def test2():
    """加锁"""
    global add
    add = auto_lock(add)
    operate(add)


def test4():
    """加锁"""
    operate(add_2)


def test3():
    """加锁"""
    my_lock = MyLock()
    operate_1(add_1, my_lock.lock)
    print(my_lock.acquire_count)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
