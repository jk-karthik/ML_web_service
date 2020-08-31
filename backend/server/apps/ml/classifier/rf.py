import joblib
import numpy as np 
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import os
class RandomForestClassifier:

	def __init__(self,filepath):
		path=os.path.dirname(os.path.realpath(__file__))
		self.model=joblib.load(path+"\\"+filepath)
		self.encoder=joblib.load(path+"\\"+'encoder.joblib')
		with open(path+"\\"+"order_cols.txt",'r') as f:
			self.cc=f.read()
		self.cc=self.cc.split(",")
		with open(path+"\\"+"preorder_cols.txt",'r') as f:
			self.qq=f.read()
		self.qq=self.qq.split(",")

		self.info={}
	def Predict(self,data):
		data=pd.DataFrame(data,index=[0])
		data['Personal Loan']=0
		x=self.encoder.transform(data[self.qq])
		
		hot=pd.DataFrame(x)
		# print(self.encoder.get_feature_names())
		hot.columns=self.encoder.get_feature_names()
		hot.head()
		data.reset_index(inplace=True,drop=True)
		hot.reset_index(inplace=True,drop=True)
		data=pd.concat([data.loc[:,:],hot],axis=1)
		data["Prev_Association"]=data[["Securities Account","CD Account","CreditCard"]].apply(lambda x: 1 if any(x[x==1]) else 0,axis=1)
		data.drop('Education',axis=1,inplace=True)

		data.drop('ZIP Code',axis=1,inplace=True)
		data.drop(["Experience","Online","CreditCard","Securities Account"],axis=1,inplace=True)
		# print(data.columns)
		self.info['label']=self.model.predict(data[self.cc])
		# print(data[self.cc],self.model.classes_,x)
		self.info['proba']={self.model.predict_proba(data[self.cc])[0][i]: i for i in [0,1]}
		return self.info




