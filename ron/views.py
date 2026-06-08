from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .chain import ask_ron

@method_decorator(csrf_exempt, name='dispatch')
class RonChatView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        question = request.data.get("question", "").strip()
        if not question:
            return Response(
                {"error": "No question provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        answer = ask_ron(question)
        return Response({"answer": answer}, status=status.HTTP_200_OK)