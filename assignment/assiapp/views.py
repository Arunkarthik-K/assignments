from django.shortcuts import render
from rest_framework import viewsets,generics,mixins
from .serializers import ExpenseSerializer, UserSerializer, CreateSerializer, UpdateSerializer, Update2Serializer
from .models import ExpenseModel, User, Group
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class pendinglistview(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = ExpenseSerializer 
        queryset = ExpenseModel.objects.filter(Status="PEND")
        lookup_field = "id"

        def get(self, request, id=None):
            if id:
                return self.retrieve(request, id)
            else:
                return self.list(request)

class approvedlistview(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = ExpenseSerializer 
        queryset = ExpenseModel.objects.filter(Status="APPR").order_by("Trans_Date")
        lookup_field = "id"

        def get(self, request, id=None):
            if id:
                return self.retrieve(request, id)
            else:
                return self.list(request)     

class createlistview(generics.GenericAPIView, mixins.CreateModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = CreateSerializer 
        queryset = ExpenseModel.objects.all()

        def post(self, request):
            return self.create(request) 

        def perform_create(self, serializer):
            serializer.save(Emp=self.request.user)         

class updatelistview(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = UpdateSerializer 
        queryset = ExpenseModel.objects.exclude(Status="APPR")  
        lookup_field = "id"     

        def get(self, request, id=None):
            if id:
                return self.retrieve(request, id)
            else:
                return self.list(request)

        def put(self, request, id):
            return self.update(request, id) 

        def perform_update(self, serializer):
            serializer.save(Emp=self.request.user)       

class update2listview(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = Update2Serializer 
        queryset = ExpenseModel.objects.filter(Status="PEND")
        lookup_field = "id"

        def get(self, request, id=None):
            if id:
                return self.retrieve(request, id)
            else:
                return self.list(request)

        def put(self, request, id):
            return self.update(request, id) 

        def perform_update(self, serializer):
            serializer.save(Emp=self.request.user)    

class deletelistview(generics.GenericAPIView, mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = ExpenseSerializer 
        queryset = ExpenseModel.objects.all()  
        lookup_field = "id"  

        def get(self, request, id=None):
            if id:
                return self.retrieve(request, id)
            else:
                return self.list(request)    

        def delete(self, request, id):
            return self.destroy(request, id)

class delete2listview(generics.GenericAPIView, mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]
        serializer_class = ExpenseSerializer 
        queryset = ExpenseModel.objects.exclude(Status="APPR")  
        lookup_field = "id"  

        def get(self, request, id=None):
            if id:
                return self.retrieve(request, id)
            else:
                return self.list(request)    

        def delete(self, request, id):
            return self.destroy(request, id)                             





        