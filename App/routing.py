from django.urls import path
from .consumer import *

url_patterns = [
    path('notification/', MyConsumer.as_asgi()),
]
