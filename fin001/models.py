from django.db import models


class Rent000(models.Model):

    seq = models.IntegerField('序號',unique = True)
    title = models.CharField('名称',max_length=50)
    
    daterange = models.CharField('合同期限',max_length=50)
    rental = models.CharField('房租价格',max_length=50)
    paid = models.CharField('已支付月份',max_length=50)
    deposit = models.CharField('保证金/押金',max_length=50)
    paymethod = models.CharField('付款方式',default='---',max_length=50)
    area = models.CharField('面积',max_length=50)
    usage = models.CharField('用途',max_length=50)
    addr = models.CharField('地址',max_length=300)
    note = models.CharField('备注',max_length=300)
    is_active = models.BooleanField('是否有效',default= True)
    
    class Meta:
        # ordering = ['dept19__code','sub19__code',]
       
        verbose_name ="门店租金资料表"
        verbose_name_plural ="门店租金资料表"


class Rent001(models.Model):

    seq = models.IntegerField('序號',unique = True)
    datefrom = models.DateField('開始日期')
    dateto = models.DateField('截止日期')
    rent1 = models.IntegerField('银泰嘉园置业租金')
    rent2 = models.IntegerField('恒泽行服务费')
    paid1 = models.DateField('租金付款日期',null=True,blank=True)
    paid2 = models.DateField('服务费付款日期',null=True,blank=True)
    paid1note = models.CharField('租金付款備註',null=True,blank=True,max_length=50)
    paid2note = models.CharField('服务费付款備註',null=True,blank=True,max_length=50)

    class Meta:
        # ordering = ['dept19__code','sub19__code',]
       
        verbose_name ="御华里商铺"
        verbose_name_plural ="御华里商铺"

# Create your models here.
#class Empe(models.Model):

    # seq = models.IntegerField('序號',default=0)
    # name = models.CharField('姓名',max_length=20)
    # gender = models.CharField('性別',max_length=20)
    # bdate = models.DateField('生日',null=True,blank=True)
    # workdate = models.DateField('入职日期',null=True,blank=True)
    # mobile = models.CharField('手機',max_length=20)
    # # store = models.CharField('店別',default='---',max_length=20)
    # store = models.CharField('門店',default='---',max_length=20)
    # dept = models.CharField('部門',default='---',max_length=20)
    # seq2 = models.IntegerField('序號2',default=0)
    
    # title = models.CharField('职位',default='---',max_length=20)
    # contact_name = models.CharField('紧急联系人',default='---',max_length=20)
    # contact_mobile = models.CharField('联系人电话',default='---',max_length=20)
    # note1 = models.CharField('保险',max_length=20,null=True,blank=True)
    # note2 = models.CharField(max_length=200,null=True,blank=True)
    # note3 = models.CharField(max_length=200,null=True,blank=True)
    
    # def __str__(self):
    #     return self.name
        
    # class Meta:
    #     # ordering = ['dept19__code','sub19__code',]
       
    #     verbose_name ="人員主檔"
    #     verbose_name_plural ="人員主檔"