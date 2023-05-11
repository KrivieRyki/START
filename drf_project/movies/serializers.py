from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from movies.models import Movie


class MovieSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='movie-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Movie
        fields = ('url', 'title', 'genre', 'year')
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
