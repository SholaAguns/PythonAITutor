from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "tutor"

urlpatterns = [
    path('', views.IndexPage.as_view(), name='tutor_index'),
]