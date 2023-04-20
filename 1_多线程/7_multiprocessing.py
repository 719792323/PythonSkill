"""
GIL:(Global Interpreter LockGlobalInterpreterLock，全局解释器锁）是CPython中采用的一种机制，它确保同一时刻只有一个线程在执行Python字节码。
给整个解释器加锁使得解释器多线程运行更方便，而且开发的CPython也更易于维护，但是代价是牺牲了在多处理器上的并行性。
因此，在相当多的场景中，CPython解释器下的多线程机制的性能都不尽如人意。
"""
"""
因为GIL，所以Python可以认为是伪多线程，所以创建多进程比多线程性能更高
因为Python程序的每个进程都有自己的GIL锁，互不干涉，因此我们也可以直接使用多线程来处理一些计算任务，
Python的多线程可以使用multiprocessing模块来完成。
"""