import httpx


login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


header_authorization = {
    "Authorization": f"Bearer {login_response_data.get('token').get('accessToken')}"
}  # Настаиваю на такой работе со словарями. Работая через метод get мы не рискуем трейсбэком, если в словаре нет ключа

users_me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=header_authorization)
print(users_me_response.json(), users_me_response.status_code)
