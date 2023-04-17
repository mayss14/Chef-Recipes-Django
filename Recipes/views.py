from django.shortcuts import render
from . models import APIData
import json
import requests





def api_data(categorie):
    url = ('https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b' % (categorie))
    response = requests.get(url)

    data = response.json()
    list = []
    for i in range(6):
        list.append({
            'id' : i,
            'name': data['hits'][i]['recipe']['label'],
            'image': data['hits'][i]['recipe']['image'],
            'ingredients': data['hits'][i]['recipe']['ingredientLines']
        })
        ingredients= data['hits'][i]['recipe']['ingredientLines']
        ing=""
        for x in ingredients:
            ing+=x
        row = APIData(
            recipe_name= data['hits'][i]['recipe']['label'],
            recipe_img = data['hits'][i]['recipe']['image'],
            recipe_ing = ing
        )
        row.save()

    return list



def welcome_page(request):
    return render(request, 'index.html')



def main_course(request):
    list = api_data('vegetables')
    return render(request, 'mainCourse.html', {'list' : list})

def Search_rec(request):
    query = request.GET.get('keyword')

    return render(request, 'mainCourse.html', {'list': liste})


def dessert(request):
    list = api_data('dessert')
    return render(request, 'dessert.html' , {'list' : list})

def side_dish(request):
    list = api_data('salad')
    return render(request, 'sideDish.html', {'list' : list})

def card_detail(request,id):
    list = api_data('vegetables')
    recipe = list[id]
    return render(request,'card.html',{'recipe': recipe})

