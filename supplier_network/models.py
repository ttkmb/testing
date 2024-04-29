from django.db import models
from django.utils.translation import gettext_lazy

from products.models import Product


class SupplierNetwork(models.Model):
    class STRUCTURE(models.TextChoices):
        FACTORY = 'factory', gettext_lazy('Завод')
        RETAIL = 'retail', gettext_lazy('Розничная сеть')
        INDIVIDUAL = 'individual', gettext_lazy('Индивидуальный предприниматель')

    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица', blank=True, null=True, unique=True)
    house = models.IntegerField(verbose_name='Номер дома', blank=True, null=True)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Продукты')
    structure = models.CharField(max_length=50, choices=STRUCTURE.choices, verbose_name='Структура')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, verbose_name='Поставщик', blank=True)
    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность',
                                                  default=0)
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Сеть поставщиков'
        verbose_name_plural = 'Сети поставщиков'

    def __str__(self):
        return self.name
