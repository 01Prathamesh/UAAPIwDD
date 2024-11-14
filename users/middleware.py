from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class CaptureIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            request.user.last_login_ip = ip_address
            request.user.save()
