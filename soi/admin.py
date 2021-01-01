from django.contrib import admin
from import_export import resources
from soi.models import *
from import_export.admin import ImportExportModelAdmin

class SaleinvoiceResource(resources.ModelResource):
    class Meta:
        model = sale_invoice_summery_v
        import_id_fields = ['Invoice_Line_id']

class SaleinvoiceAdmin(ImportExportModelAdmin):
    resource_class = SaleinvoiceResource
# Register your models here.
admin.site.register(sale_invoice_summery_v,SaleinvoiceAdmin)
