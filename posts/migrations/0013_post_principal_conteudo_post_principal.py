# Generated by Django 4.0.5 on 2022-06-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_foto_alter_post_principal_foto_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_principal',
            name='conteudo_post_principal',
            field=models.TextField(default=1, verbose_name='Conteúdo do Post Principal'),
            preserve_default=False,
        ),
    ]
