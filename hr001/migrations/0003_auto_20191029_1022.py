# Generated by Django 2.2.6 on 2019-10-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr001', '0002_auto_20191029_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='empe',
            name='dept',
            field=models.CharField(default='---', max_length=20, verbose_name='部門'),
        ),
        migrations.AlterField(
            model_name='empe',
            name='store',
            field=models.CharField(default='---', max_length=20, verbose_name='門店'),
        ),
    ]
