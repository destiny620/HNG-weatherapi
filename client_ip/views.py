from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# import requests

# Create your views here.

class HelloView(APIView):
    def get(self, request):
        visitor_name = request.GET.get("visitor_name", "Mark")
        client_ip = request.META.get("REMOTE_ADDR", "127.0.0.1")

        location = "New York"
        temperature = 11

        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degress celsius in {location}"

        data = {
            'client_ip': client_ip,
            'location': location,
            'greeting': greeting
        }

        return Response(data, status=status.HTTP_200_OK)