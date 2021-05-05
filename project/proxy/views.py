from django.http import HttpResponse
from django.views import View
from .services import get_edited_html


class ProxyView(View):
    """Proxy view."""

    def get(self, request, company, article_id):
        html = get_edited_html(company, article_id)
        return HttpResponse(html, content_type='text/HTML')
