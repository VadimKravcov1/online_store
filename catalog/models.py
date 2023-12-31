from django.db import models
from django.utils import timezone
from users.models import User
# Create your models here.

NULLABLE = {'blank':True, 'null':True}

class Product(models.Model):
    # first_name = models.CharField(max_length=150, verbose_name='имя')
    # last_name = models.CharField(max_length=150, verbose_name='фамилия')

    title = models.CharField(max_length=100, verbose_name='название', unique=True, **NULLABLE)
    description = models.TextField(unique=True, **NULLABLE)
    preview = models.ImageField(upload_to='product/', verbose_name='превью', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    purchase_price = models.PositiveIntegerField(default=0, verbose_name='цена')
    date_creation = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    date_modified = models.DateTimeField(default=timezone.now, verbose_name='дата изменения')
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.pk} {self.title} {self.purchase_price} {self.category}'

    class Meta:
        verbose_name = 'продукт' # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'









class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField()



    def __str__(self):
        # Строковое отображение объекта
        return self.title

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'




class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.PositiveIntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active_version = models.BooleanField(default=True, verbose_name='статус версии')

    def __str__(self):
        # Строковое отображение объекта
        return self.version_name


    class Meta:
        verbose_name = 'версия' # Настройка для наименования одного объекта
        verbose_name_plural = 'версии'