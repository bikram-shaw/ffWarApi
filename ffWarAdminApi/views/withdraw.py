from rest_framework import viewsets, permissions,decorators,status
from ffWarUserApi.models.user import WithdrawModel
from rest_framework.response import Response
from ffWarAdminApi.serializers.gameSerializers import WithdrawReqSerializer

@decorators.permission_classes([permissions.AllowAny])
class WithReqViewset(viewsets.ModelViewSet):
    queryset = WithdrawModel.objects.all()
    serializer_class = WithdrawReqSerializer
    def list(self, request, *args, **kwargs):
        wth_req=WithdrawModel.objects.filter(wth_status=False)
        print(wth_req)
        serializer=self.get_serializer(wth_req,many=True)
        return Response(serializer.data)



    def update(self, request, *args, **kwargs):
        wth_data=WithdrawModel.objects.get(id=self.kwargs["pk"])
        wth_data.wth_status=True
        wth_data.save()
        print(wth_data.user)


        return Response(status=status.HTTP_200_OK)


