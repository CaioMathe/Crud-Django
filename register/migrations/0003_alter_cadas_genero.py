# Generated by Django 3.2.12 on 2022-03-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_cadas_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadas',
            name='genero',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], default='Escolha um genero', max_length=1),
        ),
    ]