from django.urls import path
from .views import *

urlpatterns = [
    # path('status/', StatusAPIView.as_view()),
    # path('status/list/', StatusListAPIView.as_view()),
    # path('status/create/', StatusCreateAPIView.as_view()),
    path('status/', StatusListCreateView.as_view(),),
    

    # path('status/update/<id>/', StatusUpdateAPIView.as_view()),
    # path('status/delete/<id>/', StatusDeleteAPIView.as_view()),
    path('status/detail/<id>/', StatusDetailAPIView.as_view()),
]