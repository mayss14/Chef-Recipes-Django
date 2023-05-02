from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
import services
from django.urls import reverse
# from . models import APIData
import json
import requests

from Recipes.models import Guest, Recipe, RecipeReview


def welcome_page(request):
    addrecipes()
    users = User.objects.all()
    for u in users:
        print(u)
    return render(request, 'index.html')
    users = Guest.objects.all()


# FONCTION QUI CONSOMME L API
def api_data(categorie):
    url = ('https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b' % (categorie))
    response = requests.get(url)

    data = response.json()
    list = []
    for i in range(10):
        list.append({
            'id': i,
            'name': data['hits'][i]['recipe']['label'],
            'image': data['hits'][i]['recipe']['image'],
            'ingredients': data['hits'][i]['recipe']['ingredientLines']
        })
    return list


# LIST DES DIFFERENTS CATEGORIES OU RECETTES POSSIBLES
dict = {
    0: ['vegetables', 'chicken', 'fish', 'sushi', 'rice', 'meat', 'spaghetti', 'risotto', 'tacos', 'kebab', 'lasagna',
        'ham', 'grilling', 'beans', 'peas'],
    1: ['tarte', 'cheesecake', 'pie', 'cake', 'muffins', 'cookies', 'pudding', 'macaroons', 'tiramisu', 'brownies',
        'crepes', 'shortcake'],
    2: ['salad', 'fries', 'sidedish', 'pizza', 'ratatouille', 'coleslaw', 'gratin', 'pilaf', 'cornbread', 'spinach',
        'mushrooms', 'couscous', 'macaroni']
}
'''Ramener les recettes de l'API et les mettre au niveau de la base de données'''


def addrecipes():
    if len(Recipe.objects.all()) == 0:
        categorie = 'vegetables'
        url = ('https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b' % (
            categorie))
        response = requests.get(url)
        data = response.json()
        for i in range(10):
            r = Recipe(None, data['hits'][i]['recipe']['label'])
            r.save()
    if len(Recipe.objects.all()) == 10:
        categorie = 'salad'
        url = ('https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b' % (
            categorie))
        response = requests.get(url)
        data = response.json()
        for i in range(10):
            r = Recipe(None, data['hits'][i]['recipe']['label'])
            r.save()
    if len(Recipe.objects.all()) == 20:
        categorie = 'dessert'
        url = ('https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b' % (
            categorie))
        response = requests.get(url)
        data = response.json()
        for i in range(10):
            r = Recipe(None, data['hits'][i]['recipe']['label'])
            r.save()
    recipes = Recipe.objects.all()
    for recipe in recipes:
        print(recipe)


def Search_rec(request, categorie):
    result = request.GET['keywords']
    list = api_data(result)

    if categorie == 'mainCourse':
        return render(request, categorie + '.html', {'list': list, 'keyword': result, 'keywords': dict[0]})
    elif categorie == 'dessert':
        return render(request, categorie + '.html', {'list': list, 'keyword': result, 'keywords': dict[1]})
    else:
        return render(request, categorie + '.html', {'list': list, 'keyword': result, 'keywords': dict[2]})


def main_course(request):
    return render(request, 'mainCourse.html', {'keywords': dict[0]})


def dessert(request):
    return render(request, 'dessert.html', {'keywords': dict[1]})


def side_dish(request):
    return render(request, 'sideDish.html', {'keywords': dict[2]})


# FONCTION POUR AFFICHER LES DETAILS
def card_detail(request, id, categorie):
    list = api_data(categorie)
    recipe = list[id]
    return render(request, 'card.html', {'recipe': recipe, 'categorie': categorie})


def about_us(request):
    return render(request, 'aboutus.html')


def signup(request):
    error = False
    message = ""
    if request.method == "POST":
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter a valid email address!"
            # password
        if error == False:
            if password != repassword:
                error = True
                message = "The passwords don't match each other!"
            # Exist
        user = User.objects.filter(Q(email=email) | Q(username=username)).first()
        if user:
            error = True
            message = f"A user with an  email {email} or username  {username} already exists'!"

        # register
        if error == False:
            user = User(
                username=username,
                email=email,
            )
            user.save()
            guest = Guest(None, username, email, password)
            guest.save()
            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('log')

    context = {
        'error': error,
        'message': message
    }
    return render(request, "signup.html", context)


'''AUTHENTIFICATION :'''


def log(request):
    message = ""
    error = False
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = User.objects.filter(username=username).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('home')
            else:
                error = True
                message = "Incorrect password, retry"
        else:
            error = True
            message = "Invalid credentiels"
    context = {
        'error': error,
        'message': message
    }
    return render(request, 'login.html', context)


'''DECONNEXION'''


def log_out(request):
    logout(request)
    return redirect('log')


'''RATE A RECIPE'''


def rate(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            namere = request.POST.get('recipe', None)
            '''print(namere)'''
            comment = request.POST.get('mssg', None)
            rate = request.POST.get('chx', None)
            recipe = Recipe.objects.filter(Q(name=namere)).first()
            if recipe ==None:
                recipe=Recipe(None,namere)
                recipe.save()
            '''print(user.username)
            print(recipe)'''
            review = RecipeReview(None,recipe.id,user.id,comment, rate)
            review.save()
            return render(request, 'index.html')

    else:
        return render(request, 'login.html')
