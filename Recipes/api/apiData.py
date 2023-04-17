import json
import requests

response = requests.get('https://api.edamam.com/search?q=vegetables&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b')
data = response.json()

name_list =[]
images = []
ing_list = []

for i in range(5):
    name=data['hits'][i]['recipe']['label']
    img=data['hits'][i]['recipe']['image']
    ing=data['hits'][i]['recipe']['ingredientLines']
    name_list.append(name)
    images.append(img)
    ing_list.append(ing)

