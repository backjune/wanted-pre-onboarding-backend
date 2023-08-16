from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from .models import User
from .serializers import UserSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSigninView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if '@' not in email:
            error_msg = "This field may not be blank." \
                if len(email) == 0 else 'Email must contain the @ symbol.'

            return Response({'email': error_msg},
                            status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 8:
            error_msg = "This field may not be blank." \
                if len(password) == 0 else 'Password must be at least 8 characters long.'

            return Response({'password': error_msg},
                            status=status.HTTP_400_BAD_REQUEST)

        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):  # 비밀번호 검증
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            payload.pop("username")
            token = jwt_encode_handler(payload)
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'The email or password is incorrect.'},
                            status=status.HTTP_401_UNAUTHORIZED)
