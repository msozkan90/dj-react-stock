# Generated by Django 4.1.3 on 2022-11-16 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0007_alter_items_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PharmacySell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('item_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.items')),
            ],
        ),
    ]