from locust import SequentialTaskSet, task, constant_pacing
from locust.contrib.fasthttp import FastHttpUser
from os import environ as env
import json
import random
import string


def random_alphanum(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class LocustDemoSequence(SequentialTaskSet):

    token = env["GOREST_TOKEN"]
    user_id = 0

    @task
    def list_users(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        r = self.client.get("/public/v1/users", headers=headers, name="list users")
        # print(r.json())


    @task
    def create_user(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        first_name = random_alphanum(random.randint(3,8))
        last_name = random_alphanum(random.randint(4,12))
        body = {
            "name": f"{first_name} {last_name}",
            "gender": random.choice(["male", "female"]),
            "email": f"{first_name}.{last_name}@somewhere.com",
            "status": "active"
        }
        r = self.client.post("/public/v1/users", json.dumps(body), headers=headers, name="create user")
        self.user_id = r.json()["data"]["id"]
        # print(r.json())
    

    @task
    def update_user(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        body = {
            "status": "inactive"
        }
        r = self.client.patch(
            f"/public/v1/users/{self.user_id}",
            json.dumps(body),
            headers=headers,
            name="update user"
        )
        # print(r.json())


    @task
    def delete_user(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        r = self.client.delete(
            f"/public/v1/users/{self.user_id}",
            headers=headers,
            name="delete user"
        )
        


class DemoUser(FastHttpUser):
    tasks = {LocustDemoSequence: 1}
    wait_time = constant_pacing(10.0)
