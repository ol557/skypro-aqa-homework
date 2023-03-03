import requests
base_url = 'https://x-clients-be.onrender.com'

def get_company_list(params_to_add = None):
    resp = requests.get(base_url+ '/company', params=params_to_add)
    return resp.json()

def get_token(user = 'michaelangelo', password = 'party-dude'):
    creds = {
        'username' : user,
        'password' : password
        }
    resp = requests.post(base_url+'/auth/login', json=creds)
    return resp.json()["userToken"]

def test_get_companies():
    body = get_company_list()
    
    assert len(body) >0
    
    
def test_get_active_companies():
    #Получаем список всех компаний
    full_list = get_company_list()
    #Получаем список активных компаний
    #my_params = {'active' : 'true'} 
    #resp = requests.get('https://x-clients-be.onrender.com/company', params=my_params)
    #альтернативное решение
    active_list = get_company_list(params_to_add={'active' : 'true'})

    assert len(full_list) > len(active_list)

def test_add_new():
    body = get_company_list()
    len_before = len(body)

    company = {
        'name': 'Решение',
        'description': 'Самостоятельное'
    }
    
    my_headers = {}
    my_headers["x-client-token"] = get_token()

    resp = requests.post(base_url+'/company', json=company, headers=my_headers)

    body = get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
