"""MovieReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() func tion: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.movie_front_page),
    path('about/',views.about_us),
    path('contact/',views.contact_us),
    re_path(r'^(?P<m_id>[a-z]{2}\d+)/$',views.movie_data),
    re_path(r'^(?P<m_id>[a-z]{2}\d+)/trailer',views.movie_trailer),
    re_path('accounts/login/(?P<m_id>[a-z]{2}\d+)/',views.login_page),
    path('accounts/login/profile/',views.profile),
    re_path('accounts/login/register/(?P<m_id>[a-z]{2}\d+)/',views.sign_in),
    re_path('accounts/login/review/(?P<m_id>[a-z]{2}\d+)/$',views.form_new),
    re_path(r'^(?P<gen>[A-z]+)/$',views.genre),
    path('trailers/all/',views.all_trailers),
    re_path('movie/type/(?P<mov_type>[A-z]+)/$',views.movieType),
    re_path('toprated/(?P<rate>[0-9]+)/$',views.topRated),
    ]
