"""
URL configuration for Compuzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required



app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:id>', views.products, name="products"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('delete/<int:id>/', login_required(views.delete.as_view()), name='delete'),
    path('addproduct', login_required(views.add_product.as_view()),name='addproduct'),
    path('edit/<int:pk>', login_required(views.edit.as_view()),name='edit'),
    path('cat_list', views.cat_list, name='cat_list'),
    path('category/<str:category>/', views.cat_det, name='cat_det'),
]
# handler404 = 'views.custom_404'