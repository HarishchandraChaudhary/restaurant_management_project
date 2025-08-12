from django.urls import path
from .views import index
from .import views


urlpatterns = [
    path('',index,name='home'),
    path('about/',views.about, name='about'),
    
    path('404/',views.404,name='404'),
]