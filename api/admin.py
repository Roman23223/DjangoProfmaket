from django.contrib import admin

from api.models import Work, Image, Address, Email, Telephone_number, Application


class ImageAdmin(admin.ModelAdmin):
    search_fields =['title']
    readonly_fields = ['img_preview']


class WorkAdmin(admin.ModelAdmin):
    search_fields =['title']
    readonly_fields = ['time_create', 'time_update']

class ApplicationAdmin(admin.ModelAdmin):
    search_fields =['email']
    readonly_fields = ['size', 'product_time', 'sender_name', 'number', 'email', 'comment', 'time_create']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Work, WorkAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Telephone_number)
admin.site.register(Application, ApplicationAdmin)

