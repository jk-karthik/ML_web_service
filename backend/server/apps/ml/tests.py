from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry
from .classifier.rf import RandomForestClassifier

class MLtests(TestCase):
	def test_rf_algorithm(self):
		input_data={
			"Age" :25,
			"Experience":1,
			"Income":49,
			"Family":4,
			"CCAvg":1.6,
			"Mortgage":0,
			"Securities Account":1,
			"CD Account":0,
			"Online":0,
			"CreditCard":0,
			"Education":1,
			"ZIP Code":92212

		}
		alg=RandomForestClassifier()
		response=alg.Predict(input_data)
		self.assertTrue(response['label'] in [0,1])

	def test_registry(self):
		registry=MLRegistry()
		self.assertEqual(len(registry.endpoints),0)
		endpoint_name="rf-classifier-personal loan"
		algorithm_object=RandomForestClassifier()
		algorithm_name="randomforrest"
		algorithm_status="production"
		algorithm_code = inspect.getsource(RandomForestClassifier)
		algorithm_owner = "starboy"
		algorithm_description = "Random Forest with simple pre- and post-processing"
		registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,algorithm_status, algorithm_owner,algorithm_description, algorithm_code)
		self.assertEqual(len(registry.endpoints),1)

# input_data={
# 			"Age" :25,
# 			"Experience":1,
# 			"Income":49,
# 			"Family":4,
# 			"CCAvg":1.6,
# 			"Mortgage":0,
# 			"Securities Account":1,
# 			"CD Amount":0,
# 			"Online":0,
# 			"Credit Card":0,
# 			"Zips":911,
# 			"ed1":1,
# 			"ed2":0,
# 			"ed3":0

# 		}
# alg=RandomForestClassifier()
# response=alg.predict(input_data)
# print(response)