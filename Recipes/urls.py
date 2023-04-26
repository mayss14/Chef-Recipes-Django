from django.urls import path
from .views import *


urlpatterns = [
    path('recipes/', welcome_page, name="home"),
    path('recipes/maincourse/', main_course, name="maincourse"),
    path('recipes/dessert/', dessert, name="dessert"),
    path('recipes/sideDish/', side_dish, name="sideDish"),
    path('recipes/details/<slug:categorie>/<int:id>/', card_detail, name="cardDetail"),
    path('search/<slug:categorie>',Search_rec,name="search"),
    path('recipes/aboutus', about_us, name="aboutus"),

]