from concurrent.futures import ThreadPoolExecutor
from time import sleep

tasklist = ["任务1", "任务2", "任务3", "任务4"]


def task(taskname: str):
    sleep(5)
    print(taskname + " 已完成\n")
    return taskname + " 的执行结果"


executor = ThreadPoolExecutor(max_workers=3)  # 创建线程池(是一个ThreadPoolExecutor对象)，线程数为3
future_a = executor.submit(task, tasklist[0])  # 通过submit方法向线程池提交任务，返回一个对应的Future对象
future_b = executor.submit(task, tasklist[1])
future_c = executor.submit(task, tasklist[2])
future_d = executor.submit(task, tasklist[3])  # 如果提交时，线程池中没有空余线程，则该线程会进入等待状态，主线程不会阻塞
print(future_a.result(), future_b.result())  # 通过Future对象的result()方法获取任务的返回值，若没有执行完，则会陷入阻塞

