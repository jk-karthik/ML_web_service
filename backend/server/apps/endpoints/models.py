from django.db import models


# Create your models here.
class Endpoint(models.Model):
	'''Mk API endpoint'''
	name=models.CharField(max_length=128)
	owner=models.CharField(max_length=126)
	created_at=models.DateTimeField(auto_now_add=True,blank=True)

class MLAlgorithm(models.Model):
	''' MLalgothims enpoint'''
	name=models.CharField(max_length=128)
	description=models.CharField(max_length=1000)
	owner=models.CharField(max_length=128)
	code=models.CharField(max_length=50000)
	created_at=models.DateTimeField(auto_now_add=True,blank=True)
	parent_endpoint=models.ForeignKey(Endpoint,on_delete=models.CASCADE)

class MLAlgo_status(models.Model):
	'''Status of above algorithm'''

	status=models.CharField(max_length=128)
	active=models.BooleanField()
	created_by=models.CharField(max_length=128)
	created_at=models.DateTimeField(auto_now_add=True,blank=True)
	parent_mlalgorithm=models.ForeignKey(MLAlgorithm,on_delete=models.CASCADE)

class MLRequest(models.Model):
	'''requests to ML algorithm'''

	input_data=models.CharField(max_length=100000)
	full_response=models.CharField(max_length=100000)
	response = models.CharField(max_length=100000)
	feedback = models.CharField(max_length=100000, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)

