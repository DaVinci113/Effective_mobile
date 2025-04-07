from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    new = 'New'
    not_new = 'NOT New'
    CONDITION = [
        (new , 'Новый'),
        (not_new, 'Б/У')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=25, verbose_name='Заголовок объявления')
    description = models.CharField(max_length=255, verbose_name='Описание товара')
    image_url = models.URLField(verbose_name='URL изображения')
    category = models.CharField(max_length=30, verbose_name='Категория товара')
    condition = models.CharField(max_length=30, choices=CONDITION, verbose_name='Состояние товара')
    created_at = models.DateTimeField(auto_now_add=True)

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