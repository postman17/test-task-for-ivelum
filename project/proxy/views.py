from django.http import HttpResponse
from django.views import View
from .services import get_edited_html


class ProxyView(View):
    """Proxy view."""

    def get(self, request, *args, **kwargs):
        html = get_edited_html(request.path, *args, **kwargs)
        return HttpResponse(html, content_type='text/HTML')
