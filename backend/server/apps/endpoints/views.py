from django.shortcuts import render
from rest_framework import viewsets,views,status,mixins
from rest_framework.response import Response 
from apps.ml.registry import MLRegistry
from server.wsgi import registry

import json
from numpy.random import rand 
from apps.endpoints.models import Endpoint,MLAlgorithm,MLAlgo_status,MLRequest
from apps.endpoints.serializers import EndpointSerializer,MLAlgorithmSerializer,MLAlgo_statusSerializer,MLRequestSerializer
# Create your views here.

class EndpointViewSet(
	mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = EndpointSerializer
	queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(
	mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	serializer_class = MLAlgorithmSerializer
	queryset = MLAlgorithm.objects.all()


def deactivate_other_statuses(instance):
	old_statuses = MLAlgo_status.objects.filter(parent_mlalgorithm = instance.parent_mlalgorithm,created_at__lt=instance.created_at,active=True)
	for i in range(len(old_statuses)):
		old_statuses[i].active = False
	MLAlgo_status.objects.bulk_update(old_statuses, ["active"])

class MLAlgo_statusViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,mixins.CreateModelMixin):
	serializer_class = MLAlgo_statusSerializer
	queryset = MLAlgo_status.objects.all()
	def perform_create(self, serializer):
		try:
			with transaction.atomic():
				instance = serializer.save(active=True)
			    # set active=False for other statuses
				deactivate_other_statuses(instance)



		except Exception as e:
			raise APIException(str(e))

class MLRequestViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,mixins.UpdateModelMixin):
	serializer_class = MLRequestSerializer
	queryset = MLRequest.objects.all()

class PredictView(views.APIView):

	def post(self,request,endpoint_name,format=None):
		algorithm_status = self.request.query_params.get("status", "production")
		# print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
		algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, mlalgo_status__status = algorithm_status, mlalgo_status__active=True)
		# print(len(MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, mlalgo_status__status = algorithm_status, mlalgo_status__active=True)))
		# print(len(algs))
		if len(algs) == 0:
			return Response(
				{"status": "Error", "message": "ML algorithm is not available"},
				status=status.HTTP_400_BAD_REQUEST,
			)
		if len(algs) != 1 and algorithm_status != "ab_testing":
			return Response(
				{"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
				status=status.HTTP_400_BAD_REQUEST,
			)
		algorithm_object = registry.endpoints[algs[0].id]
		info = algorithm_object.Predict(request.data)

		info["action req"] = "Dont Advertise" if info['label']==0 else "Advertise"
		ml_request = MLRequest(
			input_data=json.dumps(request.data),
			full_response=info,
			response=info['label'],
			feedback="",
			parent_mlalgorithm=algs[0],
		)
		ml_request.save()

		return Response(info)

