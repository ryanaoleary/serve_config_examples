"""
Send requests to Ray's FruitMarket.

For details, please refer to:
https://github.com/ray-project/test_dag/blob/master/fruit.py.

- Use `FastHttpUser` raises "CPU usage was too high at some point during the test!"
"""
from locust import HttpUser, constant, task


class FruitUser(HttpUser):
    wait_time = constant(0)
    network_timeout = None
    connection_timeout = None

    @task
    def fruit_request(self):
        resp = self.client.post(
            "/fruit",
            json=["MANGO", 2],
            headers={"Content-Type": "application/json"},
        )
        body = resp.text
        if body != "6":
            resp.failure(f"unexpected response: {body}")
