from locust import task, between, events, User
import boto3
import json
import os, sys
import time
import numpy as np
import pandas as pd

sagemaker_runtime = boto3.client('sagemaker-runtime')

endpoint_name=os.environ['ENDPOINT_NAME']

csv_test_filename = 'churn_test.csv'

x_test = pd.read_csv(csv_test_filename)

def sample_data(df):
    sample=df.sample()
    state=sample['State'].values[0]
    data=np.array2string(sample.values[0][3:], separator=',', 
                         max_line_width=10000)[1:-1]
    target_model=f'churn-xgb-{state}.tar.gz'
    
    return data, target_model

class SMLoadTestUser(User):
    wait_time = between(0, 2)
    
    @task
    def test_endpoint(self):
        data, target_model = sample_data(x_test)
        start_time = time.time()
        try:
            sagemaker_runtime.invoke_endpoint(
                            EndpointName=endpoint_name, 
                            ContentType='text/csv',
                            TargetModel=target_model,
                            Body=data)
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(
                request_type="sagemaker-mme",
                name=endpoint_name,
                response_time=total_time,
                response_length=0,
            )

        except:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type="sagemaker-mme",
                name=endpoint_name,
                response_time=total_time,
                response_length=0,
                exception=sys.exc_info(),
            )
