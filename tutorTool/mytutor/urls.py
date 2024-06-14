from django.urls import path
from . import views


app_name = "mytutor"

urlpatterns = [
    path('user_request/<int:pk>', views.handle_request, name='user_request'),
    path('response/<int:pk>', views.ResponseDetail.as_view(), name='response'),
    path('myrequests', views.ResponseList.as_view(), name='requests'),
    path("delete/<int:pk>/", views.delete_response, name="delete"),
]