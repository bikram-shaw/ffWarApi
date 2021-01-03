from django.urls import path,include
from ffWarAdminApi import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('game',views.GameViewSet)
router.register('room',views.RoomDetailsViewSet)
router.register('user-withdraw-request',views.WithReqViewset)

urlpatterns = [

    path('',include(router.urls)),
    path('fetch-join-player',views.FetchJoinPlayerView.as_view()),
    path('result',views.ResultView.as_view())
]