from django.db import models
import datetime
# class Data1(models.Model):
#     date1 = models.DateField()
#     place = models.CharField(max_length=100)
#     worker = models.CharField(max_length=100)
#     thing = models.CharField(max_length=100)

class Data2(models.Model):
    ROLE_CHOICES = [
        ('Attendance', 'Attendance'),
        ('Ah-counter', 'Ah-counter'),
        ('GE', 'GE'),
        ('Grammarian', 'Grammarian'),
        ('IE', 'IE'),
        ('Speaker', 'Speaker'),
        ('TME', 'TME'),
        ('TT Speaker', 'TT Speaker'),
        ('TT Evaluator', 'TT Evaluator'),
        ('TT-master', 'TT-master'),
        ('Timer', 'Timer'),
    ]

    MEMBER_CHOICES = [
        ('Member', 'Member'),
        ('Guest', 'Guest'),
    ]

    name = models.CharField(max_length=32)
    member =  models.CharField( 'Member or Guest',choices=MEMBER_CHOICES,max_length=6)
    date1 = models.DateField('Meeting Date', default=datetime.date.today)
    role = models.CharField( 'Meeting Role', choices=ROLE_CHOICES,max_length=32)
    points = models.IntegerField(default=0)
    class Meta:
        unique_together = ('name', 'date1','member','role')
       
        verbose_name ="Meeting"
        verbose_name_plural ="Meeting"



class Best(models.Model):
    BEST_CHOICES = [
        ('tt', 'tt'),
        # ('Guest', 'Guest'),
    ]
    date1 = models.DateField()
    title = models.CharField(choices=BEST_CHOICES,default='tt',max_length=32)
    name = models.CharField(max_length=32)
    class Meta:
        unique_together = ( 'date1','title')
       
        verbose_name ="Meeting Best"
        verbose_name_plural ="Meeting Best"
