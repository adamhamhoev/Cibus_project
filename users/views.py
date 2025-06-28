from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Сразу же входим под его именем
            return redirect('dish_list')  # Перенаправляем на главную
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})