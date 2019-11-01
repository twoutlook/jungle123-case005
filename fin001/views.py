from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Count, Sum, Max, Min
import re
# from .models import Empe


# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

# https://docs.djangoproject.com/en/2.2/topics/auth/default/
from django.contrib.auth.decorators import login_required

from portal.views import index_template
# def index(request):
#     # list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1','member').annotate(headcnt=Count('id'))
#     context = {'list1': []}
#     return render(request, 'case002/index.html', context)

# @login_required(login_url='/admin/login/?next=/')
# def index(request):
#     app = 'hr001'
#     app_name ='Case003'
#     go_up ='../'
#     page_name ='HR001 索引'
#     return index_template(request,app,app_name,go_up,page_name)


# @login_required(login_url='/admin/login/?next=/')
# def s1(request):
#     key={'store':'全部'}
#     list1 = Empe.objects.order_by('seq')
#     context = {'list1': list1,'key': key}
#     return render(request, 'hr001/s1.html', context)

