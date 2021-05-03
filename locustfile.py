import time
import random
from locust import HttpUser, task, between

class Metric(HttpUser):

    wait_time = between(1, 2)

    @task
    def attack(self):
        # self.client.post('/api/graph/sausage')
        self.client.post('/graph/sausage')

    # @task(3)
    # def add_load(self):
    #     random_number = random.randint(1, 10000)
    #     self.client.post(f'/api/cache/{random_number}')

    @task(2)
    def get_load(self):
        # self.client.get(f'/api/graph')
        self.client.get(f'/graph')

    @task(3)
    def upload(self):
        random_number = random.randint(1, 5)
        self.client.get(f'/memory/file/{random_number}')

    @task(4)
    def grand_upload(self):
        self.client.get(f'/memory/file')