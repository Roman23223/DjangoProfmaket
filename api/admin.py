from django.contrib import admin

from api.models import Work, Image, Address, Email, Telephone_number, Application


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']





admin.site.register(Work)
admin.site.register(Image, ImageAdmin)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Telephone_number)
admin.site.register(Application)

