# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

from lib import constants


def activate(project_root_path):
    activate_this_path = project_root_path \
        + constants.path.VIRTUALENV_DIR \
        + constants.path.BIN_DIR \
        + constants.path.VIRTUALENV_ACTIVATE
    execfile(activate_this_path, dict(__file__=activate_this_path))
