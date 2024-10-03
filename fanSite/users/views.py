from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    '''Renders the registration page and redirects to login
      if registration is successful'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your account has been'
                             'created. You can log in now!')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
