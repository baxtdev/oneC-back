from django.shortcuts import render


from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets,permissions,generics,views
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
    
    def perform_create(self, serializer):
        serializer.save()
    
    



class UserInfoGETapiVew(generics.GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'user_id'
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        user_info_instance = self.get_object()
        serializer = self.serializer_class(user_info_instance)
        return Response(serializer.data)  



class ProcessDataAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        data_array = request.data
        for data in data_array:
            serializer = UserInfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        
        return Response({'message': 'Данные успешно сохранены'})