from django.views.generic import CreateView, ListView
from .models import Ad
from .forms import CreateAdForm


# Create your views here.


class AdsList(ListView):
    paginate_by = 5
    model = Ad
    template_name = 'ads/ads_list.html'


class CreateAd(CreateView):
    form_class = CreateAdForm
    template_name = 'ads/create_ad.html'
    success_url = '/'
