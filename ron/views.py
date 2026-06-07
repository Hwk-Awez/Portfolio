from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .chain import ask_ron

class RonChatView(APIView):
    def post(self, request):
        question = request.data.get("question", "").strip()
        if not question:
            return Response(
                {"error": "No question provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        answer = ask_ron(question)
        return Response({"answer": answer}, status=status.HTTP_200_OK)
