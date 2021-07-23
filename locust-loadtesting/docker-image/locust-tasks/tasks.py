from locust import HttpUser, task, between
import base64
import os
from google.oauth2 import service_account
import google.auth.transport.requests

ENDPOINT = os.environ["endpoint"]

class WebsiteTestUser(HttpUser):
    wait_time = between(0.1, 0.2)
    @task()
    def hello_world(self):
        credentials = service_account.Credentials.from_service_account_file("file_name.json")
        scoped_credentials = credentials.with_scopes(
            ['https://www.googleapis.com/auth/cloud-platform'])
        request = google.auth.transport.requests.Request()
        scoped_credentials.refresh(request)
        access_token = scoped_credentials.token
        data = {"data": "my_data"}
        receiving_service_headers = {'Authorization': f'Bearer {access_token}'}
        res_ = self.client.post(ENDPOINT, json=data, headers=receiving_service_headers)
        if(res_.status_code!=200):
            print(res_.text)
