# Generated by Django 4.1.1 on 2022-11-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
