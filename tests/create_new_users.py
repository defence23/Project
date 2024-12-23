from http.client import responses

import requests
import random
import string


def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters, k = length))

def create_new_users(n):
    url = "http://localhost:8000/users/"


    for i in range(n):
        user = {
                "email" : f"user_{i}@example.com",
                "username" : f"user_{i}",
                "password" : generate_random_string(8)
               }

        responses= requests.post(url,json=user)
        print(f"Create user {i}:{responses.status_code}")
create_new_users(20)