from django.urls import path
from .views import (HelloWorld, 
                    HelloWorldId, 
                    HelloWorldVar,
                    HelloError,
                    QuestionDetail, 
                    QuestionListCreate,
                    ChoiceListCreate,
                    ChoiceVote,
                    ChoiceDetail
                    )

urlpatterns = [
    path("hello/", HelloWorld.as_view()),
    path("hello/<int:id>/", HelloWorldId.as_view()),
    path("hellovar/", HelloWorldVar.as_view()),
    path("helloerror/", HelloError.as_view()),

    path("questions/<int:id>/", QuestionDetail.as_view()),
    path("questions/", QuestionListCreate.as_view()),

    path("choices/questions/<int:question_id>/", ChoiceListCreate.as_view()),
    path("choices/<int:choice_id>/vote/", ChoiceVote.as_view()),
    path("choices/<int:choice_id>/", ChoiceDetail.as_view())
]
