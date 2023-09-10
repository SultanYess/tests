from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Pets
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import *
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from .forms import PetsForm

class PetsApiList(generics.ListCreateAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializers
    # authentication_classes = (TokenAuthentication, )


class PetsApiUpdate(generics.UpdateAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializers
    # authentication_classes = (TokenAuthentication, )
    
class PetsDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializers
    # authentication_classes = (TokenAuthentication, )
    
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)


def index(request):
    news = Pets.objects.all()
    return render(request, 'pets/index.html', {'news': news})

def create(request):
    if request.method == 'POST':
        form = PetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнение данных не верна'
    form = PetsForm()
    data = {
        'form': form
    }

    return render(request, 'pets/create.html', data)


        







        