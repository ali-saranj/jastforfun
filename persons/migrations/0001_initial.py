# Generated by Django 4.2.6 on 2023-10-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='image/')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
