import requests

def test_get_employee_details_check_status_code_equals_200():
     response = requests.get('http://127.0.0.1:5000/')
     assert response.status_code == 200
