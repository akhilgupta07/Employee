from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Employee_Form,name='create'),
    path('<int:id>/',views.Employee_Form, name ='update'),
    path('list/',views.Employee_List,name='read'),
    path('delete/<int:id>/',views.Employee_Delete, name = 'delete')
   
]