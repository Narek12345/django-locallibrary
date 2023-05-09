"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    # Админиастрирование Django.
    path('admin/', admin.site.urls),
    # Приложение catalog.
    path('catalog/', include('catalog.urls')),
    # Перенаправляем запросы с корневого URL на URL приложения catalog.
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Размещение статических файлов.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)