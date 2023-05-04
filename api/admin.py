from django.contrib import admin

from api.models import Work, Image, Address, Email, Telephone_number, Application

admin.site.register(Work)
admin.site.register(Image)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Telephone_number)
admin.site.register(Application)

admin.site.site_title = 'Админ панель'
admin.site.site_header = 'Profmaket'
admin.site.index_title = 'Администрирование сайта'