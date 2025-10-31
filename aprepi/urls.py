from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('register_users/', views.register_users, name='register_users'),

    path('archive_user<int:id>/', views.archive_user, name='archive_user'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('reception_page/', views.reception_page, name='reception_page'),

    path('news_list/', views.news_list, name='news_list'),
    path('new_detail/<int:id>/', views.new_detail, name='new_detail'),
    path('testimonials_list', views.testimonials_list, name='testimonials_list'),
    path('testimonial_detail/<int:id>', views.testimonial_detail, name='testimonial_detail'),
    path('create_testimonial', views.create_testimonial, name='create_testimonial'),

    path('history/', views.history, name='history'),
    path('documents/', views.documents, name='documents'),
    path('ata/', views.ata, name='ata'),
    path('events/', views.events, name='events'),

    path('director/', views.director, name='director'),
    path('contribute/', views.contribute, name='contribute'),
]
 
