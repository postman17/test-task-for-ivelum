from django.urls import path
from .views import ProxyView


urlpatterns = [
    path('ru/company/<str:company>/blog/<int:article_id>/', ProxyView.as_view()),
]
