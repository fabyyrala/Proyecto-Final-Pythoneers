# Generated by Django 4.2.3 on 2023-08-03 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]
