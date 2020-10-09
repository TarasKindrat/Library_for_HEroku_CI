from django.http import HttpResponse
from authentication.models import CustomUser
from order.models import Order
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewCustomUserForm


def index(request):
    return HttpResponse('<h1>Start for authentication</h1>')


def get_all_users(request):
    ul = list(CustomUser.get_all())
    return render(request, 'authentication/get_all.html', context={'users_list': ul, })


def get_user_by_id(request, id=0):

    user_found = CustomUser.get_by_id(id)
    ord = [order for order in list(Order.get_all()) if order.user.id == id]
    return render(request, 'authentication/get_user_by_id.html', context = {'user': user_found, 'orders': ord})


def user_delete(request, id=0):
    if request.method == 'POST':
        c_user = get_object_or_404(CustomUser, pk=id)
        c_user.delete_by_id(id)
        return redirect('/authentication/get_all/')
    else:
        return redirect('/authentication/get_all/')


def signup(request, id=0):
    from django.contrib.auth import login as auth_login
    # form = UserCreationForm(request.POST)
    # if form.is_valid():
    #     user = form.save()
    #     auth_login(request, user)
    #     return redirect('home')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'authentication/signup.html', {'form': form})

    if request.method == 'GET':
        if id == 0:
            form = NewCustomUserForm()

        else:
            user = get_object_or_404(CustomUser, pk=id)
            form = NewCustomUserForm(instance=user)
        return render(request, 'authentication/signup.html', {'form': form})
    else:
        if id == 0:
            form = NewCustomUserForm(request.POST)
        else:
            user = get_object_or_404(CustomUser, pk=id)
            form = NewCustomUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            print(auth_login(request, user))
            # Rerurn to list users
            return redirect('/authentication/get_all/')
        else:
            return render(request, 'authentication/signup.html', {'form': form})

def edit_user(request, id=0):

    if request.method == 'GET':
        if id == 0:
            form = NewCustomUserForm()

        else:
            c_user = get_object_or_404(CustomUser, pk=id)
            form = NewCustomUserForm(instance=c_user)
        return render(request, 'authentication/edit_user.html', {'form': form})
    else:
        if id == 0:
            form = NewCustomUserForm(request.POST)
        else:
            c_user = get_object_or_404(CustomUser, pk=id)
            form = NewCustomUserForm(request.POST, instance=c_user)
        if form.is_valid():
            form.save()
            # Rerurn to list users
            return redirect('/authentication/get_all/')
        else:
            return render(request, 'authentication/edit_user.html', {'form': form})






