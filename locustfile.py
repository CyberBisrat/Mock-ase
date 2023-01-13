import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/")
        self.client.get("/")

    @task
    def upper(self):
        for _ in range(10):
            self.client.get(f"/str/upper?a=aaaa", name="/str/upper")
            time.sleep(1)
    
    @task
    def mul(self):
        for a in range(10):
            self.client.get(f"/math/mul?a={a}00&b=99999", name="/math/mul")
            time.sleep(1)

    @task
    def stats(self):
        for _ in range(10):
            self.client.get(f"/stats", name="/stats")
            time.sleep(1)