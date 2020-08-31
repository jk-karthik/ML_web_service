from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from apps.endpoints.views import EndpointViewSet,MLAlgorithmViewSet,MLAlgo_statusViewSet,MLRequestViewSet,PredictView

router=DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgo_statusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
	url(r"^api/v1/", include(router.urls)),
	url(
		r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
	),
	]