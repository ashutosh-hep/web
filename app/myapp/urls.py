from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('',views.sign, name="sign"),
   path('postsign',views.postsign, name="postsign"),
   path('logout',views.logout, name="logout"),
   path('up',views.up, name="up"),
   path('postup',views.postup, name="postup"),
   path('fp',views.fp, name="fp"),
   path('postfp',views.postfp, name="postfp"),
   path('create',views.create, name="create"),
   path('postcreate',views.postcreate, name="postcreate"),
   path('existing',views.existing, name="existing"),
   path('pe',views.pe, name="pe"),
   path('delete',views.delete, name="delete"),
   path('cancelsignup',views.cancelsignup, name="cancelsignup")

]
