from rest_framework_mongoengine import serializers
from .models import AccountInfo

class DashboardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = AccountInfo
        fields = "__all__"