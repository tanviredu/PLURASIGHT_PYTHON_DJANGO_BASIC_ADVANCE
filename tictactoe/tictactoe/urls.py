from django.contrib import admin
from django.urls import path
from .views import welcome
from django.conf.urls import include
## you need to import the views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('player/',include('player.urls'))
]
