# Generated by Django 2.0.6 on 2018-07-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20180705_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('no',), 'verbose_name': '讲师', 'verbose_name_plural': '讲师'},
        ),
        migrations.AddField(
            model_name='user',
            name='counter',
            field=models.IntegerField(default=3, verbose_name='票数'),
        ),
    ]
