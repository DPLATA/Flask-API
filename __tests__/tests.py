import requests
import json
import random
import string

def test_get_all_users_list_check_status_code_equals_200():
     response = requests.get('http://127.0.0.1:5000/get/users')
     
     # TODO: remove prints
     j = json.loads(response.text)
     print(j)

     assert response.status_code == 200

def test_get_single_user_detail_check_status_code_equals_200():
     response = requests.get('http://127.0.0.1:5000/get/users/1')
     
     # TODO: remove prints
     j = json.loads(response.text)
     print(j)

     assert response.status_code == 200

def test_post_user_check_status_code_equals_200():
     mimetype = 'application/json'
     headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
     }
     letters = string.ascii_lowercase
     random_username = ''.join(random.choice(letters) for i in range(10))
     data = {'email':random_username+'@testing.com', 'password':'somethingtest', 'name':'test_name4'}
     response = requests.post('http://127.0.0.1:5000/post/users', data=json.dumps(data), headers=headers)
     
     # TODO: remove prints
     j = json.loads(response.text)
     print(j)

     # TODO: assert response text vs. data sent
     
     assert response.status_code == 200

def test_post_address_check_status_code_equals_200():
     mimetype = 'application/json'
     headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
     }
     data = {'zip_code':'04350', 'municipality':'my_municipality', 'city':'sin_city', 'state':'quaker', 'country':'MX'}
     response = requests.post('http://127.0.0.1:5000/post/users/2/addresses', data=json.dumps(data), headers=headers)
     
     # TODO: remove prints
     j = json.loads(response.text)
     print(j)

     # TODO: assert response text vs. data sent
     
     assert response.status_code == 200
     
def test_put_to_update_address_check_status_code_equals_200():
     mimetype = 'application/json'
     headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
     }
     data = {'zip_code':'04370', 'municipality':'my_municipality_updated', 'city':'sin_city', 'state':'quaker', 'country':'MX'}
     response = requests.put('http://127.0.0.1:5000/update/users/1/addresses', data=json.dumps(data), headers=headers)
     
     # TODO: remove prints
     j = json.loads(response.text)
     print(j)

     # TODO: assert response text vs. data sent
     
     assert response.status_code == 200