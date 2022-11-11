from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# for all CBV models
from django.views import generic

"""Recipe Collection"""
def home(request):
    return render(request, 'home.html')

@login_required
def recipe_collection_index(request): 
    # grab API data, pass in object
    return render(request, 'recipe_collections/index.html')

# create recipe collection

# update recipe collection

# delete recipe collection

"""CRUD for Recipes"""
# 


"""OAuth Functions"""
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
