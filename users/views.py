from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully Created, {username}!')
            return redirect('/')
        else:
            messages.warning(request, f'Please enter valid credentials!')
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
