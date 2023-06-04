from django.contrib import admin

from api.models import Work, Image, Address, Email, Telephone_number, Application


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'work']
    search_fields = ['title']
    readonly_fields = ['img_preview']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields =['title']
    readonly_fields = ['time_create', 'time_update']

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['email', 'sender_name', 'time_create']
    search_fields =['email']
    date_hierarchy = 'time_create'
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

