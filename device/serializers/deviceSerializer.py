from rest_framework import serializers
from ..models.deviceEntity import DeviceEntity

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceEntity
        fields = ['id', 'sensor', 'button', 'robot_on', 'reset_counter', 'count_value']
