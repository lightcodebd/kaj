# Generated by Django 3.1.6 on 2021-02-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaj', '0003_auto_20210220_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOBLOCATION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
