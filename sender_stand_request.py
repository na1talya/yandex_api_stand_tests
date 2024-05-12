# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

def get_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")

def post_new_client_kit(kit_body, auth_token):
    headers_new = data.headers.copy()
    headers_new["Authorization"] = "Bearer + auth_token"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=headers_new)
response = post_new_client_kit(data.kit_body, data.headers.copy);
print(response.status_code)
print(response.json())
