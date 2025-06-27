from django.shortcuts import render
from .models import Dishes as Dish

def dish_list_view(request):
    
    all_dishes = Dish.objects.all()
    
    context = {
       'dishes': all_dishes,  
    }
    
    
    return render(request, 'dishes/dish_list.html', context)



def dish_detail_view(request, dish_id):
    
    one_dish = Dish.objects.get(id = dish_id)
    
    context = {
        'dish': one_dish,
    }
    
    return render(request, 'dishes/dish_detail.html', context )