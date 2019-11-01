from django.db import models

# class Data1(models.Model):
#     date1 = models.DateField()
#     place = models.CharField(max_length=100)
#     worker = models.CharField(max_length=100)
#     thing = models.CharField(max_length=100)

class Data2(models.Model):
    ROLE_CHOICES = [
        ('Ah-counter', 'Ah-counter'),
        ('Attendance', 'Attendance'),
        ('GE', 'GE'),
        ('Grammarian', 'SenGrammarianior'),
        ('IE', 'IE'),
        ('Speaker', 'Speaker'),
        ('TME', 'TME'),
        ('TT Evaluator', 'TT Evaluator'),
        ('TT-master', 'TT-master'),
        ('Timer', 'Timer'),
    ]

    MEMBER_CHOICES = [
        ('Member', 'Member'),
        ('Guest', 'Guest'),
    ]

    name = models.CharField(max_length=32)
    member =  models.CharField( choices=MEMBER_CHOICES,max_length=6)
    date1 = models.DateField()
    role = models.CharField(  choices=ROLE_CHOICES,max_length=32)
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
