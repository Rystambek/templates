from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('HomeApp.urls')),
    path("login/", include('LoginApp.urls')),  # Login ilovasini qo'shish
]
