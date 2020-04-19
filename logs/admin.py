from django.contrib import admin
from .models import User, Vehicle, Log


admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Log)
