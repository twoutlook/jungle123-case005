from django.contrib import admin


from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Rent000
from .models import Rent001


class Rent000Resource(resources.ModelResource):
   class Meta:
        model = Rent000
class Rent000Admin(ImportExportModelAdmin):
    resource_class = Rent000Resource
    list_display = ('seq','title','daterange','rental','paid','deposit','paymethod','area','usage','addr','note','is_active')
    list_filter = ['seq','is_active']
    # ordering = ('id',)
    search_fields = ['usage']
admin.site.register(Rent000, Rent000Admin)


class Rent001Resource(resources.ModelResource):
   class Meta:
        model = Rent001
class Rent001Admin(ImportExportModelAdmin):
    resource_class = Rent001Resource
    list_display = ('seq','datefrom','dateto','rent1','rent2','paid1','paid2','paid1note','paid2note')
    list_filter = ['seq']
    # ordering = ('id',)
    search_fields = ['datefrom']
admin.site.register(Rent001, Rent001Admin)
