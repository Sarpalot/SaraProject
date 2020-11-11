from django.contrib import admin
from django.db import models

from companydata.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','business_id','city',)
    search_fields = ['name','business_id', ]
    list_filter = ('city',)

admin.site.register(Company, CompanyAdmin)
