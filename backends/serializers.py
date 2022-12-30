from rest_framework import serializers
from .models import Post, customuser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .name_validator import name_valid
from rest_framework.validators import ValidationError


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		token['username'] = user.username

		return token



class MycustomUserSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(required = True, style={'input_type': 'password'})

	class Meta:
		model = customuser
		fields = ['username', 'email', 'password', 'password2']

	def validate(self, attrs):
		password = attrs.get('password')
		password2 = attrs.pop('password2')
		if password2 != password:
			raise ValidationError('password Does not  match')
		return attrs


class PasswordChangeSerializer(serializers.ModelSerializer):
	old_password = serializers.CharField(write_only = True, style = {'input_type': 'password'}, max_length=30)
	new_password = serializers.CharField(write_only = True, style = {'input_type': 'password'}, max_length=30)
	confirm_password = serializers.CharField(write_only = True, style = {'input_type': 'password'}, max_length=30)

	class Meta:
		model = customuser
		fields = ['old_password', 'new_password', 'confirm_password']

	def validate(self, data):
		old_password = data['old_password']
		new_password = data['new_password']
		confirm_password = data['confirm_password']
		if confirm_password != new_password:
			raise ValidationError('confirm password does not match to new password')

		return data



class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = customuser
		fields = ['id','username', 'email']
