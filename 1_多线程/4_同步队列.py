"""
# 创建一个FIFO队列，并制定队列大小，若maxsize被指定为小于等于0，则队列无限大
Queue(maxsize=5)
# 返回队列的大致大小，注意并不是确切值，所以不能被用来当做后续线程是否会被阻塞的依据
Queue.qsize()
# 判断队列为空是否成立，同样不能作为阻塞依据
Queue.empty()
# 判断队列为满是否成立，同样不能作为阻塞依据
Queue.full()
# 投放元素进入队列，block为True表示如果队列满了投放失败，将阻塞该线程，timeout可用来设置线程阻塞的时间长短（秒）
# 注意，如果block为False，如果队列为满，则将直接引发Full异常，timeout将被忽略（在外界用try处理异常即可）
Queue.put(item, block=True, timeout=None)
# 相当于put(item, block=False)
Queue.put_nowait(item)
# 从队列中取出元素，block为False而队列为空时，会引发Empty异常
Queue.get(block=True, timeout=False)
# 相当于get(block=False)
Queue.get_nowait()
# 每个线程使用get方法从队列中获取一个元素，该线程通过调用task_done()表示该元素已处理完成。
Queue.task_done()
# 阻塞至队列中所有元素都被处理完成，即队列中所有元素都已被接收，且接收线程全已调用task_done()。
Queue.join()
"""
"""
queue模块提供了4种我们可以利用的队列容器，
分别QueueQueue（先进先出队列）、LifoQueue（先进后出队列）、PriortyQueue（优先级队列）、SimpleQueue（无界的先进先出队列，简单实现，缺少Queue中的任务跟踪等高级功能）
"""
import queue
from random import choice
from threading import Thread

q = queue.Queue(maxsize=5)
dealList = ["红烧猪蹄", "卤鸡爪", "酸菜鱼", "糖醋里脊", "九转大肠", "阳春面", "烤鸭", "烧鸡", "剁椒鱼头", "酸汤肥牛", "炖羊肉"]


def cooking(chefname: str):
    for i in range(4):
        deal = choice(dealList)
        q.put(deal, block=True)
        print("厨师{}给大家带来一道：{}  ".format(chefname, deal))


def eating(custname: str):
    for i in range(3):
        deal = q.get(block=True)
        print("顾客{}吃掉了：{}  ".format(custname, deal))
        q.task_done()  # 表示完成了一个任务，主要搭配q.join()使用


if __name__ == "__main__":
    # 创建并启动厨师ABC线程，创建并启动顾客1234线程
    threadlist_chef = [Thread(target=cooking, args=chefname).start() for chefname in ["A", "B", "C"]]
    threadlist_cust = [Thread(target=eating, args=str(custname)).start() for custname in range(4)]
    # 队列阻塞，直到所有线程对每个元素都调用了task_done
    q.join()
