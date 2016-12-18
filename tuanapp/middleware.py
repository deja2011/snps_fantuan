import pytz

from django.utils import timezone

from tuanproj.settings import CURRENT_TIME_ZONE

class TimezoneMiddleware(object):
    def process_request(self, request):
        timezone.activate(pytz.timezone(CURRENT_TIME_ZONE))
