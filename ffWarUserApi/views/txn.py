from rest_framework import  permissions,decorators
from rest_framework.views import APIView
from rest_framework.response import Response
from ffWarUserApi import checksum
import random
@decorators.permission_classes([permissions.AllowAny])
class ChecksumView(APIView):
    def post(self,request):
        oid=str(random.random())
        checksum1=checksum.GenerateChecksum("eVExLv25221231925149", oid)
       
        res={"oid":oid,"checksum":checksum1}
        return Response(res)
@decorators.permission_classes([permissions.AllowAny])
class callback(APIView):
    def post(self,request):
        return Response(request.data)
