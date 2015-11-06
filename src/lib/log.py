# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

import logging
from lib import constants


def set_default_file_handler(logger, log_path):
    formatter = logging.Formatter(constants.log.DEFAULT_FORMAT)
    fh = logging.FileHandler(filename=log_path, mode="w")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
