from django.shortcuts import render

from rest_framework.views import APIView, Response
from rest_framework import status
# Create your views here.

from myapp import serializers, models


class StudentAPI(APIView):
    serializer_class = serializers.StudentSerializer
    
    def get(self, request, format = None):
        obj = models.StudentModel.objects.all()
        serializer = serializers.StudentSerializer(obj, many =True)
        print(serializer)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = f'Create Successfull'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

class StudentMarkAPI(APIView):
    serializer_class = serializers.StudentMarkSerializer

    def get(self, request):
        obj = models.StudentMarkModel.objects.all()
        serializer = serializers.StudentMarkSerializer(obj, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            message = f'Create Successfull'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )


class StudentMarkAPI1(APIView):
    serializer_class = serializers.StudentMarkSerializer

    def get_object(self, pk):
        try:
            return models.StudentMarkModel.objects.get(pk=pk)
        except models.StudentMarkModel.DoesNotExist:
            return Response({'message': "The Student does not exist"})
        
    def get(self, request, pk):
        stud = self.get_object(pk)
        serializer = serializers.StudentMarkSerializer(stud)
        return Response(serializer.data)


class Result(APIView):
    def get(self, request):
        data = []
        
        a = b = c = d = e = f= 0
        stud = models.StudentModel.objects.count()
        data.append({"Total No of Student": stud})
        mark = models.StudentMarkModel.objects.all()
        for i in mark:
            if i.mark <= 100 and i.mark >= 91:
                a = a + 1
            elif i.mark <= 90 and i.mark >= 81:
                b = b + 1
            elif i.mark <= 80 and i.mark >= 71:
                c = c + 1
            elif i.mark <= 70 and i.mark > 61:
                d = d + 1
            elif i.mark <= 61 and i.mark >= 55:
                e = e + 1
            else:
                f = f + 1 
        dic =  (a/stud)*100
        first = ((b+c)/stud) * 100
        passing =  ((stud-f)/stud) * 100 
        data.append({'Total No of Student A Grade': a})
        data.append({'Total No of Student B Grade': b})
        data.append({'Total No of Student C Grade': c})
        data.append({'Total No of Student D Grade': d})
        data.append({'Total No of Student E Grade': e})
        data.append({'Total No of Student F Grade': f})
        data.append({'Distinction percentage': dic })
        data.append({'First class percentage': first })
        data.append({'Pass percentage': passing })

        return Response(data)

