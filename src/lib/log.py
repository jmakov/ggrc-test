# header6ff05843-c222-461f-8226-36a7abe6806e

import logging
from lib import constants


def set_default_file_handler(logger, log_path, log_level=logging.DEBUG):
    """
    :type logger: logging.Logger
    :param log_path: str
    :param log_level: str
    """
    logger.setLevel(log_level)
    formatter = logging.Formatter(constants.log.DEFAULT_FORMAT)
    fh = logging.FileHandler(filename=log_path, mode="w")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
