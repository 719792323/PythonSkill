"""
Python没有volatile关键字.
因为Python将所有对象存储在主内存中的堆上，所以修改对象所有线程可见（关键原因）
此外,由于Python解释器循环使用锁定(GIL)的方式,一次只有一个线程将主动运行Python代码.（既python是伪多线程）
"""
from threading import Lock, Thread
from time import sleep

flag = True
lock = Lock()


def tar():
    global flag, lock
    while True:
        lock.acquire()
        "线程任务逻辑"
        if flag is False:
            break
        lock.release()
    lock.release()


if __name__ == "__main__":
    thread = Thread(target=tar)
    thread.start()
    print("3秒后线程会被杀死")
    sleep(3)
    flag = False
    print("线程已被杀死")
