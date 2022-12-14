# Generated by Django 4.1.3 on 2022-11-15 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Müşteri')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Müşteri')], default=1)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Erkek'), (2, 'Kadın')], null=True)),
                ('registration_number', models.CharField(blank=True, max_length=15, null=True)),
                ('identity_number', models.CharField(blank=True, max_length=11, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoggedInUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logged_in_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
