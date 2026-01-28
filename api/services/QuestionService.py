from django.utils import timezone
from ..models import Question

class QuestionService():
    @staticmethod
    def create_question(*, question_text: str) -> Question:
        """
        Creates a new Question object.
        """
        question = Question.objects.create(
            question_text=question_text,
            pub_date=timezone.now()
        )
        return question

    @staticmethod
    def list_questions():
        return Question.objects.all()