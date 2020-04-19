from rest_framework import routers
from .api import UserViewSet, VehicleViewSet, LogViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/vehicles', VehicleViewSet, 'vehicles')
router.register('api/logs', LogViewSet, 'logs')

urlpatterns = router.urls
