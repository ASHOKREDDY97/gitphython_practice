from django.urls import path
from . import views

urlpatterns = [
    path('employees_list', views.employees_list, name='employees_list'),
    path('create_employee', views.create_employee, name='create_employee'), 
    path('edit_employee/<int:pk>', views.edit_employee, name='edit_employee'),
    path('destroy/<int:pk>', views.destroy, name='destroy'),
    # path('', views.sending_mail, name='sending_mail'),
    path('', views.send_email, name='send_email'),
]
