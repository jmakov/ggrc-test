
    
import calendar
from datetime import datetime


def get_days_in_current_month():
    now = datetime.now()
    weekday, days_in_month = calendar.monthrange(now.year, now.month)
    return days_in_month
