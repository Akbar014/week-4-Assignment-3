from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    # path('edit/<int:id>', views.edit_category, name='edit_category'),
    # path('delete/<int:id>', views.category, name='delete_category'),
]