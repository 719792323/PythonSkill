from threading import Thread, current_thread
import time


def run():
    print("thread name:{}".format(current_thread().name))
    time.sleep(3)


def run_args(arg1, arg2):
    print(arg1, arg2)


def dead_loop():
    while True:
        pass


def thread_sleep():
    time.sleep(3)


if __name__ == '__main__':
    # 创建一个进程，该进程执行run方法
    t1 = Thread(target=run, name="my-thread-1")
    t1.start()
    t1.join()  # join要在start后面，否则会抛出异常，主线程调用join的后需要等待，t1执行完才能继续运行

    # 创建一个进程，运行有参数的方法
    t2 = Thread(target=run_args, name="my-thread-2", args=(1, "2"))
    t2.start()
    t2.join()

    # 创建一个进程，运行死循环方法，但是设置为守护进程
    t3 = Thread(target=dead_loop, name="my-thread-3", daemon=True)
    t3.start()

    # 创建一个线程，运行阻塞方法
    t4 = Thread(target=thread_sleep(), name="my-thread-4", daemon=True)
    t4.start()
