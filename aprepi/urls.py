from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('register_users/', views.register_users, name='register_users'),
    path('list_users/', views.list_users, name='list_users'),
    path('update_user<int:id>/', views.update_user, name='update_user'),
    path('delete_user<int:id>/', views.delete_user, name='delete_user'),
    path('archive_user<int:id>/', views.archive_user, name='archive_user'),

    path('list_patients/', views.list_patients, name='list_patients'),

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
]
 
