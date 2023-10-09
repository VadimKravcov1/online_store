# Generated by Django 4.2.5 on 2023-10-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_material_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='counter_views',
            field=models.IntegerField(default=0, verbose_name='счетчик'),
        ),
        migrations.AlterField(
            model_name='material',
            name='published',
            field=models.BooleanField(default=True, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
    ]