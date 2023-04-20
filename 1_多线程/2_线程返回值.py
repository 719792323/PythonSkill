from threading import Thread, current_thread
import concurrent.futures

"""
方案一：
使用全局变量的*列表*，来保存返回值
选择列表的一个原因是：列表的 append() 方法是线程安全的，CPython 中，GIL 防止对它们的并发访问。
(也就是说List的append是有锁的)
"""
thread_size = 10
result = [None] * thread_size
threads = [None] * thread_size


def method1(thread_index):
    result[thread_index] = current_thread().name


def test_method1():
    for i in range(thread_size):
        threads[i] = (Thread(target=method1, args=(i,), name="thread_" + str(i)))
        threads[i].start()
    for i in range(thread_size):
        threads[i].join()
    print(result)


"""
方案二
重写 Thread 的 join 方法，返回线程函数的返回值
"""


class FutureThread(Thread):
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super().join()
        return self._return


def method2():
    return "bar"


def test_method2():
    future = FutureThread(target=method2)
    future.start()
    result = future.join()
    print(result)


"""
方案三
使用concurrent.futures
"""


def method3(i):
    return "thread-{}".format(i)


def test_method3():
    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            future = executor.submit(method3, i)
            result.append(future)

        for future in concurrent.futures.as_completed(result):
            print(future.result())


if __name__ == '__main__':
    # test_method1()
    # test_method2()
    test_method3()
