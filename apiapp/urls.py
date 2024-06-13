from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .serializers import *
from apiapp.views import *
from django.conf.urls.static import static 
from django.conf import settings 


router=routers.DefaultRouter()
router.register(r'technologies',technologiesViewSet)
router.register(r'education',educationViewset)
router.register(r'experience',experienceViewSet)
router.register(r'project',projectViewSet)



urlpatterns = [
 path('', include(router.urls)),

]+static(settings.STATIC_URL, document_root=settings.STATIC_URL)
