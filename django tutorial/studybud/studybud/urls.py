
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "SUJAL VYAS"
admin.site.site_title = "sujal's portfolio"
admin.site.index_title = "welcome to portfolio admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
   
    
]
