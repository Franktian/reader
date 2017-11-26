import logging
from apps.user.models import User

logger = logging.getLogger(__name__)

def is_user_exist(user_name):
    try:
        User.objects.get(user_name=user_name)
    except User.DoesNotExist:
        logger.info('User {} does not exist'.format(user_name))
        return False
    else:
        return True
