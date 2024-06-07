from rest_framework import serializers



class CustomerSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()


class userLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=False, allow_blank=True, default='')
    password = serializers.CharField(max_length=100)


class CategorySerializer(serializers.Serializer):
    categoryName = serializers.CharField(max_length=100, )


class categoryRecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.JSONField()
    ingredients = serializers.JSONField()
    preparation_steps = serializers.JSONField()
    cooking_time = serializers.IntegerField()
    serving_size = serializers.IntegerField()
    CategoryName = serializers.CharField(max_length=100)
    user = serializers.CharField(max_length=100)


class UpdateRecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100,required=False)
    description = serializers.JSONField(required=False)
    ingredients = serializers.JSONField(required=False)
    preparation_steps = serializers.JSONField(required=False)
    cooking_time = serializers.IntegerField(required=False)
    serving_size = serializers.IntegerField(required=False)




class RatingSerializer(serializers.Serializer):
    RecipeId = serializers.CharField(max_length=100)
    rating = serializers.IntegerField()
    user = serializers.CharField(max_length=100)


class ReviewSerializer(serializers.Serializer):
    RecipeId = serializers.CharField(max_length=100)
    text = serializers.JSONField()
    user = serializers.CharField(max_length=100)
