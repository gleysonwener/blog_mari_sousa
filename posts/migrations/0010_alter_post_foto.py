# Generated by Django 4.0.5 on 2022-06-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_foto_alter_post_principal_foto_principal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='post_imagens/%Y/%m/%d', verbose_name='Imagem'),
        ),
    ]
