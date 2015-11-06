# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: jernej@reciprocitylabs.com
# Maintained By: jernej@reciprocitylabs.com
    
import calendar
from datetime import datetime


def get_days_in_current_month():
    now = datetime.now()
    weekday, days_in_month = calendar.monthrange(now.year, now.month)
    return days_in_month
