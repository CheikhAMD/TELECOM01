from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.main),
    path('home/',views.home,name="home"),
    path('01',views.bouti_01,name="01"),
    path('02',views.bouti_02,name="02"),
    path('03',views.bouti_03,name="03"),
    path('04',views.bouti_04,name="04"),
    path('about',views.about,name="about")
    
]
