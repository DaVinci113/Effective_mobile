from django.urls import path
from .views import AdsList, CreateAd, UserAdsList, AdDetail

app_name = 'ads'
urlpatterns = [
    path('', AdsList.as_view(), name='ads-list'),
    path('create_ad/', CreateAd.as_view(), name='create-ad'),
    path('ads/user_ads/', UserAdsList.as_view(), name='user-ads'),
    path('ads/detail/<int:ad_pk>/', AdDetail.as_view(), name='ad-detail'),

    path('create_ad/', CreateAd.as_view(), name='create-ad'),
]