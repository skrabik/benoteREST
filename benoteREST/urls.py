from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/content/', ContentAPIList.as_view()),
    path('api/v1/content/<int:pk>/', ContentAPIUpdate.as_view()),
    path('api/v1/contentdelete/<int:pk>/', ContentAPIDestoroy.as_view()),

]
