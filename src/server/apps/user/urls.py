from django.conf.urls import url
from apps.user.views import UserView

urlpatterns = [
    url(r'register', UserView.as_view({'post': 'register'})),
    url(r'login', UserView.as_view({'post': 'login'})),
]
