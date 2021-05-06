from django.urls import re_path
from .views import ProxyView


urlpatterns = [
    re_path('^.*', ProxyView.as_view()),
]
