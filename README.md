# Chef-Recipes-Django
# Chef-Recipes-Django
Contexte général du projet du projet : Un site web de recettes de cuisine en utilisant le framework Django comme outil de developpement et le framework Bootstrap pour le front.
Conception :
******************************************************Spécifications Fonctionnelles************************************************
* On dispose d'un admin qui a son propre dashboard pour controller les utilisateurs ajoutés et leur filtrer par permission , etc  *
* Il y a les visiteurs qui doit s'authentifier pour evaluer une recette particulière.                                             *
* Un utilisateur doit etre inscrit avant de s'authentifier.                                                                       *
* La consultation des recettes est ouverte pour tout le monde.                                                                    *         
* L'utilisateur peut chercher les recettes  par catégories : (main Course, dessert ,Side dish)                                    *
* L'utilisateur peut chercher les recettes  par mots clés : (nom d'ingrédients ou nom du plat)                                    *
***********************************************************************************************************************************
****************************************************Acteurs du site****************************************************************
* Visiteur : peut naviguer sur le site et meme voir les recettes et lire les ingrédients.                                         *
* Membre   : fait partie de la communauté des utilisateurs du site ( C'est un visiteur authentifié). , il est identifié par       *
*  son username et son mot de passe ainsi que son email mais il utilise juste les deux premiers identifiants pour se connecter.   *
* Admin    : il peut voir les utilisateurs crées , leur statut, changer leur mot de passe etc...                                  *
***********************************************************************************************************************************
***********************************************Règles de gestion*******************************************************************
* Un membre peut evaluer un ou plusieurs recette  avec une note entre 1 et 5 et un commentaire .                                  *
* Une recette peut avoir un ou plusieurs ingrédients.                                                                             *
* Toute recette appartient à une catégorie particulière ( side dish, dessert ou main course).                                     *
* *********************************************************************************************************************************
*********************************************Spécifications techniques*************************************************************
* API : https://api.edamam.com/search?q=%s&app_id=5356d460&app_key=000e634ee221f3cc3fe235e57022402b / keyword: il permet de       *  
* retourner une liste de recettes par mots-clés.                                                                                  *
* Base de données : SqlLite pour stocker les recettes , les utilisateurs et les avis.                                             *    
* Choix technologique : Django et Bootstrap et Font Awesome.                                                                      *
* Usage du package django.contrib.auth pour manipuler les utilisateurs et le login,logout,django.core.validators pour valider les *
* emails ainsi que django.db.models pour utiliser le queryset dans des requetes spécifiques                                       *
* Le package requests et json pour consommer les données de l'API.                                                                *
* *********************************************************************************************************************************
**********************************************Models*******************************************************************************
* Recipe : pour representer une recette ayant un nom et un id.                                                                    *
* API_Data: classe intermédiaire pour ramener les informations de l'api ayant trois champs : nom , image et ingrédients.          *
* Guest : l'utilisateur ayant un username, mot de passe et email.                                                                 *
* User est aussi utilisé (proposé par défaut par django).                                                                         *
* RecipeReview: pour stocker les evaluations de recette (note, commentaire).                                                      *
***********************************************************************************************************************************
*********************************************Templates*****************************************************************************
* Page d'accueil : ayant les catégories de recettes disponibles.                                                                  *
* Page about us  : pour expliquer le contenu du site.                                                                             *
* Page login pour l'authentification et une autre signup pour l'inscription.                                                      *
* Page Carddetails: pour afficher les details d'une recette.                                                                      *
* Page Sidedish, dessert et maincourse pour chercher et afficher les recettes de chaque categorie                                 *
***********************************************************************************************************************************
*********************************************URLS**********************************************************************************
*    path('recipes/', welcome_page, name="home")=> page d'accueil                                                                 *
*   path('recipes/maincourse/', main_course, name="maincourse")=> recettes de plats principaux                                    *
*    path('recipes/dessert/', dessert, name="dessert")=> recettes de dessert                                                      * 
*    path('recipes/sideDish/', side_dish, name="sideDish")=> recettes d'entrées                                                   *
*    path('recipes/details/<slug:categorie>/<int:id>/', card_detail, name="cardDetail")=> details de recettes                     *
*    path('search/<slug:categorie>',Search_rec,name="search")=> recherche par nom ou ingrédients (mots clés)                      *
*    path('recipes/aboutus', about_us, name="aboutus")=> page à propos                                                            *
*    path('recipes/signup/', signup, name="signup")=> formulaire d'inscription                                                    *
*    path('recipes/login', log, name="log")=> page d'auhentification                                                              *
*    path('recipes/logout', log_out, name="log_out")=> deconnexion                                                                *
*    path('recipes/rate', rate, name="rate") => formulaire de notes                                                               *
***********************************************************************************************************************************



