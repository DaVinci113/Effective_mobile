from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Ad
from .forms import CreateAdForm


# Create your views here.


class AdsList(ListView):
    # paginate_by = 5
    model = Ad
    template_name = 'ads/ads_list.html'


class UserAdsList(ListView):
    model = Ad
    template_name = 'ads/user_ads.html'

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)


class CreateAd(CreateView):
    form_class = CreateAdForm
    template_name = 'ads/create_ad.html'
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


class UpdateAd(UpdateView):
    form_class = CreateAdForm
    fields = '__all__'
    template_name = 'ads/update_ad.html'
    pk_url_kwarg = 'ad_pk'
    success_url = '/ads/user_ads/'

