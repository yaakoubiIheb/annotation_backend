from django.contrib import admin
from .models import*

class AnnotationAdmin(admin.ModelAdmin):
    list_display=('id','start','end','label','text','document')
    list_display_links=('id','start','end','label','text','document')
    list_filter=['document_id']
    search_fields=['label']


class DocumentAdmin(admin.ModelAdmin):
    list_display=('id','text')
    list_display_links=('id','text')
    



admin.site.register(Document,DocumentAdmin)
admin.site.register(Annotation,AnnotationAdmin)


admin.site.site_header="Annotations administration"
admin.site.site_title = "Annotations administration"
admin.site.index_title = "Annotations administration"
admin.site.site_url=None
