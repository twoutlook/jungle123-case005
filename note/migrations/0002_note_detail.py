# Generated by Django 2.2.6 on 2019-10-04 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
