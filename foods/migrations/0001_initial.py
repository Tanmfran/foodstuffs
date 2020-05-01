# Generated by Django 2.2.10 on 2020-05-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('item_url', models.CharField(max_length=512)),
                ('quantity', models.CharField(default=0, max_length=200)),
            ],
        ),
    ]
