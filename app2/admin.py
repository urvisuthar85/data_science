from django.contrib import admin
from app2.models import U
from .views import default_data

class SuperAdmin(admin.ModelAdmin):
    admin.site.site_title = admin.site.site_header = default_data['app1'].title()
    admin.site.index_title = 'Admin'

admin.site.register(U,SuperAdmin)
# Register your models here.
