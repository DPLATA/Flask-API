import requests
from requests.models import Response

# def test_get_employee_details_check_status_code_equals_200():
     # response = requests.get('http://127.0.0.1:5000/')
     # assert response.status_code == 200

def test_post_user_check_response_ok():
     data = {'email':'test@test.com','password':'something', 'name':'test_name'}
     response = requests.post('http://127.0.0.1:5000/users', data=data)
     assert response.status_code == 200
