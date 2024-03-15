from django.urls import path
from .views.deviceView import DeviceCreateAPIView

urlpatterns = [
    path('device/create/', DeviceCreateAPIView.as_view(), name='device-create'),
]
