from django.urls import path
from .views import index
from .import views

 app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path()
    path('about/',views.about, name='about'),
    path('menu/',views.menu,name='menu'),
    path('contact/',views.contact, name='contact')
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('reservation/',views.reservation_views, name='reservation'),
    path('success/',views.contact_success, name='success_page'),
    path('api/categories/',MenuCategoryListAPIView.as_view(),name='category-list'),
    path(
        'contact/submit/',
        ContactFormSubmissionCreateView.as_view(),
        name='contact-submit-api'
    ),
]