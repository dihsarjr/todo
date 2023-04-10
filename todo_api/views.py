from rest_framework.views import APIView
from rest_framework.response import Response
from todo_api.serializer import TodoModelSerializers
from todo_api.models import TodoModel
from rest_framework import status

class TodoList(APIView):
    def get(self,request):
        todo_list = TodoModel.objects.all()
        serializer = TodoModelSerializers(todo_list,many=True)
        return Response(serializer.data)
    

class AddTodo(APIView):
    def post(self,request):
        serializer = TodoModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



