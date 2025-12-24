from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()

class QuestionCreateSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=200)