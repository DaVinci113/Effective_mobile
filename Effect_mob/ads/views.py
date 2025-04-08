from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template.context_processors import request
from django.views.generic import CreateView, ListView
from .models import Ad
from .forms import CreateAdForm


# Create your views here.


class AdsList(ListView):
    # paginate_by = 5
    model = Ad
    template_name = 'ads/ads_list.html'


class CreateAd(CreateView):
    form_class = CreateAdForm
    template_name = 'ads/create_ad.html'
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)
