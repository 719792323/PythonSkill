import logging
import traceback

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("error.log")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.addHandler(console)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    try:
        open("sklearn.txt", "rb")
    except Exception:
        logger.error(traceback.format_exc())
    logger.info("Finish")
