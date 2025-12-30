from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id', 
            'question_text', 
            'pub_date'
            ]

class QuestionCreateSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id', 
            'choice_text', 
            'votes',
            'question',
            ]

class ChoiceCreateSerializer(serializers.Serializer):
    choice_text = serializers.CharField(max_length=200)