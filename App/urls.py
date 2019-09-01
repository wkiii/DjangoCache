from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^news/', views.news, name='news'),

    url(r'^jokes/', views.jokes, name='jokes'),

    url(r'^home/', views.home, name='home'),

    url(r'^getphone/', views.get_phone, name='get_phone'),

    url(r'^getticket/', views.get_ticket, name='get_ticket'),

    url(r'^search/', views.search, name='search'),

    url(r'^calc/', views.calc, name='calc'),

    url(r'^login/', views.login, name='login'),

    url(r'^addstudents/', views.add_students, name='add_students'),

    url(r'^getstudents/', views.get_students, name='get_students'),

    url(r'^getstudentswithpage/', views.get_students_with_page, name='get_students_with_page'),

    url(r'^getcode/', views.get_code, name='get_code'),
]