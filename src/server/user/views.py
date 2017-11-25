from rest_framework import status, viewsets
from rest_framework.response import Response

from user.models import User

# Create your views here.
class UserView(viewsets.ViewSet):
    """
    Handle login and register
    """
    def register(self, request):
        return Response({'Frank': 'register'}, status.HTTP_200_OK)

    def login(self, request):
        return Response({'Frank': 'login'}, status.HTTP_200_OK)
