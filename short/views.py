from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import redirect, get_object_or_404
from .models import ShortURL
from .serializers import ShortURLSerializer

class ShortenURLView(generics.CreateAPIView):
    """
    Create a shortened URL.
    """
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

class RedirectShortURLView(generics.GenericAPIView):
    """
    Redirects a short URL to the original long URL.
    """
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return redirect(short_url.original_url)
