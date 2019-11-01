# Generated by Django 2.2.6 on 2019-11-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr001', '0007_pay'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pay',
            options={'verbose_name': '薪資異動', 'verbose_name_plural': '薪資異動'},
        ),
        migrations.AddField(
            model_name='pay',
            name='pos1',
            field=models.CharField(default='---', max_length=30, verbose_name='原有职位'),
        ),
        migrations.AddField(
            model_name='pay',
            name='pos2',
            field=models.CharField(default='---', max_length=30, verbose_name='现任职位'),
        ),
    ]
