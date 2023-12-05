from rest_framework import routers, serializers

from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("user_id","created_at","company","full_name","credit")