from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('whoami', AboutPageView.as_view(), name = 'whoami'),
    path('', HomePageView.as_view(), name = 'index'),
]