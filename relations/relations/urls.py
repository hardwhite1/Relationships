"""
URL configuration for relations project.

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
from django.contrib import admin
from django.urls import path, include
from model_relations import views

urlpatterns = [
    path('', views.show, name='show'),
    path('api/artists', views.save_or_fetch_artists, name='save_or_fetch_artists'),
    path('api/artists/<int:id>', views.fetch_one_artist, name='fetch_one_artist'),
    path('api/artists/<int:id>/delete', views.delete_artist, name='delete_artist'),
    path('api/artists/<int:id>/update', views.update_artist, name='update_artist'),
    path('api/artists/<int:id>/albums', views.albums_for_artist, name='albums_for_artist'),
    path('admin/', admin.site.urls),
    # path('', include('model_relations.urls'))
]
