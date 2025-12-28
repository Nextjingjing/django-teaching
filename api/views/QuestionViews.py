from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Question
from ..serializers import QuestionSerializer, QuestionCreateSerializer
from django.utils import timezone

# Create Read Many Question
class QuestionListCreate(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(instance = question, many=True)
        res = {
            "msg": "Success",
            "data": serializer.data
        }
        return Response(res)
    
    def post(self, request):
        serializer = QuestionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question.objects.create(
                question_text=serializer.validated_data["question_text"],
                pub_date=timezone.now()
            )

        response_serializer = QuestionSerializer(instance = question)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
            )
            


# Update Delete Read One Question
class QuestionDetail(APIView):
    def get(self, request, id):
        question = get_object_or_404(Question, pk=id)
        serializer = QuestionSerializer(instance = question)
        return Response(
            serializer.data
        )