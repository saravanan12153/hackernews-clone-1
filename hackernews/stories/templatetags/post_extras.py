import datetime
from django.utils.timezone import utc
from django import template 

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def post_age(created):  
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    age_in_minutes = int((now - created).total_seconds())/60

    if age_in_minutes < 3:
	age_string = "just now"
    elif age_in_minutes < 60:
	value = age_in_minutes
	precision = "minute"
    elif age_in_minutes < 60*24:
	value = age_in_minutes // 60
	precision = "hour"
    else:
	value = age_in_minutes // (24*60)
	precision = "day"

    age_string = "%d %s%s ago" % (value,precision,'s' if value > 1 else '')
    return age_string
