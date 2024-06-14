from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "mytutor"

urlpatterns = [
    #path('', views.IndexPage.as_view(), name='tutor_index'),
    path('user_request/<int:pk>', views.handle_request, name='user_request'),
    path('response/<int:pk>', views.ResponseDetail.as_view(), name='response'),
    path('<username>/queries', views.QueryList.as_view(), name='queries'),
]