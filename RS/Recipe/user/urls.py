from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Customer
    path('register/', views.customerRegistrationView.as_view()),
    path('login/', views.userLogin.as_view()),
    #
    # #category
    path('postCategory/',views.categoryRecipe.as_view()),
    path('getCategory/',views.getAllcategory.as_view()),
    path('getCategory/<name>/',views.getAllcategoryByID.as_view()),
    #
    # #recipe
    path('postRecipe/',views.postRecipe.as_view()),
    path('getRecipe/', views.getAllRecipe.as_view()),
    path('getRecipe/<title>/',views.getAllRecipeBytitle.as_view()),
    path('updateRecipe/<RecipeId>/', views.updateRecipeById.as_view()),
    path('DeleteRecipe/<RecipeId>/', views.DeleteRecipeById.as_view()),

    #rataing
    path('postRateing/',views.postRateing.as_view()),
    path('getRataing/',views.getRataingAll.as_view()),
    path('getRataing/<rating>/',views.getRataing.as_view()),

    #review
    path('postReview/',views.postReview.as_view()),
    path('getReview/',views.getReviewall.as_view()),

    #search
    path('search/recipes/', views.SearchRecipes.as_view()),



]