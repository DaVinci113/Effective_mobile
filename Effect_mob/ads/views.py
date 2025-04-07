from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Ad, ExchangeProposal


# Create your views here.


class AdsList(ListView):
    paginate_by = 5
    model = Ad
    template_name = 'ads/ads_list.html'

class CreateAd(CreateView):
    model = Ad
    fields = '__all__'
    template_name = 'ads/create_ad.html'
    success_url = 'ads-list'
