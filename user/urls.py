from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('result',views.result,name='result'),
    path('add',views.add, name='result'),
    path('final',views.final, name='final')
    
    

]