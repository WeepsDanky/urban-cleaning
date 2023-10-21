from django.db import models

class Camera(models.Model):
    gps_location = models.CharField(max_length=255)
    trash_amount = models.FloatField()

    class Meta:
        app_label = "cameras"


class Depot(models.Model):
    gps_location = models.CharField(max_length=255)
    
    class Meta:
        app_label = "cameras"


class Route(models.Model):
    
    class Meta:
        app_label = "cameras"


class Waypoint(models.Model):
    route = models.ForeignKey(Route, related_name="waypoints", on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    gps_location = models.CharField(max_length=255)
    #camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    class Meta:
        app_label = "cameras"
        ordering = ['order']
