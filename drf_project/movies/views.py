
from rest_framework import viewsets


from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             'title': openapi.Schema(type=openapi.TYPE_STRING),
    #             'genre': openapi.Schema(type=openapi.TYPE_STRING),
    #             'year': openapi.Schema(type=openapi.TYPE_STRING),
    #         },
    #     )
    # )
    # def post(self, request, format=None):
    #     serializer = MovieSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # @swagger_auto_schema(
    #     request_body=openapi.Schema(
    #         type=openapi.TYPE_OBJECT,
    #         properties={
    #             "title": openapi.Schema(type=openapi.TYPE_STRING),
    #             "genre": openapi.Schema(type=openapi.TYPE_STRING),
    #             "year": openapi.Schema(type=openapi.TYPE_STRING),
    #         },
    #     )
    # )
    # def put(self, request, pk, format=None):
    #     movie = self.get_object(pk)
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
