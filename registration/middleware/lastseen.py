import datetime
from registration.models import UserProfile
class LastIP(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            UserProfile.objects.filter(user=request.user).update(last_activity_ip=request.META['REMOTE_ADDR'])
        return self.get_response(request)
