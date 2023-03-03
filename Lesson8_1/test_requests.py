import requests
base_url = 'https://x-clients-be.onrender.com'

#запрос на полчение списка компаний
def test_simple_rest():
    resp = requests.get(base_url+'/company')

    responce_body = resp.json()
    first_copmpany = responce_body[3]
    assert first_copmpany["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

#авторизация и получение токена
def test_auth():
    creds = {
        'username' : 'michaelangelo',
        'password' : 'party-dude'
    }
    
    resp = requests.post(base_url+'/auth/login', json = creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

def test_create_company():
    creds = {
        'username' : 'michaelangelo',
        'password' : 'party-dude'
    }
    company = {
        'name': 'Решение',
        'description': 'Самостоятельное'
    }
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]

    my_headers = {}
    my_headers["x-client-token"] = token

    resp = requests.post(base_url+'/company', json=company, headers=my_headers)
    


    assert resp.status_code == 201
