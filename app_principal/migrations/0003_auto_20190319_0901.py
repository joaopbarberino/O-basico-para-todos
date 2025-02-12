# Generated by Django 2.1.7 on 2019-03-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0002_auto_20190319_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='arquivo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='livro',
            name='descricao',
            field=models.TextField(verbose_name='Insira uma breve descrição do livro'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='lancamento',
            field=models.IntegerField(default=2006, verbose_name='Ano de Lançamento'),
            preserve_default=False,
        ),
    ]
