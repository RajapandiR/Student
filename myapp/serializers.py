from rest_framework import serializers

from myapp import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = '__all__'

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentMarkModel
        fields = '__all__'