from rest_framework import viewsets
from .serializer import CarSerializer
from .models import Car

# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
  queryset = Car.objects.all().order_by('name')
  serializer_class = CarSerializer