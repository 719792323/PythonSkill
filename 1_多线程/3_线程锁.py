from threading import Thread, current_thread, Lock
import time
from loguru import logger as log

lock = Lock()


def test_lock():
    # 获取锁
    lock.acquire()
    log.info("thread:{},get lock".format(current_thread().name))
    time.sleep(5)
    # 释放锁
    log.info("thread:{},release lock".format(current_thread().name))
    lock.release()


if __name__ == '__main__':
    t1 = Thread(target=test_lock,name="my-1")
    t2 = Thread(target=test_lock,name="my-2")
    t1.start()
    t2.start()
