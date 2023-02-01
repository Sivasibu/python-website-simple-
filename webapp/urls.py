from webapp.views import webappView
from django.urls import path
from rest_framework import routers
from django.urls import path, include
from .import views
urlpatterns =[
    
    path('basic/',webappView.as_view()),
    path('auth/',include("rest_framework.urls")),
    path('deleteData/<int:id>',views.deleteData,name='deleteData'),
   
    
]

rout =routers.SimpleRouter()
rout.register('student',views.StudentView,basename="student")
urlpatterns += rout.urls   
