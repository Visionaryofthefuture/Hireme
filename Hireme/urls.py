from django.http import HttpResponse
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login/', views.login, name = "login")
]
if(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
