from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class HelloWorld(APIView):
    def get(self, request):
        if not ("name" in request.data and "age" in request.data):
            return Response(
                {
                    "msg": "Bad Request!!!"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        name = request.data["name"]
        age = request.data["age"]
        return Response(
            {
                "msg": "Hello",
                "name": name,
                "age": age
            }
        )
    
class HelloWorldId(APIView):
    def get(self, request, id):
        return Response(
            {
                "msg": "hello",
                "id": id
            }
        )
    
class HelloWorldVar(APIView):
    def get(self, request):
        var1 = request.query_params.get("var1", "DRF1")
        var2 = request.query_params.get("var2", "DRF2")
        return Response(
            {
                "msg": f"Hello {var1} and {var2}"
            }
        )