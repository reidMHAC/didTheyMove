from django.contrib import admin
from django.urls import path, include
from didTheyMove import urls as didTheyMoveURLs
from rest_framework import routers
from didTheyMove import views

# router = routers.DefaultRouter()
# router.register(r'didTheyMove', views.DidTheyMoveView, 'didTheyMove')
# router.register(r'checkMoved', views.CheckMovedView, 'checkMoved')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(didTheyMoveURLs)),
]