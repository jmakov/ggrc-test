# header6ff05843-c222-461f-8226-36a7abe6806e
    
import calendar
from datetime import datetime


def get_days_in_current_month():
    now = datetime.now()
    weekday, days_in_month = calendar.monthrange(now.year, now.month)
    return days_in_month


def get_from_string(date_str, date_format):
    return datetime.strptime(date_str, date_format)


def get_month_start(date):
    """
    :type date: datetime
    :rtype: datetime
    """
    return date.replace(day=1)


def get_month_end(date):
    """
    :type date: datetime
    :rtype: datetime
    """
    return date.replace(day=calendar.monthrange(date.year, date.month)[1])


def get_current():
    return datetime.now()
