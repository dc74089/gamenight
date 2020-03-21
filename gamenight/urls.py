"""gamenight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from tribes import views as tribes

urlpatterns = [
    path('admin/', admin.site.urls),

    # Tribes
    path('tribes/', tribes.index, name='tribes'),
    path('tribes/admin', tribes.admin, name='tribes_admin'),
    path('tribes/admin/names', tribes.admin_ajax, name='tribes_ajax'),
    path('tribes/admin/reset', tribes.admin_reset, name='tribes_reset'),
]
