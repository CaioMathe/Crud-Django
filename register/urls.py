from django.urls import path
from register.views import list_registered, create_register, update_register, delete_register

urlpatterns = [
    path('', list_registered, name='list_registered'),
    path('Registro', create_register, name='create_register'),
    path('update/<int:id>', update_register, name='update_register'),
    path('delete/<int:id>', delete_register, name='delete_register')

]