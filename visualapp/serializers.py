from rest_framework import serializers
from .models import Post
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset = CustomUser.objects.all())])
    password1 = serializers.CharField(required=True,write_only=True,validators=[validate_password])
    password2 = serializers.CharField(required=True,write_only=True,validators =[validate_password])

    class Meta:
        model = CustomUser
        fields=('email','user_name','first_name','password1','password2')
        extra_kwargs = {
            'first_name':{'required':True}
        }
    
    def validate(self,attrs):
        if(attrs['password1'] != attrs['password2']):
            raise serializers.ValidationError({"password1":"Password field didn't match"})
        return attrs

    def create(self,validated_data):
        user = CustomUser.objects.create(
            email= validated_data['email'],
            user_name = validated_data['user_name'],
            first_name = validated_data['first_name']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user

