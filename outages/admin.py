from django.contrib import admin
from outages import models

# Register your models here.


class OutageAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'isp_provider',
        'issue_type',
        'service_area',
        'start_date',
        'ccp_account_reference',
        'status',
    ]


class OutageInline(admin.TabularInline):
    model = models.Outage

    search_fields = [
        'isp_provider',
        'start_date',
        'service_area',
        'start_date',
        'status',
    ]
    extra = 1


# Customized admin
admin.site.site_header = 'Tech Support'
admin.site.site_url = '/outages/'
admin.site.register(models.Outage)
