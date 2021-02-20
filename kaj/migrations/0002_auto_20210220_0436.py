# Generated by Django 3.1.6 on 2021-02-20 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kaj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kaj_jobst', to=settings.AUTH_USER_MODEL),
        ),
    ]
