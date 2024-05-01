from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='название товара')
    price = models.PositiveIntegerField(verbose_name='цена товара')
    description = models.TextField(verbose_name='описание товара', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания объявления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created_at']


class Feedback(models.Model):
    text = models.TextField(verbose_name='текст отзыва')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='обьявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания отзыва')

    def __str__(self):
        return f'{self.author} прокоментировал {self.ad.title}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ['-created_at']
