import logging

log = logging.getLogger(__name__)
# 日志模块最上级LEVEL，handler低于这个level的设置无效
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s | %(threadName)s | %(levelname)s | %(filename)s:%(funcName)s:%(lineno)d - %(message)s')
handler = logging.FileHandler("example.log")
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
log.addHandler(handler)
log.addHandler(console)


def test_log():
    log.info('info msg')
    log.debug("debug msg")


if __name__ == '__main__':
    test_log()
