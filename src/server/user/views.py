import logging
from rest_framework import status, viewsets
from rest_framework.response import Response

from user.models import User

logger = logging.getLogger(__name__)
# Create your views here.
class UserView(viewsets.ViewSet):
    """
    Handle login and register
    """
    def register(self, request):
        data = request.data
        resp_data = {}

        try:
            username = data['username']
            password = data['password']
        except KeyError as error:
            logger.error(
                "Missing required input for register : {}".format(str(error))
            )
            resp_data = {
                'error': 'Invalid Request Parameters.'
            }
            resp_status = status.HTTP_400_BAD_REQUEST
        else:
            logger.info('UserView - Attempt to register user'.format(username))
            resp_status = status.HTTP_200_OK

        return Response(resp_data, resp_status)

    def login(self, request):
        return Response({'Frank': 'login'}, status.HTTP_200_OK)
