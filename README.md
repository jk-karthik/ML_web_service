# ML_web_service

 3 Trained Random Forest Algorithms are put on the Django Server for Local web api
 Run the Django server to access the ML api's for prediction of Personal Loan acceptance <br /> <br />
 
 Run the server from the directory backend/server after modifying the appropriate address for each web model <br /> 
 
 # Input to API
 Input should be passed as a dictionary without the id <br /> <br />
 
 eg :
{
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
			"ZIP Code":92211}  <br /> <br />
 # WorkOut
 All the steps are detailed in Case_study.ipynb file  
 
 # Model 3: (default model)
 This is preffered due to least loss of oppurtunity (lowest False Positive)    <br />
 Accuracy on test and train set is 77.2% and test set is 77.9%  (see confusion matrix in .ipynb file) <br /> <br />
 # To run model 3- <br />
 http://127.0.0.1:8000/api/v1/rf-PL-hardpunish/predict -use this url  <br /> 
 
 Change the address ,for self.model to the installed location of "Web_rf_3.joblib" in rf file present in backend/server/apps/ml/classifier/rf.py    <br />
 Also change the endpoint_name to "rf-PL-hardpunish" and algorithm name to "randomforrest-3" in file backend/server/server/wsgi.py 
       
 
 # Model 2:
 Accuracy on test and train set is 97%  <br /> <br />
 

 # To run model 2- <br />
 http://127.0.0.1:8000/api/v1/rf-PL-freqpunish/predict -use this url <br /> 
 
 Change the address ,for self.model to the installed location of "Web_rf_2.joblib" in rf file present in backend/server/apps/ml/classifier/rf.py <br />
 Also change the endpoint_name to "rf-PL-freqpunish" and algorithm name to "randomforrest-2" in file backend/server/server/wsgi.py 
 
 # Model 1
 # To run model 1-   <br />
 Accuracy on test and train set is 98.2% and test set is 97.9%   <br /> <br />
 

 http://127.0.0.1:8000/api/v1/rf-PL-rootfreqpunish/predict -use this url  <br />
 
 Change the address ,for self.model to the installed location of "Web_rf_1.joblib" in rf file present in backend/server/apps/ml/classifier/rf.py   <br />
 Also change the endpoint_name to "rf-PL-rootfreqpunish" and algorithm name to "randomforrest-1" in file backend/server/server/wsgi.py 
 
 # Further Improvement  and Comparision with Other models
 
 This model can be further improved by adding more data and all the relavent features required for the prediction (Classification Task). <br /> <br />
 Note that all parameters are tuned to maximize the results. <br /> <br />
 Random Forests/Decision can be trained to give better or same results as logistic regression always. This can be directly inferred from the logic that each split at the nodes divides the feature space into by two parts by a hyperplane (linear seperation in that region based on distance from hyperplane). <br /> <br />
 For practical purposes Logistic Regression is implemented in same 3 varaints for comparision and all the RandomForrest Varaints outperform correspoding Logistic Regressions models
 
 # Business Model
 Business Model can be interpretted from the decision tree image in the random forest classifier. Keep the model with highest punishment to False Positives (model 3) .<br /> This essentailly makes sure we loose very small amount of customers who are willing to take loan. <br /> This approach can be justified by the fact that cost of advertisements is very minute to the opportunity in a potential loan. <br /> Reasearch futher into why on certain zip codes the advertisement is more impactful and try inculcating those practices  . <br /> Target individuals based on the feature importances ( Income, CC AVg) and the decision tree graphs (see the visualization image in case_study) for high success rates of advertisements.
