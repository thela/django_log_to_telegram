from django.core.exceptions import ImproperlyConfigured
from django.views import View


class ThrowError(View):
    def get(self, request):
        raise ImproperlyConfigured
        return HttpResponse('hallo')
