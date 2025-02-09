import inspect
import logging


class LoggenClass:
    @staticmethod
    def log_generator():
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        logfile = logging.FileHandler("C:\\Users\\91992\\PycharmProjects\\OHRM_REV_01\\Logs\\OHRM_REV_01.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
