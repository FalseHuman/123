# Generated by Django 2.2.1 on 2020-08-30 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200801_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comm_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата комментария'),
        ),
    ]
