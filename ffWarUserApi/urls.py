"""ffWarApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from ffWarUserApi import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
#router.register('signup',views.userSignUp)

#router.register('withdraw',views.WithdrawViewset)
urlpatterns = [

    path('',include(router.urls)),
    path('signup',views.userSignUp),
    path('login',views.userSignIn),
    path('active-game',views.ActiveGameView.as_view()),
    path('ongoing-game', views.OngoingGameView.as_view()),
    path('completed-game', views.CompletedGameView.as_view()),
    path('result', views.FetchResultView.as_view()),
    path('fetchJoinPlayer',views.FetchJoinPlayerView.as_view()),
    path('joinGame', views.JoinGameView.as_view()),
    path('GetUserTransaction', views.GetUserTransaction.as_view()),
    path('PostUserTransaction', views.PostUserTransaction.as_view()),
    path('withdraw', views.WithdrawViewset.as_view()),
    path('wallet',views.WalletViewset.as_view()),
    path('checksum', views.ChecksumView.as_view()),
     path('callback', views.callback.as_view())




]
'''
urlpatterns = [
    path('userlist',views.user_list.as_view()),
    path('userdetails/<int:pk>',views.user_details.as_view())
]
'''