from django.shortcuts import render,redirect
import services
from django.urls import reverse
#from . models import APIData
import json
import requests




def welcome_page(request):
    return render(request, 'index.html')

#FONCTION QUI CONSOMME L API
def api_data(categorie):
    url = ('https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b' % (categorie))
    response = requests.get(url)

    data = response.json()
    list = []
    for i in range(10):
        list.append({
            'id' : i,
            'name': data['hits'][i]['recipe']['label'],
            'image': data['hits'][i]['recipe']['image'],
            'ingredients': data['hits'][i]['recipe']['ingredientLines']
        })
    return list

#LIST DES DIFFERENTS CATEGORIES OU RECETTES POSSIBLES
dict ={
       0:['vegetables','chicken', 'fish', 'sushi', 'rice','meat','spaghetti','risotto','tacos','kebab','lasagna','ham','grilling','beans','peas'],
       1:['tarte', 'cheesecake', 'pie', 'cake', 'muffins','cookies','pudding','macaroons','tiramisu','brownies','crepes','shortcake'],
       2: ['salad','fries','sidedish','pizza','ratatouille','coleslaw','gratin','pilaf','cornbread','spinach','mushrooms','couscous','macaroni']
       }


def Search_rec(request,categorie):
    result=request.GET['keywords']
    list = api_data(result)

    if categorie == 'mainCourse':
        return render(request, categorie+'.html', {'list': list,'keyword':result,'keywords' : dict[0]})
    elif categorie == 'dessert':
        return render(request, categorie + '.html', {'list': list, 'keyword': result, 'keywords': dict[1]})
    else:
        return render(request, categorie + '.html', {'list': list, 'keyword': result, 'keywords': dict[2]})


def main_course(request):
    return render(request, 'mainCourse.html',{'keywords' : dict[0]})

def dessert(request):
    return render(request, 'dessert.html' , {'keywords' : dict[1]})

def side_dish(request):
    return render(request, 'sideDish.html',{'keywords' : dict[2]})

#FONCTION POUR AFFICHER LES DETAILS
def card_detail(request,id,categorie):
    list = api_data(categorie)
    recipe = list[id]
    return render(request,'card.html',{'recipe': recipe,'categorie':categorie})


def about_us(request):
    return render(request, 'aboutus.html')










