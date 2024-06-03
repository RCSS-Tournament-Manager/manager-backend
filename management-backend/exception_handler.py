from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def main_handler(exc, context):
    try:
        response = exception_handler(exc, context)
    

        if response is not None:
            # Get the detail from the exception
            detail = str(exc)

            # Handle the detail as needed (e.g. modify, format, etc.)
            # ...

            # Create a new response with the modified detail
            response.data = {"detail": detail}
            response.status_code = status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response