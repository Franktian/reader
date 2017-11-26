import logging
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.user.models import User
from apps.user.utils import is_user_exist

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
            logger.info('UserView - Attempt to register user {}'.format(username))
            resp_status = status.HTTP_200_OK
            if not is_user_exist(username):
                User.objects.create(user_name=username, password=password)
                resp_data = {
                    'message': "User {} created".format(username),
                    'success': True
                }
            else:
                resp_data = {
                    'message': "User {} already exists".format(username),
                    'success': False
                }

        return Response(resp_data, resp_status)

    def login(self, request):
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
            logger.info('UserView - Attempt to login user {}'.format(username))
            resp_status = status.HTTP_200_OK
            try:
                user = User.objects.get(user_name=username)
            except User.DoesNotExist:
                logger.info('User {} does not exist'.format(username))
                resp_data = {
                    'message': "User {} does not exist".format(username),
                    'success': False
                }
            else:
                if user.password != password:
                    logger.info('UserView - password does not match')
                    resp_data = {
                        'message': 'Password does not match',
                        'success': False,
                    }
                else:
                    logger.info('User {} logged in'.format(username))
                    resp_data = {
                        'message': 'User {} logged in'.format(username),
                        'success': True,
                    }

        return Response(resp_data, status.HTTP_200_OK)
