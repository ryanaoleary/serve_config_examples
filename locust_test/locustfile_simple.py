"""
Send requests to simple Serve application.

For details, please refer to:
https://github.com/JiangJiaWei1103/Incr-Upgrade-Locust/blob/main/simple_serve.py
"""
from locust import HttpUser, constant, task


class SimpleUser(HttpUser):
    wait_time = constant(0)
    network_timeout = None
    connection_timeout = None

    @task
    def test_request(self):
        resp = self.client.get("/test")
        if resp.status_code != 200:
            print(f"Error: {resp.status_code} - {resp.text}")
