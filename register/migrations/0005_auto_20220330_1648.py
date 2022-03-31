# Generated by Django 3.2.12 on 2022-03-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20220330_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadas',
            name='celular',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadas',
            name='leg_prog',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadas',
            name='trabalhou',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadas',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cadas',
            name='genero',
            field=models.CharField(blank=True, choices=[('', 'Escolha uma opção'), ('F', 'Feminino'), ('M', 'Masculino')], default='', max_length=1),
        ),
    ]
