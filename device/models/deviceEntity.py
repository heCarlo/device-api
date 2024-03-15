from django.db import models

class DeviceEntity(models.Model):
    sensor = models.BooleanField(default=False)
    button = models.BooleanField(default=False)
    robot_on = models.BooleanField(default=False)
    reset_counter = models.BooleanField(default=False)
    count_value = models.IntegerField(default=0)
