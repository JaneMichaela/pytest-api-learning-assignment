import requests

def test_login_success_reqres(secrets_login): # secrets_login is a pytest fixture
    url = "https://reqres.in/api/login"
    json = {
        ....
    }
    headers = {
        ....
    }
    response = requests.post(url, headers=headers, json=json)
    
    assert response.status_code == 200  