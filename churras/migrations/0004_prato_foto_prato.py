# Generated by Django 4.2.2 on 2023-06-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churras', '0003_prato_pessoa_prato_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='foto_prato',
            field=models.ImageField(blank=True, upload_to='pratos/%Y/%m'),
        ),
    ]
