# Generated by Django 5.0 on 2023-12-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='categori',
            field=models.CharField(default=1, max_length=255, verbose_name='Категории'),
            preserve_default=False,
        ),
    ]