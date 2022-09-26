from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('product/<int:product_id>/<slug:product_slug>/', views.show_product, name='product_detail'),
    path('cart', views.show_cart , name='show_cart'),
    path('signout', views.signout, name='signout'),
    path('checkout/', views.checkout, name='checkout'),
]
