import logging
import inspect


def CustomLogger(loglevel=logging.DEBUG):
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    logger.setLevel(loglevel)

    fileHandler = logging.FileHandler("/Users/manikantauttarkar/PycharmProjects/workspace/automation_framework/logs/automation.log", mode='a')
    fileHandler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
