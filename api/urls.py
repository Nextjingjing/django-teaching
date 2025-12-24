from django.urls import path
from .views import HelloWorld, HelloWorldId, HelloWorldVar, QuestionDetail, QuestionListCreate

urlpatterns = [
    path("hello/", HelloWorld.as_view()),
    path("hello/<int:id>/", HelloWorldId.as_view()),
    path("hellovar/", HelloWorldVar.as_view()),

    path("questions/<int:id>/", QuestionDetail.as_view()),
    path("questions/", QuestionListCreate.as_view()),
]
