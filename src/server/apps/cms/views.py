# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from apps.cms.models import HomePage
from .serializers import HomePageSerializer

@api_view(['GET'])
def get_home_content(request):

    try:
        home_page = HomePage.objects.filter(live=True)
    except Exception as error:
        return Response({
            'message': 'Page not found'
        }, status=status.HTTP_404_NOT_FOUND)

    serialized_home = HomePageSerializer(home_page, many=True)

    return Response(serialized_home.data, status=status.HTTP_200_OK)
