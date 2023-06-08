import logging as log

if __name__ == '__main__':
    log.debug('Python debug')
    log.info('Python info')
    log.warning('Python warning')
    log.error('Python Error')
    log.critical('Python critical')
    # 不支持{}写法
    # log.warning("hello {}", "world")
