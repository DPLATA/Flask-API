import requests

def test_get_employee_details_check_status_code_equals_200():
     response = requests.get("")
     assert response.status_code == 200
