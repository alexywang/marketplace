# Generated by Django 3.0.2 on 2020-04-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20200408_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='item',
            name='date_uploaded',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
