import logging

'''
logger
FileHandler
level 
Formatter

FileHandler set LEVEL and Set Formatter.
logger.add(filehandler)
'''


def log_by_ini_config():
    from logging.config import fileConfig
    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    logger.debug("I debug the python log, Configured by INI file")
    # logging.getLogger(__name__).addHandler(logging.NullHandler())
    # logging.debug('debuging informaiont.')
    # logging.info("nihaodede INFO")
    # logging.warning("Waring info")
    # logging.error("ERROR information.")
    # logging.critical("critical information-shutting down.")


def log_by_json_config():
    from logging.config import dictConfig
    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                      '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG}
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    )

    dictConfig(logging_config)
    logger = logging.getLogger()
    logger.debug('I debug logging configured by dict/json data structure.')


def log_by_code_config():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.debug('log this message Configured by CODE.')


def log_into_file():
    logger = logging.getLogger()

    logfile = "./log.txt"
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)

    # Note: you can add more handler (Container)
    logger.addHandler(fh)

    logger.debug('这是 logger debug message')
    logger.info('这是 logger info message')
    logger.warning('这是 logger warning message')


def log_into_file_second():
    logging.basicConfig(filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info("Running Urban Planning")


def log_into_file_third():
    import time
    from logging.handlers import TimedRotatingFileHandler
    import re
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    path = "mylogdate.log"
    # test the In the internal of minutes.
    # handler = TimedRotatingFileHandler(path,
    #                                    when="m",
    #                                    interval=1,
    #                                    backupCount=5)
    handler = TimedRotatingFileHandler(path,
                                       when="D",
                                       interval=1)
    handler.suffix = "%Y%m%d"
    # handler.extMatch = re.compile(r"^\d{8}$")
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    for i in range(6):
        logger.info("This is a test!")
        time.sleep(50)


if __name__ == "__main__":
    # log_by_ini_config()
    # log_by_json_config()
    # log_by_code_config()

    # log_into_file()
    # log_into_file_second()
    log_into_file_third()
