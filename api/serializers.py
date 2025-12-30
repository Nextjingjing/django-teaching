from rest_framework import serializers
from .models import Question

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