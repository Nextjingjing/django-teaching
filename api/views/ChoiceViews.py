from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from ..models import Question, Choice
from ..serializers import ChoiceCreateSerializer, ChoiceSerializer
from django.utils import timezone
from django.db import transaction

from ..services.ChoiceService import ChoiceService


class ChoiceListCreate(APIView):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        choices = Choice.objects.filter(question=question)
        response_serializer = ChoiceSerializer(instance = choices, many = True)
        return Response(response_serializer.data)

    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        serializer = ChoiceCreateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        choice_text = serializer.validated_data["choice_text"]
        choice = Choice.objects.create(
                choice_text = choice_text,
                question = question,
            )
        response_serializer = ChoiceSerializer(instance = choice)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class ChoiceVote(APIView):
    def post(self, request, choice_id):
        # Business Logic
        ChoiceService.vote_choice(choice_id=choice_id)

        return Response(
        {
                "msg": "vote success!"
            },
            status=status.HTTP_200_OK
        )
        
class ChoiceDetail(APIView):
    def get(self, request, choice_id):
        choice = get_object_or_404(Choice, pk=choice_id)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    def put(self, request, choice_id):
        choice = get_object_or_404(Choice, pk=choice_id)
        serializer = ChoiceCreateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        choice.choice_text = serializer.validated_data["choice_text"]
        choice.save()

        response_serializer = ChoiceSerializer(choice)
        return Response(response_serializer.data)

    def delete(self, request, choice_id):
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.delete()
        return Response(
            {
                "msg": "Deleted!"
            },
            status=status.HTTP_204_NO_CONTENT
            )