from django.contrib import admin
from django.urls import path

from api.views import WorkList, ImageList, AddressList, EmailList, TelephoneList, ApplicationCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/work', WorkList.as_view()),
    path('api/image', ImageList.as_view()),
    path('api/address', AddressList.as_view()),
    path('api/email', EmailList.as_view()),
    path('api/telephone', TelephoneList.as_view()),
    path('api/application/create', ApplicationCreate.as_view()),
]
