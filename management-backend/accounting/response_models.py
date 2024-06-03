from rest_framework.response import Response
from rest_framework import status


def CreatedResponse(detail=""):
    return Response({"detail": detail}, status=status.HTTP_201_CREATED)


def BadRequestResponse(detail):
    return Response({"detail": detail}, status=status.HTTP_400_BAD_REQUEST)
