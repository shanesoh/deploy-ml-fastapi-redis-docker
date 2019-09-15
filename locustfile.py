from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def predict(self):
        with open('jemma.png', 'rb') as image:
            self.client.post('/predict', files={'img_file': image})


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 500
    max_wait = 5000
