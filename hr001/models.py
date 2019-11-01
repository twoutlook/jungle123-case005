from django.db import models

# Create your models here.
class Empe(models.Model):

    seq = models.IntegerField('序號',default=0)
    name = models.CharField('姓名',max_length=20)
    gender = models.CharField('性別',max_length=20)
    bdate = models.DateField('生日',null=True,blank=True)
    workdate = models.DateField('入职日期',null=True,blank=True)
    work2date = models.DateField('转正日期',null=True,blank=True)
    resigndate = models.DateField('離職日期',null=True,blank=True)
    is_resign = models.BooleanField('是否離職',default=False)
    mobile = models.CharField('手機',max_length=20)
    # store = models.CharField('店別',default='---',max_length=20)
    store = models.CharField('門店',default='---',max_length=20)
    dept = models.CharField('部門',default='---',max_length=20)
    seq2 = models.IntegerField('序號2',default=0)
    
    title = models.CharField('职位',default='---',max_length=20)
    contact_name = models.CharField('紧急联系人',default='---',max_length=20)
    contact_mobile = models.CharField('联系人电话',default='---',max_length=20)
    note1 = models.CharField('保险',max_length=20,null=True,blank=True)
    note2 = models.CharField(max_length=200,null=True,blank=True)
    note3 = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        # ordering = ['dept19__code','sub19__code',]
       
        verbose_name ="人員主檔"
        verbose_name_plural ="人員主檔"

class Pay(models.Model):
    empe = models.ForeignKey(Empe, on_delete=models.CASCADE)
    seq = models.IntegerField('序號')
    date1 = models.DateField('調薪日期')
    pay1 = models.IntegerField('原有薪資')
    pay2 = models.IntegerField('調整后薪資')
    pos1 =  models.CharField('原有职位',default='---',max_length=30)
    pos2 =  models.CharField('现任职位',default='---',max_length=30)
    approval =  models.CharField('調資審批人',max_length=30)
    note =  models.CharField('備註',max_length=200,null=True,blank=True)
    class Meta:
        # ordering = ['dept19__code','sub19__code',]
       
        verbose_name ="薪資異動"
        verbose_name_plural ="薪資異動"
