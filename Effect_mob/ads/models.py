from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=35, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ad(models.Model):

    CONDITION = [
        ('NEW', 'Новый'),
        ('NOT NEW', 'Б/У'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=25, verbose_name='Заголовок объявления')
    description = models.CharField(max_length=255, verbose_name='Описание товара')
    image_url = models.URLField(verbose_name='URL изображения')
    category = models.ManyToManyField(Category, verbose_name='Категория товара', related_name='category')
    condition = models.CharField(choices=CONDITION, verbose_name='Состояние товара')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.get_condition_display()}'

    class Meta:
        ordering = ['created_at']


class ExchangeProposal(models.Model):

    awaits = 'awaits'
    accepted = 'accepted'
    rejected = 'rejected'
    STATUS = [
        (awaits, 'ожидает'),
        (rejected, 'отклонена'),
        (accepted, 'принята'),
    ]
    ad_sender_id = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='sender', verbose_name='id объявления отправителя')
    ad_receiver_id= models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='receiver', verbose_name='id объявления получателя')
    comment = models.CharField(max_length=150, verbose_name='Комментарий')
    status = models.CharField(max_length=10, choices=STATUS, default=awaits, verbose_name='Статус заявки')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_at']
