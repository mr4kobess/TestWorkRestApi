# Generated by Django 3.1.7 on 2021-02-26 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0013_auto_20210226_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='quiz', to=settings.AUTH_USER_MODEL),
        ),
    ]
