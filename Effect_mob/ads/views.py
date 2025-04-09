
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Ad, Category
from .forms import CreateAdForm


# Create your views here.
class Filter:
    """Категории фильтрации"""

    def get_category(self):
        return Category.objects.all().distinct()

    def get_condition(self):
        return Ad.CONDITION


class AdsFilter(Filter, ListView):
    """Фильтрует на основании выбора категории"""

    template_name = 'ads/ads_list.html'

    def get_queryset(self):
        category = self.request.GET.getlist('category')
        condition = self.request.GET.getlist('condition')
        if category and condition:
            return Ad.objects.filter(
                category__in=category,
                condition__in=condition
            ).exclude(user=self.request.user)
        elif condition:
            return Ad.objects.filter(
                condition__in=condition
            ).exclude(user=self.request.user)
        else:
            return Ad.objects.filter(
                category__in=category
            ).exclude(user=self.request.user)


class AdsList(AdsFilter, ListView):
    """Вывод чужих объявлений"""

    # paginate_by = 5
    model = Ad
    template_name = 'ads/ads_list.html'

    def get_queryset(self):
        return Ad.objects.exclude(user=self.request.user)


class UserAdsList(Filter, ListView):
    """Вывод своих объявлений"""

    model = Ad
    template_name = 'ads/user_ads_list.html'

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)


class CreateAd(CreateView):
    """Создает объявление"""

    form_class = CreateAdForm
    template_name = 'ads/create_ad.html'
    success_url = '/ads/user_ads'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


class UpdateAd(UpdateView):
    """Обновляет объявление"""

    model = Ad
    fields = [
        'title',
        'description',
        'image_url',
        'category',
        'condition',
    ]
    template_name = 'ads/update_ad.html'
    pk_url_kwarg = 'ad_pk'
    success_url = '/ads/user_ads/'


class DeleteAd(DeleteView):
    """Удаляет объявление"""

    model = Ad
    pk_url_kwarg = 'ad_pk'
    template_name = 'ads/delete.html'
    success_url = '/ads/user_ads/'


class DetailAd(DetailView):
    """Вывод подробной инф-ии по объявлению"""

    model = Ad
    template_name = 'ads/ad_detail.html'
    pk_url_kwarg = 'ad_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if context['object'].user == self.request.user:
            context['autor'] = True
        else:
            context['autor'] = False
        return context


class SearchAd(ListView):
    """Поиск чужих объявлений по введденным данным"""

    model = Ad
    template_name = 'ads/ads_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        query = Ad.objects.filter(Q(title__icontains=q)|Q(description__icontains=q)).exclude(user=self.request.user)
        return query


class SearchUserAd(ListView):
    """Поиск своих объявлений по введденным данным"""

    model = Ad
    template_name = 'ads/user_ads_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        query = Ad.objects.filter(Q(title__icontains=q)|Q(description__icontains=q)).filter(user=self.request.user)
        return query
