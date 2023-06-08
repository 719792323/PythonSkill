import logging as log

"""
通过 logging.basicConfig() 可以设置 root 的日志级别，和日志输出格式。
注意：Logging.basicConfig() 需要在开头就设置，在中间设置并无作用
"""
if __name__ == '__main__':
    log.basicConfig(filename='example.log', level=log.DEBUG)
    log.debug('Python debug')
    log.info('Python info')
    log.warning('Python warning')
    log.error('Python Error')
    log.critical('Python critical')