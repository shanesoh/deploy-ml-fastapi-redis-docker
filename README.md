# Deploy and Scale Machine Learning Models with Keras, FastAPI, Redis and Docker Swarm
Serve a production-ready and scalable Keras-based deep learning model image classification using FastAPI, Redis and Docker Swarm. Based off this [series of blog posts](https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/).

## How to Use

### Prerequisites
Make sure you have a modern version of `docker` (>1.13.0)and `docker-compose` installed.

### Run with Docker Compose
Simply run `docker-compose up` to spin up all the services on your local machine.

### Test Service
* Test the `/predict` endpoint by passing in the included `doge.jpg` as parameter `img_file`:

```bash
curl -X POST -F img_file=@doge.jpg http://localhost/predict
```

You should see the predictions returned as a JSON response.

### Deploy on Docker Swarm
Deploying this on Docker Swarm allows us to scale the model server to multiple hosts. 

This assumes that you have a Swarm instance set up (e.g. on the cloud). Otherwise, to test this in a local environment, put your Docker engine in swarm mode with `docker swarm init`.

* Deploy the stack on the swarm:

```bash
docker stack deploy -c docker-compose.yml mldeploy
```

* Check that it's running with `docker stack services mldeploy`. Note that the model server is unreplicated at this time. You may scale up the model worker by:

```bash
docker service scale mldeploy_modelserver=X
```

Where `X` is the number of workers you want.

## Load Testing
We can use [locust](https://locust.io) and the included `locustfile.py` to load test our service. Run the following command to spin up `20` concurrent users immediately:

```bash
locust --host=http://localhost --no-web -c 20 -r 20
```

The `--no-web` flag runs locust in CLI mode. You may also want to use locust's web interface with all its pretty graphs, if so, just run `local --host=http://localhost`.
