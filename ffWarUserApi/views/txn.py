from rest_framework import  permissions,decorators
from rest_framework.views import APIView
from rest_framework.response import Response
from ffWarUserApi import checksum
@decorators.permission_classes([permissions.AllowAny])
class ChecksumView(APIView):
    def post(self,request):
        checksum1=checksum.GenerateChecksum(request.data["mid"],request.data["orderid"])
       
        
        return Response(checksum1)
@decorators.permission_classes([permissions.AllowAny])
class callback(APIView):
    def post(self,request):
        return Response(request.data)
