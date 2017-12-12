from django.conf.urls import url
from .views import get_home_content

urlpatterns = [
    url(
        regex=r'get-home-content',
        view=get_home_content
    )
]
