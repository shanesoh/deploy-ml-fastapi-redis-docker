from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def index(self):
            self.client.get('/')

    @task
    def predict(self):
        with open('jemma.png', 'rb') as image:
            self.client.post('/predict', files={'img_file': image})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
