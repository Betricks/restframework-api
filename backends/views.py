from .models import Post
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PostSerializer, MyTokenObtainPairSerializer, MycustomUserSerializer, UserListSerializer, PasswordChangeSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import redirect
from .models import customuser

from rest_framework_simplejwt.tokens import RefreshToken

class PasswordChangeAPIVew(APIView):
	def put(self, request):
		password_ser = PasswordChangeSerializer(data = request.data )
		if password_ser.is_valid():
			old_password = password_ser.data.get('OldPassword')
			if not self.object.check_password(old_password):
				return Response({"old_password": ['wrong password. ']})
			self.object.set_password(password_ser.data.get('NewPassword'))
			self.object.save()
			return Response({'message': 'seccesfully changed your password'}, status = status.HTTP_201_CREATED)
		return Response({'message': 'invalid user'}, status = status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


class MycustomUserView(APIView):
	def post(self, request):
		if request.method == 'POST':
			serializer = MycustomUserSerializer(data=request.data)
			data = {}
			if serializer.is_valid():
				user = serializer.save()
				data = {
				'message' : 'this account was created seccesfully',
				'username': request.data['username']
						}
				return Response(data, status = status.HTTP_201_CREATED)
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
	def get(self, request):
		datas = customuser.objects.all()
		serializer = UserListSerializer(datas, many=True)
		return Response(serializer.data)

class UserDetailView(APIView):
	def get(self, request, pk):
		if request.method == 'GET':
			data = customuser.objects.get(username=pk)
			if data is not None:
				serializer = UserListSerializer(data)
				return Response(serializer.data)
			data = 'this user does not exists'
			return Response(data)


class UserDeleteView(APIView):
	def delete(self, request, pk):
		if request.method == 'DELETE':
			data = customuser.objects.get(username = pk)
			if data == request.user:
				data.remove()
				message = 'deleted seccesfully'
				return Response(message, status= status.HTTP_202_ACCEPTED)
			message = "unauthorized you can't delete this user you are not admin"
			return Response(message, status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)



class PostList(APIView):
	def get(self, request):
		datas = Post.objects.all()
		serializer = PostSerializer(datas, many=True)
		return Response(serializer.data)

	def post(self, request):
		if request.method == 'POST':
			serializer = PostSerializer(data = request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def update(self, request):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_SECCESS)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
