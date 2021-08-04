from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from django.http import HttpResponse

from services.services import *
from smart_screen.settings import BASE_URL
from smart_screen.utils.send_request import send_request


class ServicesRUD(RetrieveUpdateDestroyAPIView):
    def delete(self, request, id):
        data, status_code = delete_service(service_id=id)
        return Response(data, status=status_code)
        
    def put(self, request, id):
        data, status_code = update_service(service_id=id, data=request.data)
        return Response(data, status=status_code)
    
    def get(self, request, id):
        data, status_code = get_service(service_id=id)
        return Response(data, status=status_code)


class Services(APIView):      
    def get(self, request):
        data, status_code = get_services(request.get_full_path())
        return Response(data, status=status_code)

    def post(self, request):
        data, status_code = create_service(request.data)
        return Response(data, status=status_code)


class Image(APIView):    
    def get(self, request, id):
        data, status_code = get_image(image_id=id)
        return HttpResponse(data, content_type="image/*", status=status_code)

class ImageCreate(APIView):
    def post(self, request):
        data, status_code = create_image(request.data.get("image"))
        return Response(data, status=status_code)