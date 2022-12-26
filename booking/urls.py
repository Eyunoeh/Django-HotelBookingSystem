from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('book/', views.book, name='book'),
    path('booked', views.thankyouPage, name='thankyou'),
    path('book/booked/', views.checkIns, name='booked'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/delete_record/', views.update_delete_data, name='delete_record')
]
urlpatterns += staticfiles_urlpatterns()
