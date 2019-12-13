from django.contrib import admin
from .models import Cusip
# Register your models here.

class CusipAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Cusip, CusipAdmin)
