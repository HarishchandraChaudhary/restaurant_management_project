from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home_page_view,name='home')
]