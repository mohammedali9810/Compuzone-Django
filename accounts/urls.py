from django.urls import include,path
from .views import Delus, Userdet,loginredirect,Crus,editus,logoutredirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('', include('django.contrib.auth.urls'),name='authen'),
    path('register/', Crus.as_view(),name='register'),
    path('userprofile/<int:pk>', login_required(Userdet.as_view()),name='userdetails'),
    path('loginredirect/',loginredirect,name='loginredirect'),
    path('edituser/<int:pk>',login_required(editus.as_view()),name='edituser'),
    path('deleteuser/<int:pk>',login_required(Delus.as_view()),name='deleteuser'),
    # path('logoutredirect/', logoutredirect, name='logoutredirect')
]