from django.urls import path
from .views import ShortenURLView, RedirectShortURLView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:short_code>/', RedirectShortURLView.as_view(), name='redirect-url'),
]
