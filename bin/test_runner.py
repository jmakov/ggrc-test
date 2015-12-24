#!/usr/bin/env python2
# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com
import sys
import os
import commands
import subprocess
import logging


# append path so we can import project modules
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../"
PROJECT_SRC_PATH = PROJECT_ROOT_PATH + "src/"
sys.path.append(PROJECT_SRC_PATH)

from lib import constants, file_ops, log, virtual_env


VIRTENV_PATH = PROJECT_ROOT_PATH + constants.path.VIRTUALENV_DIR
logger = logging.getLogger()


def set_up_directories():
    logger.info("Setting up directories.")
    file_ops.create_directory(PROJECT_ROOT_PATH + constants.path.LOGS)
    file_ops.create_directory(VIRTENV_PATH)


def update_virtenv():
    exit_code = subprocess.call(
        ["pip", "install", "-r", constants.path.REQUIREMENTS]
    )

    if exit_code != 0:
        raise EnvironmentError("Problem installing requirements")


def run_tests():
    import nose
    nose.main()


if __name__ == "__main__":
    set_up_directories()
    log.set_default_file_handler(
        logger, constants.path.LOGS + constants.log.TEST_RUNNER
    )

    exit_code, result = commands.getstatusoutput(
        "virtualenv %s %s" %
        (PROJECT_ROOT_PATH + constants.path.VIRTUALENV_DIR, "--python=python2")
    )

    if exit_code != 0:
        print result
        print "Failed to set up basic virtualenv. Please check the logs."
        raise RuntimeError

    logger.info("Updating virtual environment packages.")

    # doing execfile() on this file will alter the current interpreter's
    # environment so you can import libraries in the virtualenv
    virtual_env.activate(PROJECT_ROOT_PATH)
    update_virtenv()

    run_tests()
