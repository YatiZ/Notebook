from django.contrib import admin
from . models import Page,Image,Book,newstats
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
# Register your models here.

admin.site.register(Page)
admin.site.register(Image)
admin.site.register(Book)
@admin.register(newstats)
class NewStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context= None):

        stat_data = (
            newstats.objects.annotate().values('win','mac','iph','android','oth')
        )

        as_json = json.dumps(list(stat_data),cls = DjangoJSONEncoder)
        extra_context = extra_context or {'stat_data':as_json}
        return super().changelist_view(request, extra_context = extra_context)
