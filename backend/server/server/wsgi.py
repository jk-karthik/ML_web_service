"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

import inspect
from apps.ml.registry import MLRegistry
from apps.ml.classifier.rf import RandomForestClassifier
registry=MLRegistry()
try:

	

	endpoint_name="rf-PL-hardpunish"
	algorithm_object=RandomForestClassifier("Web_rf_3.joblib")
	algorithm_name="randomforrest-3"
	algorithm_status="production"
	algorithm_code = inspect.getsource(RandomForestClassifier)
	algorithm_owner = "starboy"
	algorithm_description = "Random Forest with class weight ration 10"
	# registry.isbefore(endpoint_name,algorithm_name,algorithm_status,algorithm_owner,algorithm_description)
	registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,algorithm_status, algorithm_owner,algorithm_description, algorithm_code)
	print("Success 3")
except Exception as e:
	print("Exception while loading the algorithms to the registry,", str(e))
try:



	endpoint_name="rf-PL-freqpunish"
	algorithm_object=RandomForestClassifier("Web_rf_2.joblib")
	algorithm_name="randomforrest-2"
	algorithm_status="production"
	algorithm_code = inspect.getsource(RandomForestClassifier)
	algorithm_owner = "starboy"
	algorithm_description = "Random Forest with class weight ration 10"
	# registry.isbefore(endpoint_name,algorithm_name,algorithm_status,algorithm_owner,algorithm_description)
	registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,algorithm_status, algorithm_owner,algorithm_description, algorithm_code)
	print("Success  2")
except Exception as e:
	print("Exception while loading the algorithms to the registry,", str(e))



try:



	endpoint_name="rf-PL-rootfreqpunish"
	algorithm_object=RandomForestClassifier("Web_rf_1.joblib")
	algorithm_name="randomforrest-"
	algorithm_status="production"
	algorithm_code = inspect.getsource(RandomForestClassifier)
	algorithm_owner = "starboy"
	algorithm_description = "Random Forest with class weight ration 10"
	# registry.isbefore(endpoint_name,algorithm_name,algorithm_status,algorithm_owner,algorithm_description)
	registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,algorithm_status, algorithm_owner,algorithm_description, algorithm_code)
	print("Success 1")
except Exception as e:
	print("Exception while loading the algorithms to the registry,", str(e))