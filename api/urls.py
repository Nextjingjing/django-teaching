from django.urls import path
from .views import HelloWorld, HelloWorldId, HelloWorldVar

urlpatterns = [
    path("hello/", HelloWorld.as_view()),
    path("hello/<int:id>/", HelloWorldId.as_view()),
    path("hellovar/", HelloWorldVar.as_view()),
]
