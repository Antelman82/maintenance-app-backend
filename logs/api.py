from logs.models import Log, User, Vehicle
from rest_framework import viewsets, permissions
from .serializers import LogSerializer, UserSerializer, VehicleSerializer
from django.conf import settings
# from django.core.files.storage import FileSystemStorage


# Log Viewset
class LogViewSet(viewsets.ModelViewSet):
    # queryset = Log.objects.all()
    permission_classes = [
        # permissions.AllowAny
        permissions.IsAuthenticated
    ]
    serializer_class = LogSerializer

    def get_queryset(self):
        return Log.objects.all()


# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.filter(username=self.request.user)
    permission_classes = [
        # permissions.AllowAny
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_queryset(self): 
        return User.objects.filter(username=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def image_upload(request):
    #     if request.method == 'POST':
    #     image_file = request.FILES['image_file']
    #     image_type = request.POST['image_type']
    #     if settings.USE_S3:
    #         upload = Upload(file=image_file)
    #         upload.save()
    #         image_url = upload.file.url
    #     else:
    #         fs = FileSystemStorage()
    #         filename = fs.save(image_file.name, image_file)
    #         image_url = fs.url(filename)
    #     return render(request, 'upload.html', {
    #         'image_url': image_url
    #     })
    # return render(request, 'upload.html')

# Vehicle Viewset
class VehicleViewSet(viewsets.ModelViewSet):
    # queryset = Vehicle.objects.all()
    permission_classes = [
        # permissions.AllowAny
        permissions.IsAuthenticated
    ]
    serializer_class = VehicleSerializer

    def get_queryset(self):
        print(self.request.user.id)
        user = self.request.user.id
        return Vehicle.objects.filter(user=user)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.vehicle)


