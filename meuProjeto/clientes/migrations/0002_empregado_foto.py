# Generated by Django 4.1.4 on 2022-12-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]