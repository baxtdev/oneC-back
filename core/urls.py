"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import debug_toolbar
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from users.views import*
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()

router.register('userINFO',UserInfoAPIViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
    path('api/v1/userGET/<str:user_id>',UserInfoGETapiVew.as_view(),name='Get info User'),
    path('api/v1/userSET/',ProcessDataAPIView.as_view(),name="Set Data Array")
]


if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)