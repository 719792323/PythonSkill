from threading import Thread, current_thread, Lock
import time

lock = Lock()


def test_lock():
    # 获取锁
    lock.acquire()
    print("thread:{},get lock".format(current_thread().name))
    time.sleep(5)
    # 释放锁
    print("thread:{},release lock".format(current_thread().name))
    lock.release()


if __name__ == '__main__':
    t1 = Thread(target=test_lock,name="my-1")
    t2 = Thread(target=test_lock,name="my-2")
    t1.start()
    t2.start()
