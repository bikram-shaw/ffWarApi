from rest_framework import  permissions,decorators
from rest_framework.views import APIView
from rest_framework.response import Response
from ffWarUserApi import checksum
import random,json
import requests
@decorators.permission_classes([permissions.AllowAny])
class ChecksumView(APIView):
    def post(self,request):
        oid=str(random.random())
        

       
        checksum1=checksum.GenerateChecksum(oid)
       
        res={"oid":oid,"checksum":checksum1}
        return Response(res)
@decorators.permission_classes([permissions.AllowAny])
class callback(APIView):
    def post(self,request):
        paytmParams = dict()
        paytmParams["head"] = {
            "signature": request.data["checksum"]
        }

        post_data = json.dumps(paytmParams)

        # for Staging
        #url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"

        # for Production
        url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=eVExLv25221231925149&orderId="+request.data["oid"]
        response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
        return Response(response)
