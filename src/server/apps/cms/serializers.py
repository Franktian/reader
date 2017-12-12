from rest_framework import serializers
from rest_framework.fields import Field

from .models import HomePage

class StreamFieldSerializer(Field):
    """
    provides a method that loops over wagtail streamfield
    blocks and serializes them so they can be easily
    consumed by the front end.
    """

    def to_representation(self, value):
        return value.stream_block.get_prep_value(value)


class HomePageSerializer(serializers.ModelSerializer):
    content = StreamFieldSerializer()

    class Meta:
        model = HomePage
        fields = ['content']
