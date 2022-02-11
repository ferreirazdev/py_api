from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    db_table = 'car'
    model = Car
    fields = ('name', 'year')