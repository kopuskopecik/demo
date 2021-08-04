from django.urls import path
from django.conf.urls import url
from rest_framework.generics import CreateAPIView
from services.views import *

urlpatterns = [
    path('services/', Services.as_view()),
    url(r'services/(?P<id>[0-9a-f-]+)/', ServicesRUD.as_view()),
    path("images/<str:id>/", Image.as_view()),
    path("images/", ImageCreate.as_view())
]