from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HelloWorld(APIView):
    def get(self, request):
        if not ("name" in request.data and "age" in request.data):
            return Response(
                {
                    "msg": "Bad Request!!!"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        name = request.data["name"]
        age = request.data["age"]
        return Response(
            {
                "msg": "Hello",
                "name": name,
                "age": age
            }
        )