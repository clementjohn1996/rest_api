from django.urls import path
from .import views

urlpatterns = [ 
    path('',views.APIoverview),
    path('emplist/',views.EmpList,name="emplist"),
    path('empcreate/',views.EmpCreate,name="empcreate"),
    path('empupdate/<int:pk>/',views.EmpUpdate,name="empupdate"),
    path('empdelete/<int:pk>/',views.EmpDelete,name="empdelete"),
]