from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'audconverter'
urlpatterns = [
        path('<slug>',views.conv,name = 'filetype'),
        
        ]
