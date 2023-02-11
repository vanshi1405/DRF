from django.shortcuts import render
from api.serializers import StudentSerializer
from api.models import Student
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions,DjangoModelPermissions

# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset=Student.objects.all()
    serializer=StudentSerializer(queryset,many=True)

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [DjangoModelPermissions]

    @action(methods=['get'], detail=False)
    def byhello (self, request,pk=None):
        # data=self.get_object()
        # serializer=self.get_serializer(data)
        return Response({"From Hello": "Got it"})
        # return Response(serializer.data)

    # def list(self,request):
    #     stu=Student.objects.all()
    #     serializer=StudentSerializer(stu,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    #
    #
    # def retrive(self,request,pk=None):
    #     id=pk
    #     if id is not None:
    #         stu=Student.objects.get(id=id)
    #         serializer=StudentSerializer(stu)
    #         return Response(serializer.data)
    #
    # def create(self,request):
    #     # stu=Student.object.all()
    #     serializer=StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    # def update(self, request,pk=None):
    #     id=pk
    #     if id is not None:
    #         stu=Student.object.get(id=id)
    #         serializer = StudentSerializer(stu)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, "data updated")
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    # def partial_update(self, request,pk=None):
    #     id=pk
    #     if id is not None:
    #         stu=Student.objects.get(id=id)
    #         serializer = StudentSerializer(stu)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, "data updated")
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # def destroy(self, request,pk=None):
    #     id=pk
    #     if id is not None:
    #         stu=Student.objects.get(id=id)
    #         stu.delete()
    #         return Response("data deleted")
    #         # return Response(status=status.HTTP_400_BAD_REQUEST)
    #
