from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.db.models import Q


class customerRegistrationView(APIView):
    def post(self, request):
        try:
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data['username']
                email = serializer.data['email']
                mobile = serializer.data["mobile"]
                password = serializer.data["password"]

                User.objects.create_user(username=username,password=password, email=email)
                data = User.objects.filter(username=username).values()[0]
                id = data["id"]

                Customer.objects.create(
                    cSid_id=id,
                    username=username,
                    password=password,
                    mobile=mobile,
                    email=email

                )
                data = {'Message': "Employee Create Successfully"}
                return JsonResponse(data, safe=False)
            return JsonResponse(serializer.errors, safe=False)
        except Exception as e:
            return JsonResponse(str(e), safe=False)


class userLogin(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = userLoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']

                data = User.objects.filter(email=email).values()[0]

                username = data["username"]
                print("username===",username)

                tokenData = Token.objects.filter(user_id=data["id"]).values()[0]
                print(tokenData)
                finaltoken = {
                            "token": tokenData["key"]
                        }
                return JsonResponse({
                    'status': 200,
                    'message': "Login Successful",
                    'token': finaltoken,

                    })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'data': "Username & Password Not Correct"
            })


class categoryRecipe(APIView):
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                categoryName = serializer.data['categoryName']

                Category.objects.create(categoryName=categoryName)

                return JsonResponse({
                    'status': 200,
                    'message': "category create Successfully"
                })
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class getAllcategory(APIView):
    def get(self, request,):
        try:
            data = list(Category.objects.filter().values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class getAllcategoryByID(APIView):
    def get(self, request,name):
        try:
            data = list(Category.objects.filter(name=name).values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class postRecipe(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = categoryRecipeSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data["title"]
                description = serializer.data["description"]
                ingredients = serializer.data["ingredients"]
                preparation_steps = serializer.data["preparation_steps"]
                cooking_time = serializer.data["cooking_time"]
                serving_size = serializer.data["serving_size"]
                CategoryName = serializer.data["CategoryName"]
                user = serializer.data["user"]
                data = User.objects.filter(username=user).values()[0]
                x = data["id"]
                print(x)
                Recipe.objects.create(
                    title=title,
                    description=description,
                    ingredients=ingredients,
                    preparation_steps=preparation_steps,
                    cooking_time=cooking_time,
                    serving_size=serving_size,
                    CategoryName_id=CategoryName,
                    user_id=x
                )
                return JsonResponse({
                    'status': 200,
                    'data': "Recipe create Sucessfully"
                })
            return JsonResponse({
                'status': 400,
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class getAllRecipe(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,):
        try:
            data = list(Recipe.objects.filter().values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class getAllRecipeBytitle(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,title):
        try:
            data = list(Recipe.objects.filter(title=title).values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class getAllRecipeBytitle(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,title):
        try:
            data = list(Recipe.objects.filter(title=title).values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class updateRecipeById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request,RecipeId):
        try:
            serializer = categoryRecipeSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data["title"]
                description = serializer.data["description"]
                ingredients = serializer.data["ingredients"]
                preparation_steps = serializer.data["preparation_steps"]
                cooking_time = serializer.data["cooking_time"]
                serving_size = serializer.data["serving_size"]

                Recipe.objects.filter(RecipeId=RecipeId).update(
                    title=title,
                    description=description,
                    ingredients=ingredients,
                    preparation_steps=preparation_steps,
                    cooking_time=cooking_time,
                    serving_size=serving_size,
                )
            return JsonResponse({
                'status': 200,
                'data': "Recipe Update Sucessfully"
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class DeleteRecipeById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, RecipeId):
        try:
            serializer = categoryRecipeSerializer(data=request.data)
            if serializer.is_valid():
                Recipe.objects.filter(RecipeId=RecipeId).delete(RecipeId=RecipeId)

            return JsonResponse({
                'status': 200,
                'data': "Recipe Delete Sucessfully"
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class postRateing(APIView):

    def post(self, request):
        try:
            serializer = RatingSerializer(data=request.data)
            if serializer.is_valid():
                RecipeId = serializer.data["RecipeId"]
                rating = serializer.data["rating"]
                user=serializer.data["user"]
                user = User.objects.filter(username=user).values()[0]
                y = user['id']

                Rating.objects.create(
                    RecipeId_id=RecipeId,
                    rating=rating,
                    user_id=y

                )
                return JsonResponse({
                    'status': 200,
                    'data': "Rating create Sucessfully"
                })
            return JsonResponse({
                'status': 200,
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })
class getRataingAll(APIView):
    def get(self, request,):
        try:
            data = list(Rating.objects.filter().values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })

class getRataing(APIView):
    def get(self, request,rating):
        try:
            data = list(Rating.objects.filter(rating=rating).values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data':data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class postReview(APIView):

    def post(self, request):
        try:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                RecipeId = serializer.data["RecipeId"]
                text = serializer.data["text"]
                user = serializer.data["user"]
                user = User.objects.filter(username=user).values()[0]["id"]
                Review.objects.create(
                    RecipeId_id=RecipeId,
                    text=text,
                    user_id=user

                )
            return JsonResponse({
                'status': 200,
                'data': "Review create Sucessfully"
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class getReviewall(APIView):
    def get(self, request, ):
        try:
            data = list(Review.objects.filter().values())
            print(data)
            return JsonResponse({
                'status': 200,
                'data': data
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class SearchRecipes(APIView):
    permission_classes = [AllowAny]  # Allow any user, authenticated or not

    def get(self, request):
        try:
            title = request.GET.get('title', '')
            description = request.GET.get('description', '')
            ingredients = request.GET.get('ingredients', '')
            CategoryName = request.GET.get('CategoryName', '')

            filters = Q()
            if title:
                filters &= Q(title__icontains=title)
            if description:
                filters &= Q(description__icontains=description)
            if ingredients:
                filters &= Q(ingredients__icontains=ingredients)
            if CategoryName:
                filters &= Q(CategoryName__icontains=CategoryName)

            if filters:
                recipes = Recipe.objects.filter(filters)
                serializer = categoryRecipeSerializer(recipes, many=True)
                return JsonResponse({
                    'status': 200,
                    'data': serializer.data,
                })
            else:
                return JsonResponse({
                    'status': 400,
                    'message': 'No search criteria provided'
                })
        except Exception as e:
            return JsonResponse({
                'status': 400,
                'message': 'Something went wrong',
                'error': str(e)
            })