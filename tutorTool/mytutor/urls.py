from django.urls import path
from . import views


app_name = "mytutor"

urlpatterns = [
    path('user_request/<int:pk>', views.handle_request, name='user_request'),
    path('response/<int:pk>', views.ResponseDetail.as_view(), name='response'),
    path('myqueries', views.return_queries, name='queries'),
]