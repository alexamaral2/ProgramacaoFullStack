# Generated by Django 4.1.4 on 2022-12-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_parametros'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentoRotativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField()),
                ('saida', models.DateTimeField(null=True)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pago', models.BooleanField(default=False)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
        ),
    ]