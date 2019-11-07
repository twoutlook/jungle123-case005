from django.contrib import admin


from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Empe
from .models import Pay
from .models import Attendance

class AttendanceResource(resources.ModelResource):
   class Meta:
        model = Attendance
class AttendanceAdmin(ImportExportModelAdmin):
    # inlines = [PayInline]
    resource_class = AttendanceResource
    list_display = ('date1','name','acct','dept','type1','time1','place')
    list_filter = ['name','dept','type1','place']
    # list_filter = ['store','gender']
    # ordering = ('id',)
    # search_fields = ['name','mobile',]
admin.site.register(Attendance, AttendanceAdmin)


class PayInline(admin.TabularInline):
    model = Pay
    extra = 3
# class Empe19Resource(resources.ModelResource):
#    class Meta:
#         model = Empe19
# class Empe19Admin(ImportExportModelAdmin):
#     resource_class = Empe19Resource
#     list_display = ('id','dept19','sub19','seq','name','title','jobdesc','phone','is_set1')
#     list_filter = ['dept19','sub19','title',]
#     ordering = ('id',)
#     search_fields = ['name','phone',]
# admin.site.register(Empe19, Empe19Admin)

class EmpeResource(resources.ModelResource):
   class Meta:
        model = Empe
class EmpeAdmin(ImportExportModelAdmin):
    inlines = [PayInline]
    resource_class = EmpeResource
    list_display = ('seq','name','gender','bdate','workdate','work2date','resigndate','is_resign','mobile','store','dept','seq2','title','contact_name','contact_mobile')
    # list_display = ('seq','name','gender','bdate','workdate','mobile','store','dept','seq2','title','contact_name','contact_mobile')
    list_filter = ['is_resign','store','gender']
    # list_filter = ['store','gender']
    # ordering = ('id',)
    search_fields = ['name','mobile',]
admin.site.register(Empe, EmpeAdmin)

class PayResource(resources.ModelResource):
   class Meta:
        model = Pay
class PayAdmin(ImportExportModelAdmin):
    resource_class = PayResource
    list_display = ('empe','seq','date1','pay1','pay2','pos1','pos2','approval','note')
    # list_display = ('seq','name','gender','bdate','workdate','mobile','store','dept','seq2','title','contact_name','contact_mobile')
    list_filter = ['approval','pos1','pos2']
    # list_filter = ['store','gender']
    # ordering = ('id',)
    search_fields = ['empe__name','approval','pos1','pos2']
admin.site.register(Pay, PayAdmin)
