from webapp.views import webappView
from django.urls import path
from rest_framework import routers
from django.urls import path, include
from .import views 
urlpatterns =[
    
    path('basic/',webappView.as_view(),name="Home"),
    path('auth/',include("rest_framework.urls")),
    path('deleteData/<int:id>',views.deleteData,name="delete"),
   
    path('record/<int:id>',views.updaterecord,name="updated"),
    path('addData/',views.addData,name='addData'),
    
]

rout =routers.SimpleRouter()
rout.register('student',views.StudentView,basename="student")
urlpatterns += rout.urls   
