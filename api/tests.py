from django.test import TestCase
from django.utils import timezone
from django.db import close_old_connections
from django.test import TransactionTestCase
import threading

from .models import Question, Choice
from .services import QuestionService
from .services.ChoiceService import ChoiceService


# Create your tests here.
class QuestionServiceCreateTest(TestCase):
    def test_create_question(self):
        """
        test creating a question
        """
        question_text = "Taylor Swift or Sabrina Carpenter?"

        question = QuestionService.create_question(
            question_text=question_text
        )

        self.assertIsNotNone(question.id)
        self.assertEqual(question.question_text, question_text)
        self.assertEqual(Question.objects.count(), 1)
        self.assertIsNotNone(question.pub_date)
        self.assertLessEqual(question.pub_date, timezone.now())

    def test_list_questions(self):
        """
        test listing all questions
        """
        q1 = Question.objects.create(
            question_text="Question 1",
            pub_date=timezone.now()
        )
        q2 = Question.objects.create(
            question_text="Question 2",
            pub_date=timezone.now()
        )

        questions = QuestionService.list_questions()

        self.assertEqual(questions.count(), 2)
        self.assertIn(q1, questions)
        self.assertIn(q2, questions)

class ChoiceServiceConcurrentVoteTest(TransactionTestCase):

    def setUp(self):
        self.question = Question.objects.create(
            question_text="Best singer?",
            pub_date=timezone.now()
        )

        self.choice = Choice.objects.create(
            question=self.question,
            choice_text="Taylor Swift",
            votes=0
        )

    def _vote(self):
        close_old_connections()
        ChoiceService.vote_choice(choice_id=self.choice.id)
        close_old_connections()

    def test_concurrent_vote(self):
        threads = []
        vote_times = 5

        for _ in range(vote_times):
            t = threading.Thread(target=self._vote)
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 5)