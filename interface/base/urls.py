from django.urls import path
from .views import *
urlpatterns = [
    path('', DrawView.as_view(), name="draw_view")
]
