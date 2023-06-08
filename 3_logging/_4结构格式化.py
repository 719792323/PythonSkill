import logging as log


def test_log():
    log.info('Python info')


if __name__ == '__main__':
    # log.basicConfig(format='%(asctime)s %(message)s',level=log.INFO)
    # log.info('Python info')

    # log.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=log.INFO)
    # log.info('Python info')
    format = '%(asctime)s | %(threadName)s | %(levelname)s | %(filename)s:%(funcName)s:%(lineno)d - %(message)s'
    log.basicConfig(format=format, level=log.INFO, filename='example.log')
    test_log()
