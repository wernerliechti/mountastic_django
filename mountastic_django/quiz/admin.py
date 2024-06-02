from django.contrib import admin
from .models import Mountain

class MountainAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'region', 'group', 'has_image')
   

    @admin.display(boolean=True, ordering='image', description='Has Image')
    def has_image(self, obj):
        return bool(obj.image)

# Register your models here.
admin.site.register(Mountain, MountainAdmin)
