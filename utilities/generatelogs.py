import logging
def log():
    logging.basicConfig(filename="..\logs\\Logfile.log", format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logger = logging.getLogger()
    return logger
logger=log()
logger.info("my name is python")
logger.error("my name is java")
