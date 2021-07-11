import requests
import json
import random
import string

def test_get_all_users_list_check_status_code_equals_200():
     response = requests.get('http://127.0.0.1:5000/users')
     j = json.loads(response.text)
     print(j)
     assert response.status_code == 200

def test_post_user_check_response_ok():
     mimetype = 'application/json'
     headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
     }
     letters = string.ascii_lowercase
     random_username = ''.join(random.choice(letters) for i in range(10))
     data = {'email':random_username+'@testing.com', 'password':'somethingtest', 'name':'test_name4'}
     response = requests.post('http://127.0.0.1:5000/users', data=json.dumps(data), headers=headers)
     j = json.loads(response.text)
     print(j)
     # assert j vs. data
     assert response.status_code == 200