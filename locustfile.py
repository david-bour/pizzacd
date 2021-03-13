import time
import random
from locust import HttpUser, task, between

class Metric(HttpUser):

    wait_time = between(1, 1.5)

    @task
    def attack(self):
        self.client.get('/api/cache/info')

    @task(3)
    def add_load(self):
        random_number = random.randint(1, 10000)
        self.client.post(f'/api/cache/{random_number}')

    @task(2)
    def get_load(self):
        self.client.get(f'/api/cache/1')