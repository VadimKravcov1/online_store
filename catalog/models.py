from django.db import models

# Create your models here.


class Product(models.Model):
    # first_name = models.CharField(max_length=150, verbose_name='имя')
    # last_name = models.CharField(max_length=150, verbose_name='фамилия')

    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField()
    preview = models.ImageField(upload_to='product/', verbose_name='превью', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

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


