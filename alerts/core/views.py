from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer, UserChangePasswordSerializer, \
    UserAlertSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import CoinAlert
from core.serializers import CoinAlertSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#     })

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    # renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    # renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
            print(username, password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}},
                                status=status.HTTP_404_NOT_FOUND)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUser(APIView):

    def get(self, request, format=None):
        return Response({'user': str(request.user)})


class UserChangePasswordView(APIView):
    # renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)


class UserAlertView(APIView):

    def post(self, request, format=None):
        serializer = UserAlertSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                print(serializer.validated_data)
                serializer.create(serializer.validated_data)
                token = get_tokens_for_user(user)
                return Response({'token': token, 'status': 'alert added'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}},
                                status=status.HTTP_404_NOT_FOUND)
            # return Response({'data': serializer.data})
        return Response({'error': serializer.errors})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = []
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AlertViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = CoinAlert.objects.all()
    serializer_class = CoinAlertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlertsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CoinAlertSerializer(data=request.data)



# class AlertDetail(generics.RetrieveAPIView):
#     queryset = CoinAlert.objects.all()
#     serializer_class = CoinAlertSerializer
#
#
# class AlertList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     serializer_class = CoinAlertSerializer
#     # renderer_classes = [renderers.StaticHTMLRenderer]
#
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return CoinAlert.objects.all()
#         return CoinAlert.objects.filter(created_by=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)


# class AlertList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = CoinAlert.objects.all()
#     serializer_class = CoinAlertSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
