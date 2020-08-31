from apps.endpoints.models import Endpoint,MLAlgorithm,MLAlgo_status

class MLRegistry:
	def __init__(self):
		self.endpoints = {}

	def add_algorithm(self, endpoint_name, algorithm_object, algorithm_name,
					algorithm_status, owner,
					algorithm_description, algorithm_code):
	    # get endpoint
		endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)

	    # get algorithm
		database_object, algorithm_created = MLAlgorithm.objects.get_or_create(name=algorithm_name,description=algorithm_description,code=algorithm_code,owner=owner,parent_endpoint=endpoint)
		# print([algorithm_created for i in range(50)],database_object.id)
		if algorithm_created:
			status = MLAlgo_status(status = algorithm_status,created_by = owner,parent_mlalgorithm = database_object,active = True)
			status.save()

	    # add to registry
		self.endpoints[database_object.id] = algorithm_object
		# print(self.endpoints[database_object.id])

