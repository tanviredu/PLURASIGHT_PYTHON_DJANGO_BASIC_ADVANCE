from django.contrib import admin
from django.urls import path
from .views import welcome

## you need to import the views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
]
