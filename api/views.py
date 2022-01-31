from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from database import models
from . import serializers

class record_api_view_get_all(APIView):
    serializer_class = serializers.record_serializer

    def get(self, request):
        serializer = self.serializer_class

        try:
            queryset = models.record.objects.all().order_by('-_created')
            serializer = serializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return HttpResponse(status=500, content=b'Internal Server Error')

class record_api_view_create_new(APIView):
    serializer_class = serializers.record_serializer

    def post(self, request):
        serializer = self.serializer_class

        try:
            serializer = serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except:
            return HttpResponse(status=500, content=b'Internal Server Error')
