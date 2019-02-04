from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='index.html')),
    path('index.html', views.index, name='index'),
]
