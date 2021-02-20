# Generated by Django 3.1.6 on 2021-02-20 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kaj', '0005_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=200, unique=True)),
                ('jobpublished', models.DateTimeField()),
                ('Apply_start', models.DateTimeField()),
                ('Last_date', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('jobdescription', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish'), (2, 'Pending')], default=0)),
                ('types', models.IntegerField(choices=[(0, 'BD Govt Job'), (1, 'Private Job'), (2, 'Question'), (3, 'Cercular')], default=4)),
                ('source_link', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kajpost', to=settings.AUTH_USER_MODEL)),
                ('joblocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joblocation', to='kaj.joblocation')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
