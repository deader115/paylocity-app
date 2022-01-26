from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('preview-cost', views.previewCost),
    # re_path(r'^lookup-cost/(?P<id>[0-9]+)$', views.lookupCost),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
