from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('', include('PronafMaisAlimentos.urls')),
    path('admin/', admin.site.urls),
]
