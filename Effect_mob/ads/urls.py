from django.urls import path
from .views import AdsList, CreateAd, UserAdsList, UpdateAd, DeleteAd, DetailAd, SearchAd

app_name = 'ads'
urlpatterns = [
    path('', AdsList.as_view(), name='ads-list'),
    path('create_ad/', CreateAd.as_view(), name='create-ad'),
    path('ads/user_ads/', UserAdsList.as_view(), name='user-ads'),
    path('ads/user_ads/update/<int:ad_pk>/', UpdateAd.as_view(), name='update-ad'),
    path('ads/user_ads/delete/<int:ad_pk>/', DeleteAd.as_view(), name='delete-ad'),
    path('ads/detail/<int:ad_pk>/', DetailAd.as_view(), name='ad-detail'),
    path('ads/search_ad/', SearchAd.as_view(), name='search-ad'),
]