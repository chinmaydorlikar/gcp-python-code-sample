from google.oauth2 import service_account
import google.auth.transport.requests

def get_access_token(self):
    credentials = service_account.Credentials.from_service_account_file("sa_file_name")
    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/cloud-platform'])
    request = google.auth.transport.requests.Request()
    scoped_credentials.refresh(request)
    access_token = scoped_credentials.token
    return access_token