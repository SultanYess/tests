# from django.test import TestCase
# from rest_framework import serializers
# from .models import  Pets, Owner, Type, Gender

# # сериализатор после Pets

class OwnerSerializers(serializers.ModelSerializer):
        name = serializers.CharField()
        surname = serializers.CharField()
        number = serializers.IntegerField()
        class Meta:
            fields = ['id', 'name']

# class GenderSerializers(serializers.Serializer):
#     gender = serializers.CharField(max_length = 2)
    
# class Type(serializers.Serializer):
#     pet_typee = serializers.CharField(max_length = 6)
    
    
    
    
    
# class PetsListView(generics.ListCreateAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializers


# class PetsList(APIView):
#     def get(self, request, fromat=None):
#         pets = Pets.objects.all()
#         serializers = PetsSerializers(pets, many = True)
#         return Response(serializers.data)
#     def post(self, request, format=None):
#         serializers = PetsSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# class PetsDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Pets.objects.get(pk=pk)
#         except Pets.DoesNotExist:
#             raise Http404
#     def get(self,pk,format=None):
#         pets = self.get_object(pk)
#         serializers = PetsSerializers(pets)
#         return Response(serializers.data)
#     def put(self, pk, request, format=None):
#         pets = self.get_object(pk)
#         serializers = PetsSerializers(pets, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         pets = self.get_object(pk)
#         pets.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    










# class PetsApiList(generics.ListCreateAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializers
#     permission_classes = (IsAuthenticatedOrReadOnly,)


# class PetsApiUpdate(generics.UpdateAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializers
    
# class PetsDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Pets.objects.all()
#     serializer_class = PetsSerializers
#     permission_classes = (IsAdminUser,)



# class GenderViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Gender.objects.all()
#     serializer_class = GenderSerializer

# class TypeViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer












# # sadasd

#     gender = models.ForeignKey('Gender', on_delete=models.CASCADE, default='', blank=True)
#     pet_type = models.ForeignKey('Type', on_delete=models.CASCADE, default='', blank=True)

# # asdsadasd

# class Gender(models.Model):
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     ]
    
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='')
    
#     def __str__(self):
#         return self.gender
    
# class Type(models.Model):
#     TYPE_CHOICES = [
#         ('Dog', 'Dog'),
#         ('Cat', 'Cat'),
#     ]
    
#     pet_typee = models.CharField(max_length=3, choices=TYPE_CHOICES, default='')
    
#     def __str__(self):
#         return self.pet_typee
    

# # sadasdasd
# class TypeSerializer(serializers.Serializer):
#     class Meta:
#         model = Type
#         fields = '__all__'

# class GenderSerializer(serializers.Serializer):
#     class Meta:
#         model = Gender
#         fields = '__all__'

# ## sadasdsasdasd

# class GenderViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Gender.objects.all()
#     serializer_class = GenderSerializer

# class TypeViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer
    