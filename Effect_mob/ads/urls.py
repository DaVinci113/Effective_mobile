from django.urls import path
from .views import AdsList, CreateAd

app_name = 'ads'
urlpatterns = [
    path('', AdsList.as_view(), name='ads-list'),
    path('create_ad/', CreateAd.as_view(), name='create-ad'),
]