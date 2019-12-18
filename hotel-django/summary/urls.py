from django.urls import path, include
from . import views

urlpatterns = [
    path(r'?<locator>\d+)/$', views.summary, name="summary"),
]