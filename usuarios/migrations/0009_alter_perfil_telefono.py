# Generated by Django 4.0.5 on 2022-06-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_alter_perfil_legajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
    ]
