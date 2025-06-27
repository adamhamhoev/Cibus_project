from django.urls import path
from . import views

urlpatterns = [

    path('',views.dish_list_view, name = 'dish_list'),
    
    path('dish/<int:dish_id>/', views.dish_detail_view, name = 'dish_detail'),    
]