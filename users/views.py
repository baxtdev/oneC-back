from django.shortcuts import render


from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets,permissions,generics
from rest_framework.response import Response

from .models import UserInfo
from .serializers import UserInfoSerializer

class UserInfoAPIViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs=[]
        return qs 


class UserInfoGETapiVew(generics.GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'user_id'
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        user_info_instance = self.get_object()
        serializer = self.serializer_class(user_info_instance)
        return Response(serializer.data)  
