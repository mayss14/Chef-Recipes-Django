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
    path('recipes/signup/', signup, name="signup"),
    path('recipes/login', log, name="log"),
    path('recipes/logout', log_out, name="log_out"),
    path('recipes/rate', rate, name="rate")

]