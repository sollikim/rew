from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from blog import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # Добавляем маршруты blog
    path('', include('blog.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), 

]