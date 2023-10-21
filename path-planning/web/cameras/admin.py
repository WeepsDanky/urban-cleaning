from django.contrib import admin

from .models import Camera, Depot, Route, Waypoint

admin.site.register(Camera)
admin.site.register(Depot)

# preliminary
admin.site.register(Route)
admin.site.register(Waypoint)
