# Generated by Django 2.2.6 on 2019-10-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=0, verbose_name='序號')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gender', models.CharField(max_length=20, verbose_name='性別')),
                ('bdate', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('workdate', models.DateField(blank=True, null=True, verbose_name='入职日期')),
                ('mobile', models.CharField(max_length=20, verbose_name='手機')),
                ('dept', models.CharField(default='---', max_length=20, verbose_name='部门')),
                ('title', models.CharField(default='---', max_length=20, verbose_name='职位')),
                ('contact_name', models.CharField(default='---', max_length=20, verbose_name='紧急联系人')),
                ('contact_mobile', models.CharField(default='---', max_length=20, verbose_name='联系人电话')),
                ('note1', models.CharField(blank=True, max_length=20, null=True, verbose_name='保险')),
                ('note2', models.CharField(blank=True, max_length=200, null=True)),
                ('note3', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': '人員主檔',
                'verbose_name_plural': '人員主檔',
            },
        ),
    ]
