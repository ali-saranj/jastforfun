# Generated by Django 4.2.6 on 2023-10-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0003_remove_salon_category'),
        ('categorys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='salon',
            field=models.ManyToManyField(to='salons.salon'),
        ),
    ]