# Generated by Django 2.1.7 on 2019-03-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='arquivo',
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.CharField(default='Apenas o primeiro autor listado no livro: SOBRENOME, Nome', max_length=120),
        ),
    ]