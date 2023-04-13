"""
URL configuration for book_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from rest_framework.routers import SimpleRouter
from .views import BookViewSet, AuthorViewSet, PublisherViewSet
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path








routes = SimpleRouter()
routes.register('books', BookViewSet)
routes.register('author', AuthorViewSet)
routes.register('publisher', PublisherViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes.urls)),
]

urlpatterns += staticfiles_urlpatterns()