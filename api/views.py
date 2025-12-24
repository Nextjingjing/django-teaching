from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question
from .serializers import QuestionSerializer

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
    
class HelloWorldId(APIView):
    def get(self, request, id):
        return Response(
            {
                "msg": "hello",
                "id": id
            }
        )
    
class HelloWorldVar(APIView):
    def get(self, request):
        var1 = request.query_params.get("var1", "DRF1")
        var2 = request.query_params.get("var2", "DRF2")
        return Response(
            {
                "msg": f"Hello {var1} and {var2}"
            }
        )
    
# Create Read Many Question

# Update Delete Read One Question
class QuestionDetail(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(instance = question)
        return Response(
            serializer.data
        )
