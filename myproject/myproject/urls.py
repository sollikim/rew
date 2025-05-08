from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для админки
    path('api/', include('myapp.urls')),  # Путь для API, включающий маршруты из приложения myapp
]

from django.http import HttpResponse
from django.urls import path, include

# Функция для обработки домашней страницы
def home(request):
    return HttpResponse("Welcome to the API!")

urlpatterns = [
    path('', home),  # Домашняя страница будет возвращать сообщение
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]