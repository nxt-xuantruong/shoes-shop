"""
URL configuration for shop project.

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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import single_page_view
# get_client_token

router = routers.DefaultRouter()


urlpatterns = [
    path('account/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path("api/", include('customer.urls')),  
    path("api/", include('product.urls')),  
    path("api/", include('sale.urls')),    
    path("api/", include('order.urls')),    

    
    re_path(r"^.*$", single_page_view),
    # path('client_token/', get_client_token, name='client_token'),
]

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + urlpatterns