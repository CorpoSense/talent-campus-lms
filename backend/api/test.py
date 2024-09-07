import requests
import json

BASE_URL = "https://8000-corposense-talentcampus-0wid12991xq.ws-eu116.gitpod.io"
bearer_token = None

def register_user():
    url = f"{BASE_URL}/auth/register/"
    data = {
        "username": "ibrahim",
        "email": "lahcen@gmail.com",
        "password": "password",
        "firstName": "Hassane",
        "lastName": "BENCHAREF",
        "type": "student",
        "interests": ["web dev"],
        "skills": ["js"],
        "industry_name": "IT"
    }
    response = requests.post(url, json=data)
    print("Register User:", response.status_code)
    print(response)

def login_user():
    global bearer_token
    url = f"{BASE_URL}/auth/login/"
    data = {
        "email": "lahcen@gmail.com",
        "password": "password"
    }
    response = requests.post(url, json=data)
    print("Login User:", response.status_code)
    response_data = response.json()
    print(response_data)
    if 'access' in response_data:
        bearer_token = response_data['access']
        print("Bearer Token:", bearer_token)

def reset_password():
    url = f"{BASE_URL}/auth/password_reset/"
    response = requests.get(url)
    print("Reset Password:", response.status_code)
    print(response.text)

def get_profile(user_id):
    url = f"{BASE_URL}/auth/profile/{user_id}/"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.get(url, headers=headers)
    print("Get Profile:", response.status_code)
    print(response.json())

def update_profile(user_id):
    url = f"{BASE_URL}/auth/profile/{user_id}/"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    data = {
        "first_name": "Lahcen",
        "last_name": "lahcen",
        "phone_number": "0674171417",
        "sexe": "Male"
    }
    response = requests.put(url, headers=headers, json=data)
    print("Update Profile:", response.status_code)
    print(response.json())

def refresh_token(user_id, refresh_token):
    url = f"{BASE_URL}/auth/refreshToken/{user_id}/"
    data = {"refreshToken": refresh_token}
    response = requests.post(url, json=data)
    print("Refresh Token:", response.status_code)
    print(response.json())

# Add more functions for other endpoints as needed

def main():
    register_user()
    login_user()
    reset_password()
    get_profile(3)
    update_profile(3)
    # Add calls to other endpoint functions here

if __name__ == "__main__":
    main()