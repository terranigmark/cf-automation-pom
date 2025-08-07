import requests

class APIHelper:
    BASE_API = "https://reqres.in/api"

    HEADERS = {
        "x-api-key": "reqres-free-v1"

    }

    def login(self, email, password):
        return requests.post(f"{self.BASE_API}/login",
                             json={"email": email, "password": password},
                             headers=self.HEADERS
                             )

    def is_service_up(self):
        response = requests.get(f"{self.BASE_API}/users/2",
                                headers=self.HEADERS
                                )
        return response.status_code == 200
