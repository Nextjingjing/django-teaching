from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField()