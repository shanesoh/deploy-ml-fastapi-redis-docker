# Deploy and Scale Machine Learning Models with Keras, FastAPI, Redis and Docker Swarm
Serve a production-ready and scalable Keras-based deep learning model image classification using FastAPI, Redis and Docker Swarm. Based off this [series of blog posts](https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/).

## How to Use

### Prerequisites
Make sure you have a modern version of `docker` (>1.13.0)and `docker-compose` installed.

### Build Images
* In project directory, use `docker-compose` to build the images:

```bash
docker-compose build
```

* Using Docker Swarm requires that these built images are pushed to a registry (so that Swarm can distribute the images to all the Docker Engines in a swarm). We'll use a local Docker registry for this purpose. We can use the official Docker `registry` image to start one:

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

* Now we can push our newly built images to the registry:

```bash
docker-compose push
```

### Deploy Images to a Docker Swarm
* Assuming you're testing this in a local environment, make sure your engine is in swarm mode with `docker swarm init`.

* Deploy the stack on the swarm:

```bash
docker stack deploy -c docker-compose.yml mldeploy
```

* Check that it's running with `docker stack services mldeploy`. Notice that the model server is replicated twice. You can increase this to handle more requests but ensure your server has sufficient resources (RAM and CPU) to handle the replication.


### Test Service
* Test the service by `curl`ing the endpoint:

```bash
curl http://localhost
```

You should see `"Hello World!"` as a response.

* Test the `/predict` endpoint by passing in the included `doge.jpg` as parameter `img_file`:

```bash
curl -X POST -F img_file=@doge.jpg http://localhost/predict
```

## Load Testing
We can use [locust](https://locust.io) and the included `locustfile.py` to load test our service. Run the following command to spin up `20` concurrent users immediately:

```bash
locust --host=http://localhost --no-web -c 20 -r 20
```

The `--no-web` flag runs locust in CLI mode. You may also want to use locust's web interface with all its pretty graphs, if so, just run `local --host=http://localhost`.
