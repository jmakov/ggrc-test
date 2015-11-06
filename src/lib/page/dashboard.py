# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com

from lib import constants
from lib.page import widget_bar, header


class DashboardPage(widget_bar.WidgetBarPage, header.HeaderPage):
    def navigate_to(self):
        self._driver.get(constants.uri.BASE + constants.uri.DASHBOARD)
